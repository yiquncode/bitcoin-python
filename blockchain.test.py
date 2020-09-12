import unittest

from block import Block
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.bc = Blockchain()
        self.bc2 = Blockchain()
    
    def test_starts_with_genesis_block(self):
        self.assertEqual(self.bc.chain[0].block_hash, Block.genesis().block_hash)

    def test_add_new_block(self):
        data = 'foo'
        self.bc.add_block(data)
        self.assertEqual(self.bc.chain[-1].data,data)
    
    def test_validates_a_valid_chain(self):
        self.bc2.add_block('foo')
        self.assertTrue(self.bc.is_vaild_chain(self.bc2.chain))

    def test_bad_genesis_block_is_invalid(self):
        self.bc2.chain[0].data = 'bad data'

        self.assertFalse(self.bc.is_vaild_chain(self.bc2.chain))
    
    def test_bad_block_is_invalid(self):
        self.bc2.add_block('foo')
        self.bc2.chain[1].data = 'bad data'

        self.assertFalse(self.bc.is_vaild_chain(self.bc2.chain))
    
    def test_replace_the_chain_with_a_valid_chain(self):
        self.bc2.add_block('bar')
        self.bc.replace_chain(self.bc2.chain)

        self.assertEqual(self.bc.chain, self.bc2.chain)
    
    def test_not_replace_with_less_chain(self):
        self.bc.add_block('foo')
        self.bc.replace_chain(self.bc2.chain)

        self.assertNotEqual(self.bc.chain, self.bc2.chain)

if __name__ == '__main__':
    unittest.main()