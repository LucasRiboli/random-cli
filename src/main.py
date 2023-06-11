from typing import Optional

import typer
import function_commands.commands_note as notes

app = typer.Typer()

@app.command()
def take_note(note: str, note_name: Optional[str] = None):
    if note_name:
        notes.take_note(note, note_name)
    else:
        notes.take_note(note)
    typer.echo("Nota salva com sucesso")

@app.command()
def see_note(date_file: Optional[str] = None):
    if date_file:
        typer.echo(notes.read_note(date_file))
    else:
        typer.echo(notes.read_note())

if __name__ == "__main__":
    app()