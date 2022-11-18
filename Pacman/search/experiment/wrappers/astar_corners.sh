#!/usr/bin/env bash

if [ "$#" -ne 2 ]; then
	echo "Usage: `basename ${0}` <layout> <seed>" >&2
	exit -1
fi

_BASE_DIR="$(realpath $(dirname $0))"
_PROJECT_DIR=`realpath ${_BASE_DIR}/../..`
PACMAN="${_PROJECT_DIR}/pacman.py"


MAP=`echo $(basename $1) | cut -f1 -d.`
SEED=${2}

cd "${_PROJECT_DIR}" && \
	python ${PACMAN} -q -l ${MAP} \
		-p SearchAgent \
		-a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

