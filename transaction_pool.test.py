import unittest
from transaction_pool import TransactionPool
from wallet import Wallet
from transaction import Transaction

class TestTransactionPool(unittest.TestCase):

    def setUp(self):
        self.tp = TransactionPool()
        self.wallet = Wallet()
        self.recipient = 'r3co09ow99'
        self.transaction = Transaction.new_transaction(self.wallet, self.recipient, 30)
        self.tp.update_or_add(self.transaction)
    
    def test_add_transaction_to_pool(self):
        self.assertEqual(self.tp.transactions[0].id, self.transaction.id)
    
    def test_update_pool(self):
        old = str(self.transaction.__dict__)
        new = self.transaction.insert_output(self.wallet, 'k5co09ow99', 10)
        self.tp.update_or_add(new)
        
        self.assertNotEqual(old, str(self.tp.transactions[0].__dict__))

if __name__ == '__main__':
    unittest.main()