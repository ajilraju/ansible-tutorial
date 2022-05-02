# Overwritting ansible variable by CLI

```bash
ansible-playbook -e greetings=Hola playbooks.yaml
or
ansible-playbook --extra-vars greetings=Hola playbooks.yaml
```