#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    python fetch_word.py "$line"
    cd dataset
    mkdir "$line"
    cd ~/Downloads
    mv "*.wav" "~/Documents/School/Fall\ 2018/ML/Final_Project/dataset/$line"
    cd ~/Documents/School/Fall\ 2018/ML/Final_Project/dataset
    mkdir "$line-train" "$line-test" "$line-validate"
    cd "$line"

    for i in {1..60};
    do
        FIRST_FILE=$(ls | sort -n | head -1)
        mv "$FIRST_FILE" "../$line-train"
    done

    for i in {1..25};
    do
        FIRST_FILE=$(ls | sort -n | head -1)
        mv "$FIRST_FILE" "../$line-validate"
    done

    for i in {1..15};
    do
        FIRST_FILE=$(ls | sort -n | head -1)
        mv "$FIRST_FILE" "../$line-test"
    done

    cd ../

    mkdir "$line-train"
    mkdir "$line-test"
    mkdir "$line-validate"

    mv "$line-train" "$line/$line_train"
    mv "$line-train" "$line/$line_train"
    mv "$line-train" "$line/$line_train"

    rm -r "$line-train"
    rm -r "$line-test"
    rm -r "$line-validate"

done < "$1"