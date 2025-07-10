## P2P Blockchain Simulation

This project simulates a Peer-to-Peer (P2P) blockchain network using Python, Flask, and HTTP communication. 
Each node maintains its own blockchain, mines blocks with Proof of Work (PoW), registers peers, and resolves conflicts to stay in sync with the longest chain rule.


## Features

- Add new transactions via a web form
- Mine blocks with basic Proof of Work(PoW)
- View blockchain in JSON
- Register peer nodes
- Sync chains using the "longest chain wins" consensus
- Web dashboard for user interaction (HTML + CSS)

## Tech Stack

- Python 3.x
- Flask (web framework)
- `requests` (for peer-to-peer HTTP communication)
- HTML/CSS (Flask templates for dashboard)
