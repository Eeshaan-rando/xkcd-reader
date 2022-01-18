#!/usr/bin/bash

comicUrl=$(curl https://xkcd.com 2> /dev/null | grep -i "hotlinking" | grep -Eo 'https:[/|a-z|A-Z|\.|_]+?png' | head -n 1)
comicFile=$(basename "$comicUrl")
wget "$comicUrl" &> /dev/null
xdg-open "$comicFile"
