#!/bin/bash

# This is a script to query my rasperry pi about the bitcoin blockchain info from the fullnode that it's running.
# TODO Find out how to check if the rasperry pi is reachable before attempting to run commands.
date=$(date +%Y%m%d)
echo $date

ssh rpi "bitcoin-cli getblockchaininfo"
sleep 2
echo "Queried blockchain info"
echo $blockchaininfooutput
