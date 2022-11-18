import json
from data.conf import db_path

def id_generator():
    with open(db_path,'r') as file:
        son=len(json.loads(file.read()))
    while True:
        son+=1
        yield son