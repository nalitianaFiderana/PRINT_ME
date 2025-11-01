import typer

app = typer.Typer(help="this CLI will print your portfolio in another way")

@app.command()
def hello(name: str):
    """
        Simple command to greet a user by name.
    """
    typer.echo(f"Hello, {name}!")