#! /usr/bin/env bash

display_usage() { 
	echo "This script grab url and filter pdf links."
	echo -e "\nUsage: \$0 url \n"
}


# if less than two arguments supplied, display usage 
if [  $# -lt 1 ]
then
  display_usage
  exit 1
fi
 
# check whether user had supplied -h or --help . If yes display usage 
if [[ ( $# == "--help") ||  $# == "-h" ]]
then
  display_usage
  exit 0
fi



url=$1
curl -s $url|cut -d "\"" -f 2|grep -i .pdf


