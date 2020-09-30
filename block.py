import time
import hashlib
import json

import config

DIFFICULTY = config.miner["DIFFICULTY"]

class Block:
    def __init__(self, timestamp, prev_hash, block_hash, data, nonce, difficulty):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.block_hash = block_hash
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty
    
    @staticmethod
    # https://en.bitcoin.it/wiki/Genesis_block The genesis block is almost always hardcoded into the software
    def genesis():
        return Block(1231006505.7165034,'00000000000000','000000000019d6','The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',0,DIFFICULTY)
    
    @staticmethod
    def mine_block(prev_block, data):
        prev_hash = prev_block.block_hash
        difficulty = prev_block.difficulty
        nonce = 0
        block_hash = "INIT"

        while block_hash[0:difficulty] != '0'*difficulty:
            nonce += 1
            timestamp = time.time()
            difficulty = Block.addjust_difficulty(prev_block, timestamp)
            block_hash = Block.create_hash(timestamp, prev_hash, data, nonce, difficulty)
            

        return Block(timestamp, prev_hash, block_hash, data, nonce, difficulty)
    
    @staticmethod
    def create_hash(timestamp, prev_hash, data, nonce, difficulty):
        m = hashlib.sha256()
        m.update(('%s%s%s%s%s' % (timestamp, prev_hash, data, nonce, difficulty)).encode('utf-8'))
        return m.hexdigest()
    
    @staticmethod
    def create_block_hash(block):
        return Block.create_hash(block.timestamp, block.prev_hash, block.data, block.nonce, block.difficulty)
    
    @staticmethod
    def addjust_difficulty(prev_block, current_time):
        difficulty = prev_block.difficulty
        difficulty = difficulty + 1 if prev_block.timestamp + config.miner["MINE_RATE"] > current_time else difficulty - 1
        return difficulty