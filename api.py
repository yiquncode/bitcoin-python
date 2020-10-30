import os
import json
import logging
import threading
import base64

from flask import Flask, request, jsonify, redirect

from blockchain import Blockchain
from p2p import MyOwnPeer2PeerNode
from wallet import Wallet
from transaction_pool import TransactionPool

app = Flask(__name__)

bc = Blockchain()
wallet = Wallet()
tp = TransactionPool()

# Use diffierent ports to simulate nodes in my development environment. 
# It will be distinguish by ip address in real world.
HTTP_PORT = os.environ["HTTP_PORT"] if 'HTTP_PORT' in os.environ else 3000 # export HTTP_PORT=3001
P2P_PORT = int(os.environ["P2P_PORT"]) if 'P2P_PORT' in os.environ else 5001 # export P2P_PORT=5002
node = MyOwnPeer2PeerNode("127.0.0.1", int(P2P_PORT), bc)

@app.route('/blocks')
def blocks():
    j = bc.to_json()
    return j

@app.route('/mine', methods=['POST'])
def mine():
    content = request.json
    bc.add_block(content["data"])
    logging.info('New block added: %s', content["data"])
    encoded = base64.b64encode(str.encode(bc.to_json()))
    node.send_to_nodes(encoded)
    return redirect('/blocks')

@app.route('/transactions')
def transactions():
    return tp.to_json()

@app.route('/transact', methods=['POST'])
def transact():
    content = request.json
    wallet.create_transaction(content['recipient'], content['amount'], tp)
    return redirect('/transactions')

if __name__ == '__main__':
    node.start()
    # Hardcode a master seed for p2p nodes cold start
    print(P2P_PORT)
    if P2P_PORT == 5002:
        node.connect_with_node('127.0.0.1', 5001)

    if P2P_PORT == 5003:
        node.connect_with_node('127.0.0.1', 5001)
        
    app.run(host='0.0.0.0', port=HTTP_PORT)