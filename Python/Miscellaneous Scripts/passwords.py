import string
import click
import random


@click.command()
@click.option("-l", "--length", default=16, help="Length of the password")
@click.option("-n", "--number", default=1, help="Number of passwords to generate")
@click.option("-s", "--special", is_flag=True, help="Do not include special characters")
@click.option("-x", "--xkcd", is_flag=True, help="Use XKCD style passwords")
def main(length, number, special, xkcd):
    """Generate a random password"""
    chars = string.ascii_letters + string.digits
    if not special:
        chars += string.punctuation

    if xkcd:
        if length == 16:
            length = 4
        words = open("/usr/share/dict/words").read().splitlines()
        for i in range(number):
            print("-".join(random.choice(words) for i in range(length)))
    else:
        for i in range(number):
            password = "".join(random.choice(chars) for i in range(length))
            click.echo(password)


if __name__ == "__main__":
    main()
