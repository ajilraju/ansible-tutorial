Ansible Role: QuickHTTP
=========

Configure and launch a very SimpleHTTPServer powered by Python3.

Requirements
------------

None

Role Variables
--------------

```bash
web_user: web
web_group: web
www_dir: '/home/{{ web_user }}/www/'
www_files:
  - index.html
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: ec2
      roles:
         - { role: ajilraju.quickhttp, web_user: 42 }

License
-------

GNU GPLv3

Author Information
------------------

This role was created in 2021 by [Ajil Raju](https://ajilraju.github.io).
