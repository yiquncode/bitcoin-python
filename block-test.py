import unittest

from block import Block

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.data = 'bar'
        self.prev_block = Block.genesis()
        self.block = Block.mine_block(self.prev_block,self.data)

    def test_create_block(self):
        self.assertEqual(self.block.data, self.data)

        print('check the prev_hash of current block vs the hash of prev block')
        self.assertEqual(self.block.prev_hash,self.prev_block.block_hash)
    
    def test_create_hash(self):
        print(Block.create_hash("ss","22","33"))
        
if __name__ == '__main__':
    unittest.main()