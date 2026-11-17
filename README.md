<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 26 26" width="128px" align="left">

  <path d="M25.50 13.00 L25.50 16.42 L25.48 17.52 L25.47 18.31 L25.44 18.95 L25.40 19.50 L25.36 19.99 L25.31 20.42 L25.25 20.81 L25.19 21.18 L25.11 21.51 L25.03 21.82 L24.94 22.11 L24.84 22.39 L24.73 22.64 L24.61 22.88 L24.48 23.11 L24.35 23.32 L24.20 23.52 L24.05 23.71 L23.88 23.88 L23.71 24.05 L23.52 24.20 L23.32 24.35 L23.11 24.48 L22.88 24.61 L22.64 24.73 L22.39 24.84 L22.11 24.94 L21.82 25.03 L21.51 25.11 L21.18 25.19 L20.81 25.25 L20.42 25.31 L19.99 25.36 L19.50 25.40 L18.95 25.44 L18.31 25.47 L17.52 25.48 L16.42 25.50 L13.00 25.50 L9.58 25.50 L8.48 25.48 L7.69 25.47 L7.05 25.44 L6.50 25.40 L6.01 25.36 L5.58 25.31 L5.19 25.25 L4.82 25.19 L4.49 25.11 L4.18 25.03 L3.89 24.94 L3.61 24.84 L3.36 24.73 L3.12 24.61 L2.89 24.48 L2.68 24.35 L2.48 24.20 L2.29 24.05 L2.12 23.88 L1.95 23.71 L1.80 23.52 L1.65 23.32 L1.52 23.11 L1.39 22.88 L1.27 22.64 L1.16 22.39 L1.06 22.11 L0.97 21.82 L0.89 21.51 L0.81 21.18 L0.75 20.81 L0.69 20.42 L0.64 19.99 L0.60 19.50 L0.56 18.95 L0.53 18.31 L0.52 17.52 L0.50 16.42 L0.50 13.00 L0.50 9.58 L0.52 8.48 L0.53 7.69 L0.56 7.05 L0.60 6.50 L0.64 6.01 L0.69 5.58 L0.75 5.19 L0.81 4.82 L0.89 4.49 L0.97 4.18 L1.06 3.89 L1.16 3.61 L1.27 3.36 L1.39 3.12 L1.52 2.89 L1.65 2.68 L1.80 2.48 L1.95 2.29 L2.12 2.12 L2.29 1.95 L2.48 1.80 L2.68 1.65 L2.89 1.52 L3.12 1.39 L3.36 1.27 L3.61 1.16 L3.89 1.06 L4.18 0.97 L4.49 0.89 L4.82 0.81 L5.19 0.75 L5.58 0.69 L6.01 0.64 L6.50 0.60 L7.05 0.56 L7.69 0.53 L8.48 0.52 L9.58 0.50 L13.00 0.50 L16.42 0.50 L17.52 0.52 L18.31 0.53 L18.95 0.56 L19.50 0.60 L19.99 0.64 L20.42 0.69 L20.81 0.75 L21.18 0.81 L21.51 0.89 L21.82 0.97 L22.11 1.06 L22.39 1.16 L22.64 1.27 L22.88 1.39 L23.11 1.52 L23.32 1.65 L23.52 1.80 L23.71 1.95 L23.88 2.12 L24.05 2.29 L24.20 2.48 L24.35 2.68 L24.48 2.89 L24.61 3.12 L24.73 3.36 L24.84 3.61 L24.94 3.89 L25.03 4.18 L25.11 4.49 L25.19 4.82 L25.25 5.19 L25.31 5.58 L25.36 6.01 L25.40 6.50 L25.44 7.05 L25.47 7.69 L25.48 8.48 L25.50 9.58Z" fill="#ffffff" stroke="#d4d4da" stroke-width="0.4"/><path d="M13 7v12M7 13h12" fill="none" stroke="#df433d" stroke-width="2.6" stroke-linecap="round"/>
</svg>

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
