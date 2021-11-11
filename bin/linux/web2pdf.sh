#! /usr/bin/env bash

echo "Start ..."
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

if [[ -f "urls.txt" ]]
then
    wget  --continue --recursive --level=2 --accept pdf --input-file urls.txt
else
	read -p "Please input a url link of web page: " url
	echo $url
	wget  --continue --recursive --level=2 --accept pdf $url
fi


echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "Finished ."
