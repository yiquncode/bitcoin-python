import config
from chain_util import ChainUtil
from transaction import Transaction

class Wallet:
    def __init__(self):
        self.balance = config.wallet["INIT_BALANCE_FOR_TEST"]
        self.key_pair = ChainUtil.gen_key_pair()
        self.public_key = self.key_pair.get_verifying_key().to_string().hex()
    
    # In bitcoin terms, “spending” is signing a transaction that transfers value from a previous transaction 
    # over to a new owner identified by a bitcoin address.
    def sign(self, data):
        return self.key_pair.sign(data)

    def create_transaction(self, recipient, amount, transactionPool):
        if amount > self.balance:
            print(f'FAILD: {amount} exceeds current balance: {self.balance}')
            return False
        
        transaction = transactionPool.existing_transaction(self.public_key)

        if transaction != None:
            transaction.insert_output(self, recipient, amount)
        else:
            transaction = Transaction.new_transaction(self, recipient, amount)
            transactionPool.update_or_add(transaction)
        
        return transaction