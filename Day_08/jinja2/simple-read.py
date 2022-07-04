from os import environ
from jinja2 import FileSystemLoader, Template, Environment

bio_data = {
    "first_name": "Tony",
    "last_name": "Stark"
}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('fill-in-the-blank')

print(template.render(bio_data))