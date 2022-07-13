clear
string="Wake up Neo..."

read_string() {
    while IFS= read -n 1 char ; do
        sleep .2
        printf "$char"
    done <<< "$string"
    sleep 2
    echo \n
    clear
}

read_string
string="The Matrix has you..."
read_string
string="Follow the white rabbit."
read_string
printf "Knock, knock, Neo."
sleep 2
echo \n
clear
play Knock,\ knock.mp3 &> /dev/null