#!/bin/sh

usage() {
cat << END
Application Entrypoint.

Usage: ./init COMMAND-DOCKER-COMPOSE

Options:
  -e (test|local) : Current enviroment
                    (default: local)  
END
exit 0
}

while getopts 'he:' OPTION; do
  case "$OPTION" in
    e)
      enviroment="$OPTARG"
      ;;
    h)
      usage
      ;;
  esac
done
enviroment=${enviroment:-local}

case $enviroment in
'local'|'test')
    echo "Running Script in '$enviroment' enviroment"
    ;;
*)
    echo "'$enviroment' is a invalid <enviroment>. Please read de option to -e <enviroment>\n"
    usage
    ;;
esac

command=$(echo $@ | sed 's/-e\s\+\w\+\s*//')

echo "Docker command: '$command'"
docker compose --project-directory ./ -f ./docker/$enviroment/docker-compose.yml $command
