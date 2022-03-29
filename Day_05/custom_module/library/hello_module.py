#!/usr/bin/python3

from ansible.module_utils.basic import *

def main():

	module = AnsibleModule(argument_spec={})
	response = {"hello": "world"}
	module.exit_json(changed=True, meta=response)


if __name__ == '__main__':
    main()