import os
from datetime import datetime


def check_exists(file_name):
    all_directory_files = os.listdir()
    for file in all_directory_files:
        if f"{file_name}.txt" == file:
            return "\n"
    return f"Notas do Dia {file_name} \n"

def take_note(note):
    file_name = datetime.now().date()
    note_sufix = check_exists(file_name)
    with open(f"{file_name}.txt", "a") as data:
        data.write(f"{note_sufix}{note}")
