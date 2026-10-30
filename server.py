#!/usr/bin/env python3
"""Voorraadkast: a tiny local server.

Serves index.html and keeps supplies in data.json next to this file.
Run: python3 server.py   then open http://localhost:8765
"""
import json
import os
import sys
import threading
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "data.json")
INDEX_FILE = os.path.join(HERE, "index.html")
HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8765"))

EXAMPLES = [
    {"name": "Bottled water, 1.5 L", "category": "Water", "location": "Garage shelf", "qty": 12, "target": 16, "unit": "L", "expires": "2027-08-01", "notes": "Rotate into the kitchen each spring."},
    {"name": "Canned beans", "category": "Food", "location": "Pantry, bottom shelf", "qty": 6, "target": 6, "unit": "cans", "kcal": 300, "expires": "2026-12-10", "notes": ""},
    {"name": "First aid kit", "category": "First aid", "location": "Hall closet", "qty": 1, "target": 1, "unit": "pcs", "expires": None, "notes": "Check plasters and painkillers."},
    {"name": "AA batteries", "category": "Power & light", "location": "Kitchen drawer", "qty": 4, "target": 12, "unit": "pcs", "expires": "2030-03-01", "notes": "For torches and the radio."},
    {"name": "Energy bars", "category": "Food", "location": "Go-bag", "qty": 10, "target": 10, "unit": "pcs", "kcal": 200, "expires": "2026-09-15", "notes": ""},
    {"name": "LED torch", "category": "Power & light", "location": "Hall closet", "qty": 2, "target": 2, "unit": "pcs", "expires": None, "notes": ""},
]

lock = threading.Lock()


def load():
    if not os.path.exists(DATA_FILE):
        data = {
            "household": {"people": 2, "days": 3},
            "supplies": {"ex-%d" % i: dict(e, example=True) for i, e in enumerate(EXAMPLES)},
        }
        save(data)
        return data
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def save(data):
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, DATA_FILE)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def send_json(self, status, body=None):
        payload = b"" if body is None else json.dumps(body).encode("utf-8")
        self.send_response(status)
        if body is not None:
            self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def read_body(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(length) or b"{}")
        if not isinstance(body, dict):
            raise ValueError("body must be an object")
        return body

    def supply_id(self):
        prefix = "/api/supplies/"
        return self.path[len(prefix):] if self.path.startswith(prefix) else None

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(INDEX_FILE, "rb") as f:
                page = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.end_headers()
            self.wfile.write(page)
        elif self.path == "/api/supplies":
            with lock:
                data = load()
            self.send_json(200, [dict(v, id=k) for k, v in data["supplies"].items()])
        elif self.path == "/api/household":
            with lock:
                self.send_json(200, load()["household"])
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/supplies":
            return self.send_json(404, {"error": "not found"})
        try:
            body = self.read_body()
        except ValueError:
            return self.send_json(400, {"error": "invalid JSON"})
        new_id = uuid.uuid4().hex[:12]
        with lock:
            data = load()
            data["supplies"][new_id] = body
            save(data)
        self.send_json(201, dict(body, id=new_id))

    def do_PUT(self):
        try:
            body = self.read_body()
        except ValueError:
            return self.send_json(400, {"error": "invalid JSON"})
        with lock:
            data = load()
            if self.path == "/api/household":
                data["household"] = {"people": int(body.get("people", 2)), "days": int(body.get("days", 3))}
            else:
                sid = self.supply_id()
                if not sid:
                    return self.send_json(404, {"error": "not found"})
                body.pop("id", None)
                data["supplies"][sid] = body
            save(data)
        self.send_json(204)

    def do_PATCH(self):
        sid = self.supply_id()
        try:
            body = self.read_body()
        except ValueError:
            return self.send_json(400, {"error": "invalid JSON"})
        with lock:
            data = load()
            if sid not in data["supplies"]:
                return self.send_json(404, {"error": "not found"})
            body.pop("id", None)
            data["supplies"][sid].update(body)
            save(data)
        self.send_json(204)

    def do_DELETE(self):
        sid = self.supply_id()
        with lock:
            data = load()
            data["supplies"].pop(sid, None)
            save(data)
        self.send_json(204)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print("Voorraadkast running at http://localhost:%d  (Ctrl+C to stop)" % PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)
