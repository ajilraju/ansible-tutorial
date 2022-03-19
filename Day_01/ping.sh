#!/bin/bash

python3_bin=$(type python3 | awk '{ print $3 }')

cat << EOL
SUCCESS => {
    "demo_ansible_facts": {
        "discovered_interpreter_python": $python3_bin
    },
    "changed": false,
    "ping": "pong"
}
EOL