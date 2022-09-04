import click
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("Imports finished, about to define the command options with click.")


@click.command()
@click.argument(
    "grade",
    type=float,
    required=True,
    nargs=1,
)
@click.option(
    "-c",
    "--curve",
    is_flag=True,
    help="Show whether your grade is above or below average.",
)
def main(grade: float, curve):
    """This script will tell you your letter grade based on your percentage grade."""
    logging.debug("Command options defined, about to run the main function.")
    logging.debug(f"The grade is: {grade}")

    if 97.0 <= grade <= 100.0:
        print("A+")
    elif 93.0 <= grade < 97.0:
        print("A")
    elif 90.0 <= grade < 93.0:
        print("A-")
    elif 87.0 <= grade < 90.0:
        print("B+")
    elif 83.0 <= grade < 87.0:
        print("B")
    elif 80.0 <= grade < 83.0:
        print("B-")
    elif 77.0 <= grade < 80.0:
        print("C+")
    elif 73.0 <= grade < 77.0:
        print("C")
    elif 70.0 <= grade < 73.0:
        print("C-")
    elif 67.0 <= grade < 70.0:
        print("D+")
    elif 63.0 <= grade < 67.0:
        print("D")
    elif 60.0 <= grade < 63.0:
        print("D-")
    elif 0.0 <= grade < 60.0:
        print("F")

    if curve:
        logging.debug("Curve option is set, about to calculate the curve grade.")
        # Show where in the class your grade is
        # Assume the class average is 80.0
        if grade >= 80.0:
            print("You are above average.")
        elif grade < 80.0:
            print("You are below average.")

    logging.debug("Main function finished, about to exit.")


if __name__ == "__main__":
    main()
