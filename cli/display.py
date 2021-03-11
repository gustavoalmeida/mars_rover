import sys
import time

import click

from cli.validators import validate_command

def welcome():
    click.echo("")
    click.echo("================================")
    click.echo("Welcome to Mars Rover Controller")
    click.echo("================================")

def instructions():
    click.echo("")
    click.echo("Instructions:")
    click.echo("Start inputing the Mars Rover initial position or let it use its self localization system.")
    click.echo("")

def initial_position(rover):
    click.echo("")
    click.echo(f"Current position: {rover.position}")
    click.echo("")
    use_current = click.confirm("Use this current position?")
    if not use_current:
        rover = input_new_position(rover)
    return rover
    
def input_new_position(rover):
    confirm = False
    while not confirm:
        click.echo("")
        click.echo("Please, informe the start position?")
        x = click.prompt("x: ", type=int)
        y = click.prompt("y: ", type=int)
        direction = click.prompt("direction: ", type=click.Choice(["NORTH", "EAST", "SOUTH", "WEST"], case_sensitive=True))
        confirm = click.confirm(f"Confirm the start position: {(x, y, direction)}")
    rover.position = (x, y, direction)
    return rover

def moving(rover):
    click.echo("")
    click.echo("Motor started.")
    click.echo("")
    while True:
        command = click.prompt("Input the direction command or type exit to turn the rover off", value_proc=validate_command)
        if command != "exit":
            rover.goto(command)
            click.echo(f"Current position: {rover.position}")
        else:
            turn_off(rover)

def turn_off(rover):
    click.echo("")
    click.echo("Turning the Rover off.")
    click.echo("See you soon.")
    click.echo("")
    sys.exit(0)


        