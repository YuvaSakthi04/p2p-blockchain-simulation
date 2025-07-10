from flask import Flask, jsonify, request, render_template, redirect, url_for
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain,
                           transactions=blockchain.current_transactions,
                           peers=blockchain.nodes,
                           port=request.host.split(":")[-1])

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])
    blockchain.add_transaction(sender="0", recipient=node_id, amount=1)
    block = blockchain.create_block(proof, blockchain.hash(last_block))
    return redirect(url_for('index'))

@app.route('/transactions/new', methods=['POST'])
def new_transaction_form():
    sender = request.form['sender']
    recipient = request.form['recipient']
    amount = request.form['amount']
    blockchain.add_transaction(sender, recipient, float(amount))
    return redirect(url_for('index'))

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)})

@app.route('/nodes/register', methods=['POST'])
def register_node_form():
    node_url = request.form['node_url']
    blockchain.register_node(node_url)
    return redirect(url_for('index'))

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    blockchain.resolve_conflicts()
    return redirect(url_for('index'))

if __name__ == '__main__':
    import sys
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)