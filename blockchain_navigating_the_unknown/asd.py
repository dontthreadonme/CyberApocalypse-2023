from web3 import Web3

rpc_url = "http://139.59.173.68:30728"
target_contract_address = "0xAaD9c59235C1307bF4aFe2ce1618e8856bF64a48"
setup_contract_address = "0x9A3498C1DCA0ff273BD210a13173973752f3f667"
caller = "0x362857232ABfE48f180d86FD2d13AAeF5D307c53"
private_key = "0xf2cf61139122ea8b2f05b1e12eb1c5e0660472d03a2693b2fae4baf8f99656db"

w3 = Web3(Web3.HTTPProvider(rpc_url))


nonce = w3.eth.get_transaction_count(caller)

# solc Setup.sol --abi
"""
======= Setup.sol:Setup =======
Contract JSON ABI
[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TARGET","outputs":[{"internalType":"contract Unknown","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

======= Unknown.sol:Unknown =======
Contract JSON ABI
[{"inputs":[{"internalType":"uint256","name":"version","type":"uint256"}],"name":"updateSensors","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"updated","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]
"""
setup_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TARGET","outputs":[{"internalType":"contract Unknown","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
setup_contract = w3.eth.contract(address=setup_contract_address, abi=setup_abi)

target_abi = '[{"inputs":[{"internalType":"uint256","name":"version","type":"uint256"}],"name":"updateSensors","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"updated","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
target_contract = w3.eth.contract(address=target_contract_address, abi=target_abi)

test = target_contract.functions.updateSensors(10).transact()

print(test)
