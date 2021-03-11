import re
import click

def validate_command(value):
    if value.lower() == "exit":
        return value
    
    match = re.match(r"[FBLR]+", value)
    if match and value == match.group():
        return value
    raise click.BadParameter('Command is not valid. Valid inputs: F, B, L, R or exit.')