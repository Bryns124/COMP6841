#!/bin/bash

counter=1

while true; do
  input=$(python2 -c "print('A' * $counter)")
  echo "$input" | "$1"
  ret_value=$?
  if [ $ret_value -eq 139 ]; then
    echo "Segmentation fault with input length: $counter"
    exit 1
  fi
  ((counter++))
done