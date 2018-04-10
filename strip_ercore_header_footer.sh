#! /bin/bash

# Specifically for stripping header and footer from
# er-core and similarly templated files

if [ $# -lt 1 ]; then
  echo "Specify at least one argument"
  exit 1
fi
# Remove all lines that come before this match
sed '/You are here/,$!d' $1 | \
# Remove this line itself
sed '/You are here/d' |  \
# Remove all lines that come after this match
sed '/Copyright ©/,$d'
