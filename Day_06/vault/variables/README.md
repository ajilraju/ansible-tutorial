# Encrypting individual variables with Ansible Vault
You can encrypt single values inside a YAML file using the ansible-vault encrypt_string command. 

```bash
ansible-vault encrypt_string <password_source> '<string_to_encrypt>' --name '<string_name_of_variable>'
```
### Example
```bash
ansible-vault encrypt_string <--vault-password-file a_password_file> 'password' --name 'user_passwd'

```
