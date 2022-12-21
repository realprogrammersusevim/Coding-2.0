#!/bin/bash
clear
sleep 2
string="Wake up Neo..."

read_string() {
    while IFS= read -n 1 char ; do
        sleep .2
        printf "%s" "$char"
    done <<< "$string"
    sleep 2
    clear
}

read_string
string="The Matrix has you..."
read_string
string="Follow the white rabbit."
read_string
printf "Knock, knock, Neo."
sleep 2
clear

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
    DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
    SOURCE=$(readlink "$SOURCE")
    [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
play "$DIR/knock_knock.mp3" &> /dev/null
