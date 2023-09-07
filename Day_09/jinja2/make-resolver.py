import sys
from os import environ
from jinja2 import FileSystemLoader, Template, Environment

# Global data
nameservers = [
    "ns1.example.com",
    "ns2.example.com",
    "ns3.example.com",
]
search_domain = 'example.com'
options = 'options edns0 trust-ad'

if sys.argv[1] == 'resolv.conf.j2':
    # subjective data
    nameservers = "ns1.example.com"
    data = {
        'namesrv': nameservers,
        'domain': search_domain,
        'opts': options
    }
else:
    data = {
        'namesrv': nameservers,
        'domain': search_domain,
        'opts': options
    }

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template(sys.argv[1])

print(template.render(data))