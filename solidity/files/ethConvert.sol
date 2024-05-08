// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract EthToUsdConverter {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Sepolia
     * Aggregator: ETH/USD
     * Address: 0x694AA1769357215DE4FAC081bf1f309aDC325306
     */
    constructor() {
        priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
    }

    /**
     * Returns the latest price of 1 ETH in USD
     */
    function getEthPrice() public view returns (uint256) {
        (
            /*uint80 roundID*/,
            int256 price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        return uint256(price); // Adjust the price to a more readable format, as it's usually provided with extra decimals
    }

    function convertEthToUsd(uint256 ethQuantity) public view returns (uint256) {
        uint256 ethValue = getEthPrice();
        uint256 ethToUsd = (ethValue * ethQuantity);
        return ethToUsd;
    }
}

/*
Need Sepolia network and faucet to get some Ethereum.
Needed Price feed contract address for Sepolia in order to make it work as well.
*/


