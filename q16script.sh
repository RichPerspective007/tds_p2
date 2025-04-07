#!/bin/bash

# making the folder where the extracted files will be kept
mkdir tq16 >/dev/null 2>&1
mkdir tq16/extractedfiles >/dev/null 2>&1

# unzip the downloaded zip files into the folder named extractedfiles using the unzip command. Refer to man unzip for usage guide.
unzip $1 -d tq16/extractedfiles/ >/dev/null 2>&1

# the folder names ym zch... 24amoj are the folders that were present in the zip file. The names for those may be different in your zip file. Check and change the script accordingly
for file in ./tq16/extractedfiles/*; do
	mv $file/* tq16/extractedfiles >/dev/null 2>&1
done

# creating the empty folder
rm -r empty >/dev/null 2>&1
mkdir empty >/dev/null 2>&1

# moving all files from extractedfiles to empty folder.
mv tq16/extractedfiles/* empty >/dev/null 2>&1

# renaming all files in the empty folder
while read -r line; do
	newfn=""
	ch=$(echo $line | cut -d '.' -f1 | grep -o .)
	while read -r character; do
		if [[ $character =~ [[:digit:]] ]]; then
			character=$(($character+1))
			if [ $character -gt 9 ]; then
				character=0
			fi	
		fi
		newfn+=$character
	done <<< $ch
	mv ./empty/$line ./empty/$newfn.$(echo $line | cut -d '.' -f2) >/dev/null 2>&1
done <<< $(ls ./empty | tr -s ' ')

cd empty
grep . * | LC_ALL=C sort | sha256sum
cd ..
rm -r empty >/dev/null 2>&1
rm -r tq16 >/dev/null 2>&1
# script end
