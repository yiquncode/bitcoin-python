import config
from chain_util import ChainUtil

class Wallet:
    def __init__(self):
        self.balance = config.wallet["INIT_BALANCE_FOR_TEST"]
        self.key_pair = ChainUtil.gen_key_pair()
        self.public_key = self.key_pair.get_verifying_key().to_string().hex()
    
    # In bitcoin terms, “spending” is signing a transaction that transfers value from a previous transaction 
    # over to a new owner identified by a bitcoin address.
    def sign(self, data):
        return self.key_pair.sign(data)