from os import environ
from jinja2 import FileSystemLoader, Template, Environment

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

bio_data = {
    "first_name": fname,
    "last_name": lname,
    "age": age
}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('fill-in-the-blank')

print(template.render(bio_data))

