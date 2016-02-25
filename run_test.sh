#! /bin/bash
ret=0

dir="$(dirname "$BASH_SOURCE")"

docker-compose -f ${dir}/docker/test-compose.yml run --rm babylonlexer-py3 coverase

docker-compose -f ${dir}/docker/test-compose.yml run --rm babylonlexer-py3 test
ret=$(($ret + $?))

docker-compose -f ${dir}/docker/test-compose.yml run --rm babylonlexer-py2 test
ret=$(($ret + $?))

docker-compose -f ${dir}/docker/test-compose.yml run --rm babylonlexer-node10 test
ret=$(($ret + $?))

if [ "$ret" -gt 0 ]; then
    echo $(tput setaf 1)Tests failed...$(tput sgr0)
    exit 1
fi;

echo $(tput setaf 2)Success...$(tput sgr0)

docker-compose -f ${dir}/docker/test-compose.yml run --rm babylonlexer-py3 covreport
