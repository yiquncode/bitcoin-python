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
    
    def test_hash_match_difficulty(self):
        self.assertEqual(self.block.block_hash[0:self.block.difficulty],'0'*self.block.difficulty)
        print(self.block.__dict__)
    
    def test_mined_too_slow(self):
        self.assertEqual(Block.addjust_difficulty(self.block, self.block.timestamp + 36000), self.block.difficulty - 1)

    def test_mined_too_easy(self):
        self.assertEqual(Block.addjust_difficulty(self.block, self.block.timestamp + 1), self.block.difficulty + 1)

if __name__ == '__main__':
    unittest.main()