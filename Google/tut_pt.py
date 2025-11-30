#! /usr/bin/env python


import click

@click.command()
@click.argument('src', nargs=1)
@click.argument('dsts', nargs=-1)

def copy(src:str, dsts:tuple[str, ...]):

    for destination in dsts:
        click.echo(f"copy {src} to folder {destination}")
