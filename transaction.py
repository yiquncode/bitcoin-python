import time
from chain_util import ChainUtil

class Transaction:
    def __init__(self):
        self.id = ChainUtil.id()
        self.input = {}
        self.outputs = []
    
    def insert_output(self, sender_wallet, recipient, amount):
        for output in self.outputs:
            if output['address'] == sender_wallet.public_key:
                sender_output = output
        
        if amount > sender_output['amount']:
            print(f'insert output faild: {amount} exceeds balance')
            return False
        
        sender_output['amount'] = sender_output['amount'] - amount
        self.outputs.append({'amount': amount, 'address': recipient})
        Transaction.sign_transaction(self, sender_wallet)

        return self

    @staticmethod
    def new_transaction(sender_wallet, recipient, amount):
        transaction = Transaction()

        if amount > sender_wallet.balance:
            #print(f'Faild: You send {amount} but you only have {sender_wallet.balance}')
            return False
        
        transaction.outputs.append({'amount': sender_wallet.balance - amount, 'address': sender_wallet.public_key})
        transaction.outputs.append({'amount': amount, 'address': recipient})

        Transaction.sign_transaction(transaction, sender_wallet)

        return transaction
    
    @staticmethod
    def sign_transaction(transaction, sender_wallet):
        outputs_hash = ChainUtil.to_hash(str(transaction.outputs))

        transaction.input = {
            'timestamp': time.time(),
            'amount': sender_wallet.balance,
            'address': sender_wallet.public_key,
            'signature': sender_wallet.sign(outputs_hash)
        }
    
    @staticmethod
    def verify_transaction(transaction):
        return ChainUtil.verify_sig(transaction.input['address'],
        transaction.input['signature'],
        ChainUtil.to_hash(str(transaction.outputs)))