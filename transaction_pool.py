import json
import base64

class TransactionPool:

    def __init__(self):
        self.transactions = []

    def update_or_add(self, transaction):
        old_transaction = None

        for count, item in enumerate(self.transactions):
            if item.id == transaction.id:
                old_transaction = count
        
        if old_transaction != None:
            self.transactions[old_transaction] = transaction
        else:
            self.transactions.append(transaction)
    
    def existing_transaction(self, address):
        for t in self.transactions:
            if t.input['address'] == address:
                return t
            else:
                return None
    
    def to_json(self):
        for ob in self.transactions:
            encoded = base64.b64encode(ob.input['signature'])
            ob.input['signature'] = encoded.decode('ascii')
            # decoded = base64.b64decode(ob.input['signature'])
            return json.dumps(ob.__dict__)
                 