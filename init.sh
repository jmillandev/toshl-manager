#!/bin/sh

usage() {
cat << EOF
Application Entrypoint.

Usage: ./init COMMAND-DOCKER-COMPOSE

Options:
  -e <enviroment> (test|local) : Current enviroment
                                  (default: local)  
EOF
}

while getopts 'he:' OPTION; do
  case "$OPTION" in
    e)
      enviroment="$OPTARG"
      echo "The value provided is $OPTARG"
      ;;
    h)
      usage
      exit 0
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
docker compose --project-directory ./ -f ./docker/$enviroment/docker-compose.yml $command
