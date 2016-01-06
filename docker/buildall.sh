#! /bin/bash

set -e

dir="$(dirname "$BASH_SOURCE")"

for name in babylonlexer-py2 babylonlexer-py3 babylonlexer-node10
do
    out="rbann/${name}"
    outlen=${#out}
    line=$(head -c ${outlen} < /dev/zero | tr '\0' '-')
    echo $(tput setaf 3)${out}$(tput sgr0)
    echo $(tput setaf 2)${line}$(tput sgr0)
    docker build -t "rbann/$name" ${dir}/$name
done
