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
play knock_knock.mp3 &> /dev/null
