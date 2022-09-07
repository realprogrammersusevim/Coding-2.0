import string
import click
import random


@click.command()
@click.option("-l", "--length", default=16, help="Length of the password")
@click.option("-n", "--number", default=1, help="Number of passwords to generate")
def main(length, number):
    """Generate a random password"""
    chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(number):
        password = "".join(random.choice(chars) for i in range(length))
        click.echo(password)


if __name__ == "__main__":
    main()
