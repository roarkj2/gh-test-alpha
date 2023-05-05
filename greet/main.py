from importlib import metadata
import click

def showVersion():
    version = metadata.version("gh-test-alpha")
    click.echo(f"Version: {version}")

@click.command(no_args_is_help=True,help="Automated greeter")
@click.option("--name","-n",help="Name of person to greet")
@click.option("--version",is_flag=True,help="show version of package")
def cli(name,version):
    if (version):
        showVersion()
    else:
        print(f"Hello world, to my bestie {name}")