import click

@click.command()
@click.option(
    "-i", 
    "--ip", 
    type=str, 
    help="Single IP scan, e.g: -i 192.168.0.1"
)

@click.option(
    "-r", 
    "--range", 
    type=str, 
    help="Scan a network segment, e.g: -r 192.168.0.1/24"
)

@click.option(
    "-f", 
    "--file", 
    type=str, 
    help="Import IP list, e.g: -f targets.txt"
)
def main():
    click.echo("Hello")

if __name__ == '__main__':
    main()