# Voorraadkast

A small local web app for keeping track of home emergency supplies: what you have, what's still to buy, where it's stored and when it expires.

- Counts, targets, units, storage spots, expiry dates and notes per item
- Status at a glance: ready, below target, to buy, expiring within 60 days, expired
- Water and food reserves for your household size and number of days (2 L and 2,000 kcal per person per day)
- Categories from water and food to safety, pets and entertainment, each with its own emoji per item
- Light and dark mode, works on phones

## Run it

Needs only Python 3, no packages to install.

```sh
python3 server.py
```

Then open http://localhost:8765. The server only listens on your own computer.

Your supplies are saved in `data.json` next to `server.py`. On first run it is created with a few example items, which you can remove from the page. `data.json` is in `.gitignore`, so your own list is never committed.

To use another port: `PORT=9000 python3 server.py`.
