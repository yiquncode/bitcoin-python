import unittest
from transaction_pool import TransactionPool
from wallet import Wallet

class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        self.tp = TransactionPool()
        self.send_amount = 50
        self.recipient = 'r3co09ow99'
    
    def test_create_transaction(self):
        t = self.wallet.create_transaction(self.recipient, self.send_amount, self.tp)
        self.wallet.create_transaction(self.recipient, self.send_amount, self.tp)
        
        for item in t.outputs:
            if item['address'] == self.wallet.public_key:
                print()
                self.assertEqual(item['amount'], self.wallet.balance - self.send_amount * 2)

    def test_outputs(self):
        t = self.wallet.create_transaction(self.recipient, self.send_amount, self.tp)
        self.wallet.create_transaction(self.recipient, self.send_amount, self.tp)

        a = []
        for item in t.outputs:
            if item['address'] == self.recipient:
                a.append(item['amount'])
        
        self.assertEqual(a,[self.send_amount, self.send_amount])

if __name__ == '__main__':
    unittest.main()