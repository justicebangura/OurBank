// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoWallet {
    address payable public accountOwner;
    mapping(address => uint256) private balances;

    constructor() {
        accountOwner = payable(msg.sender);
    }

    modifier onlyOwner() {
        require(msg.sender == accountOwner, "Only account owner can call this function");
        _;
    }

    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance in the contract");
        accountOwner.transfer(amount);
    }

    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }

    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    receive() external payable {}
}