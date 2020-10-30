import json
import base64
from types import SimpleNamespace
from p2pnetwork.node import Node

class MyOwnPeer2PeerNode (Node):

    def __init__(self, host, port, blockchain):
        super(MyOwnPeer2PeerNode, self).__init__(host, port, None)
        self.blockchain = blockchain

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)
        
    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)
        encoded = base64.b64encode(str.encode(self.blockchain.to_json()))
        self.send_to_node(connected_node, encoded)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        # print("node_message from " + connected_node.id + ": " + str(data))
        data = base64.b64decode(data) # Keep data format, in my case if I send json string directly the character " was changed to '
        data = data.decode()
        chain = json.loads(data)
        self.blockchain.replace_chain_from_json(chain)
        
    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop!")