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
    
    def is_vaild_chain(self,chain):
        if json.dumps(chain[0].__dict__) != json.dumps(Block.genesis().__dict__): return False

        for i in range(1, len(chain)):
            block = chain[i]
            prev_block = chain[i-1]

            if block.prev_hash != prev_block.block_hash or block.block_hash != Block.create_block_hash(block):
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
