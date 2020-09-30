# Test control mining difficulty dynamically
# If solve a puzzle take long time I will setup a lower difficulty value
# When it's too easy then its value + 1

from blockchain import Blockchain

bc = Blockchain()

for i in range(0, 10):
    print(bc.add_block('foo'+str(i)).__dict__)