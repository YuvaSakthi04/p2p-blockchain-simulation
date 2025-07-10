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

## Working

1. Each Flask server is a **node** in the blockchain network.
2. Users can:
   - Submit transactions
   - Mine new blocks
   - View the chain
   - Register other nodes
   - Resolve chain conflicts
3. Transactions are stored temporarily until mined into a block.
4. **Proof of Work (PoW)** ensures mining takes computational effort.
5. Nodes **sync** using the longest valid chain when conflicts arise.

### Dashboard View
![Dashboard](screenshots/Node_1.png)

### Node 2
![Dashboard](screenshots/Node_2.png)

### Node 3
![Dashboard](screenshots/Node_3.png)

### Adding Transaction
![Transaction](screenshots/Adding_Transaction.png)

### Pending Transaction before mining
![Pending Transaction](screenshots/Pending_Transaction_before_mining.png)

### Peer Node Registering for Node 2
![Peer node registering for Node2](screenshots/Peer_node_of_Node2.png)

### Mining Block in Node 1
![Mining Block](screenshots/After_mining_block_in_node1.png)

### Resolving Conflicts in Node 2
![Resolving conflicts in node 2](screenshots/After_resolving_conflicts.png)
