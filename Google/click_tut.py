#! /usr/bin/env python

#↑↑↑↑  SHEBANG command , usedwhen we want to execute a file directly without using python in CLI.


import click


@click.command()
@click.option('--count',default =1, help = "Number of Greetings")
@click.option('--name', prompt = "your name", help = "the person to greet")


def hello(count, name):

    for x in range(count):
        click.echo(f"Hello {name}")



if __name__ == "__main__":
    hello()