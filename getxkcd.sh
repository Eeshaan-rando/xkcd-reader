#!/usr/bin/bash

read -n 1 -ep "Get random comic? [y|N]: " rand
if [ $rand = "y" ]; then
	comicUrl=$(curl -L https://c.xkcd.com/random/comic 2> /dev/null | grep -i "hotlinking" | grep -Eo 'https:[/|a-z|A-Z|\.|_]+?png' | head -n 1)
else
	comicUrl=$(curl -L https://xkcd.com 2> /dev/null | grep -i "hotlinking" | grep -Eo 'https:[/|a-z|A-Z|\.|_]+?png' | head -n 1)
fi

comicFile=$(basename "$comicUrl")
wget "$comicUrl" &> /dev/null
xdg-open "$comicFile"
