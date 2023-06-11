from typing import Optional

import typer
import src.function_commands.commands_note as notes

app = typer.Typer()

@app.command()
def take_note(note):
    notes.take_note(note)
    typer.echo("Nota salva com sucesso")
    

if __name__ == "__main__":
    app()