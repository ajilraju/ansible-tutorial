from os import environ
from jinja2 import FileSystemLoader, Template, Environment

fruits_indicate = ['f1', 'f2', 'f3']
fruits = ['apple', 'orange', 'kiwi']
fruits_list = dict(zip(fruits_indicate, fruits))

data = {
    "heading": "Jinja2 template demo",
    "fruits": fruits_list,
    "fruits2": fruits
}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('index.html.j2')

print(template.render(data))