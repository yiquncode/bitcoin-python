import json

from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]
    
    def add_block(self,data):
        prev_block = self.chain[-1]
        block = Block.mine_block(prev_block, data)
        self.chain.append(block)

        return block
    
    def to_json(self):
        return json.dumps([ob.__dict__ for ob in self.chain])
    
    def is_vaild_chain(self, chain):
        if json.dumps(chain[0].__dict__) != json.dumps(Block.genesis().__dict__): return False

        for i in range(1, len(chain)):
            block = chain[i]
            prev_block = chain[i-1]

            if block.prev_hash != prev_block.block_hash or block.block_hash != Block.create_block_hash(block):
                return False
        
        return True
    
    def is_vaild_chain_from_json(self, chain):
        if type(chain) is str:
            chain = json.loads(chain)

        if Block.genesis().__dict__ != chain[0]: return False

        for i in range(1, len(chain)):
            block = chain[i]
            prev_block = chain[i-1]

            if block['prev_hash'] != prev_block['block_hash'] or block['block_hash'] != Block.create_block_hash(block):
                return False
        
        return True

    
    def replace_chain(self, new_chain):
        if len(new_chain) <= len(self.chain):
            print('Recevied chain is not longer than the current chain.')
            return
        elif self.is_vaild_chain(new_chain) == False:
            print('The recevied chain is not valid.')
            return
        
        print('Replacing blockchain with the new chain.')
        self.chain = new_chain

    def replace_chain_from_json(self, new_chain):
        if type(new_chain) is str:
            new_chain = json.loads(new_chain)
        if len(new_chain) <= len(self.chain):
            print('Recevied chain is not longer than the current chain.')
            return
        elif self.is_vaild_chain_from_json(new_chain) == False:
            print('The recevied chain is not valid.')
            return
        
        c = [Block.genesis()]

        for i in range(1, len(new_chain)):
            str_block = new_chain[i]
            obj_block = Block(str_block['timestamp'], str_block['prev_hash'], str_block['block_hash'], str_block['data'], str_block['nonce'], str_block['difficulty'])
            c.append(obj_block)

        print('Replacing blockchain with the new chain.')
        self.chain = c