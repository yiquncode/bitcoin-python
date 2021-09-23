# Bitcoin Python

I am very interested in Bitcoin both economics and technical, but it's very hard for me learning it from only read whitepaper, so I try to rewrite its core in Python, My purpose is to understand the principles of Bitcoin.

我对比特币的经济学和技术都很感兴趣，但是我完全无法通过只阅读白皮书掌握其精髓，所以我尝试用 Python 重写其核心，我的目的是理解比特币的原理。

## Planning and tracking work

According to the white paper, the project can be disassemble into eight main parts, the ticked task means I've been completed it.

根据白皮书，可以将实现BTC可以分解为八个主要部分，打勾的任务表示我已经完成了代码。

**Block**

- [x] Create the block
- [x] Genesis Block
- [x] Mine Blocks
- [x] Unit Test

**Chain**

- [x] Design and build the Blockchain class
- [x] Chain Validation
- [x] Replace the Chain
- [x] Unit Test

**API**

- [x] Get Blocks
- [x] Mine Blocks
- [x] Unit Test

**Blockchain Network**

- [x] Build Peer to Peer Server
- [x] Connect to Blockchain Peers
- [x] Handle Messages from Peers
- [x] Synchronize the Blockchain across Peers
- [x] Unit Test

**Proof of Work**

- [x] Proof of Work and the Nonce
- [x] Dynamic Block Difficulty
- [x] Unit Test

**Wallets and Transactions on the Blockchain**

- [x] Create Wallet
- [x] Create a Transaction
- [x] Sign a Transaction
- [x] Verify Transactions
- [x] Unit Test

**Collect Transactions in a Pool**

- [x] Add Transaction
- [x] Create Transactions with the Wallet
- [x] Add the Transaction Pool to the Peer to peer Server
- [x] Handle Transaction Messages in the Peer to peer Server
- [x] Unit Test

**Mine Transactions in a Block**

- [ ] Miner Class
- [ ] Reward Transactions
- [ ] Reward Valid, and Clear Transactions
- [ ] Broadcast Clear Transactions
- [ ] Mine Transactions Endpoint
- [ ] Unit Test