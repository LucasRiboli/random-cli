import os
from datetime import datetime
import requests
import json

def __check_exists(file_name):
    all_directory_files = os.listdir()
    for file in all_directory_files:
        if f"{file_name}.txt" == file:
            return "\n"
    return f"- Notas do Dia {file_name} \n"

def __grammatic_help(note):
    headers = {
                'content-type': '',
                'X-RapidAPI-Key': '',
                'X-RapidAPI-Host': ''
            }
    payload = {
        "text" : note,
        "language": "pt-BR"
    }
    try:
        response = requests.post(url="https://dnaber-languagetool.p.rapidapi.com/v2/check", headers=headers, data=json.dumps(payload))
        print(response)
        return response
    except requests.RequestException as e:
        print(e)
        return note  
    
def take_note(note: str, note_name = datetime.now().date()):
    note_sufix = __check_exists(note_name)
    note = __grammatic_help(note)
    with open(f"{note_name}.txt", "a") as data:
        data.write(f"{note_sufix}{note}")

def read_note(name_file = datetime.now().date()):
    with open(f"{name_file}.txt", "r") as data:
        return data.read()