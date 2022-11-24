#!/bin/sh

while getopts 'e:' OPTION; do
  case "$OPTION" in
    e)
      enviroment="$OPTARG"
      echo "The value provided is $OPTARG"
      ;;
  esac
done
enviroment=${enviroment:-local}

case $enviroment in
'local'|'test')
    echo "Running Script in $enviroment enviroment"
    ;;
*)
    echo "'$enviroment' is a invalid enviroment. Only 'local' and 'test' are valids"
    exit 1
    ;;
esac

command=$(echo $@ | sed 's/-e\s\+\w\+\s*//')

echo "Docker command: '$command'"
docker compose -f ./docker/$enviroment/docker-compose.yml $command
