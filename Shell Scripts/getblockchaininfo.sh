#!/bin/bash

# This is a script to query my Rasperry Pi about the Bitcoin blockchain info from the fullnode that it's running.
# TODO: Find out how to check if the rasperry pi is reachable before attempting to run commands.

ping -c1 192.168.0.43 > /dev/null
if [ $? -eq 0 ]
then
    echo "What info would you like to get from the Raspberry Pi?"
    read BITCOIN_USER_COMMAND
    echo "About to send the ssh command to the RPi"
    ssh rpi "bitcoin-cli $BITCOIN_USER_COMMAND"
fi

echo "Completed the script"

exit 0