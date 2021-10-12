#!/bin/bash

count=10

while true
do
  for i in $(seq $count); do
    curl -s $1
    echo
  done
	
  echo "Going to sleep for a while"
  echo
	sleep 0.3
done