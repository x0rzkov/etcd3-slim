#!/usr/bin/env bash

set -x

SCRIPT_DIR="$(dirname $0)"
source ${SCRIPT_DIR}/common.sh

for i in $(seq 1 ${CLUSTER_SIZE}); do
    kill $(cat ${WORKSPACE_DIR}/etcd${i}.pid)
    rm ${WORKSPACE_DIR}/etcd${i}.pid
done
