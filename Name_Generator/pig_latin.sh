#!/usr/bin/env bash

while true; do
    read -p "Type a word: " w

    if [[ -z $w ]]; then
        echo "No Input"
        exit
    fi

    if ! [[ $w =~ ^[a-zA-Z]+$ ]]; then
        echo "Only letters :)"
        continue
    fi

    f=${w:0:1}
    r=${w:1}

    if [[ $f =~ [aeiouAEIOU] ]]; then
        echo pig_latin="$w"way
    else
        echo pig_latin="$r$f"ay
    fi

    read -p "Again? (y/n) " ans
    if [[ $ans != "y" ]]; then
        break
    fi
done