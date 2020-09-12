import time
import hashlib
import json

class Block:
    def __init__(self, timestamp, prev_hash, block_hash, data):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.block_hash = block_hash
        self.data = data
    
    def to_string(self):
        self.timestamp
    
    @staticmethod
    # https://en.bitcoin.it/wiki/Genesis_block The genesis block is almost always hardcoded into the software
    def genesis():
        return Block('1231006505.7165034','00000000000000','000000000019d6','The Times 03/Jan/2009 Chancellor on brink of second bailout for banks')
    
    @staticmethod
    def mine_block(prev_block, data):
        timestamp = time.time()
        prev_hash = prev_block.block_hash
        block_hash = Block.create_hash(timestamp, prev_hash, data)

        return Block(timestamp,prev_hash,block_hash,data)
    
    @staticmethod
    def create_hash(timestamp, prev_hash, data):
        m = hashlib.sha256()
        m.update(('%s%s%s' % (timestamp, prev_hash, data)).encode('utf-8'))
        return m.hexdigest()
    
    @staticmethod
    def create_block_hash(block):
        return Block.create_hash(block.timestamp, block.prev_hash, block.data)