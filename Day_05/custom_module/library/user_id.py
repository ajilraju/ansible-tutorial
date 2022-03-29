#!/usr/bin/python3

from ansible.module_utils.basic import *

import pwd
import os

def main():

    module_args = dict(
        name = dict(type='str', required=True)
    )

    result = dict(
        changed=True,
        id='',    
    )

    module = AnsibleModule(argument_spec=module_args)


    try:
        if module.params['name'] == None:
            user = pwd.getpwnam(os.getlogin())
            result['id'] = {
                'user': user.pw_name,
                'uid' : user.pw_uid,
                'gid' : user.pw_gid,
            }          
        else:
            user = pwd.getpwnam(module.params['name'])
            result['id'] = {
                'user': user.pw_name,
                'uid' : user.pw_uid,
                'gid' : user.pw_gid,
            }

    except KeyError:
        result = dict(
            failed=True,
            msg=f"failed to find such user called {module.params['name']}",
        )


    module.exit_json(**result)


if __name__ == '__main__':
    main()