import json
import logging

from flask import Flask, request, jsonify, redirect

from blockchain import Blockchain

app = Flask(__name__)
bc = Blockchain()

@app.route('/blocks')
def blocks():
    j = bc.to_json()
    return j

@app.route('/mine', methods=['POST'])
def mine():
    content = request.json
    bc.add_block(content["data"])
    logging.info('New block added: %s', content["data"])
    return redirect('/blocks')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3000)