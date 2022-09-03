import click
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Imports finished, about to define the command options with click.")


@click.command()
@click.option(
    "-g", "--grade", is_flag=False, help="The percentage grade to be converted."
)
@click.option(
    "-c", "--curve", is_flag=True, help="Show where your grade would be on a curve."
)
def main(grade: float, curve):
    logging.debug("Command options defined, about to run the main function.")

    grade = float(grade)
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

    if curve:
        print("Your grade would be a B on a curve.")

    logging.debug(f"The grade is: {grade}")
    logging.debug("Main function finished, about to exit.")


if __name__ == "__main__":
    main()
