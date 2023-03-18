from web3 import Web3

rpc_url = "http://68.183.37.122:31424"
target_contract_address = "0xA05520DFe55970cB69f34E8452a514B7f1625667"
setup_contract_address = "0xD6Ba146096eB45dF345582459f9dDea51414E97b"
caller = "0x22891371A9e9D3A43BFE7145382c321e5aea8cAe"
private_key = "0x42e431c782a0bf90d88364fc667801b4b83929f75960adfda34d785106b20260"

w3 = Web3(Web3.HTTPProvider(rpc_url))


nonce = w3.eth.get_transaction_count(caller)

# solc Setup.sol --abi
"""
======= Setup.sol:Setup =======
Contract JSON ABI
[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TARGET","outputs":[{"internalType":"contract ShootingArea","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

======= ShootingArea.sol:ShootingArea =======
Contract JSON ABI
[{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"firstShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"secondShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"third","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"thirdShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
"""
setup_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TARGET","outputs":[{"internalType":"contract ShootingArea","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
setup_contract = w3.eth.contract(address=setup_contract_address, abi=setup_abi)

# added fake function updateSensors
target_abi = '[{"inputs":[{"internalType":"uint256","name":"version","type":"uint256"}],"name":"updateSensors","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"firstShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"secondShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"third","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"thirdShot","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'
target_contract = w3.eth.contract(address=target_contract_address, abi=target_abi)


amount_eth = 0.0000000000000000000001
amount_wei = w3.to_wei(amount_eth, "ether")

# for fallback send ether to contract and invalid function signature
transaction = {
    "to": target_contract_address,
    "value": amount_wei,
    "gasPrice": 1,
    "gas": 2100000,
    "from": caller,
    "nonce": nonce,
    "data": target_contract.encodeABI(fn_name="updateSensors", args=[1]),
}

signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(receipt)

# no worky
# test = target_contract.fallback.call()


# for receive send ether to contract without calling specific function
test = target_contract.receive.transact()

# for third just call function
test = target_contract.functions.third().transact()

print(target_contract.functions.firstShot().call())
print(target_contract.functions.secondShot().call())
print(target_contract.functions.thirdShot().call())
