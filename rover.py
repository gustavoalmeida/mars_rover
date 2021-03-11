import click

from cli.display import welcome, instructions, initial_position, moving
from cli.rover import Rover

current_position = (4, 2, "EAST")

@click.group()
def cli():
    pass

@cli.command()
def ignite():
    rover = Rover(current_position)
    welcome()
    instructions()
    rover = initial_position(rover)
    moving(rover)
    
if __name__ == '__main__':
    cli()