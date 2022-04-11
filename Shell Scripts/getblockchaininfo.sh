#!/bin/bash

date=$(date +%Y%m%d)
echo $date

ssh rpi "bitcoin-cli getblockchaininfo"
sleep 2
echo "Queried blockchain info"
echo $blockchaininfooutput
