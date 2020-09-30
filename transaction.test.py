import unittest
from wallet import Wallet
from transaction import Transaction

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        self.amount = 50
        self.recipient = 'r3co09ow99'
        self.transaction = Transaction.new_transaction(self.wallet, self.recipient, self.amount)
    
    def test_subtract_from_balance(self):
        for output in self.transaction.outputs: 
            if output['address'] == self.wallet.public_key:
                self.assertEqual(output['amount'], self.wallet.balance - self.amount)
    
    def test_add_amount_to_recipient(self):
        for output in self.transaction.outputs: 
            if output['address'] == self.recipient:
                self.assertEqual(output['amount'], self.amount)        

    def test_amount_more_than_balance(self):
        transaction = Transaction.new_transaction(self.wallet, self.recipient, 700)
        self.assertFalse(transaction)
    
    def test_input_equal_balance(self):
        self.assertEqual(self.transaction.input['amount'], self.wallet.balance)
        #print(self.transaction.__dict__)
    
    def test_verify_real_transation(self):
        #print(self.transaction.__dict__)
        self.assertTrue(Transaction.verify_transaction(self.transaction))
    
    def test_verify_malicious_transation(self):
        self.transaction.outputs[0]['amount'] = 66
        self.assertFalse(Transaction.verify_transaction(self.transaction))


if __name__ == '__main__':
    unittest.main()