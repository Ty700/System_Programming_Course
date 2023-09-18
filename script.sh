#!/bin/bash

# Is line 4 even needed? Doing it so I don't make dirs in random locs by accident
cd ~/Desktop 

mkdir -p ~/Desktop/big-directory/small-directory && touch $_/file-1.txt

cd big-directory/small-directory

echo "Tyler Scotti" > file-1.txt

seq 1 1 20 >> file-1.txt

cat file-1.txt

wc -w < file-1.txt >> file-2.txt

cat file-1.txt && cat file-2.txt

cp file-1.txt ../file-1.txt

cd ..

#Never will understand why git and linux use mv to rename. 
#Where is the petition to change -m and mv to -r & rename
mv file-1.txt file-3.txt

rm -r small-directory

# echo "ls -l"
ls -l

# echo "ls -a:"
ls -a

cd ..
rm -r big-directory