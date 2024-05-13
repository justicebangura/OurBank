// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Wallet {
    // Event for Ethers deposited
    event Deposit(address indexed sender, uint amount);

    // Event for Ethers sent
    event Sent(address from, address to, uint amount);

    // Function to deposit Ether into the contract
    function deposit() public payable {
        emit Deposit(msg.sender, msg.value);
    }

    // Function to send Ether from the contract to another address
    function send(address payable to, uint amount) public {
        require(address(this).balance >= amount, "Insufficient balance in contract");
        to.transfer(amount);
        emit Sent(address(this), to, amount);
    }

    // Function to get the contract's balance
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Fallback function to receive Ether
    function () external payable {}
}