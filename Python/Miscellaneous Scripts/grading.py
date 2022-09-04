import click
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("Imports finished, about to define the command options with click.")


@click.command()
@click.argument("grade", type=float)
@click.option(
    "-c", "--curve", is_flag=True, help="Show where your grade would be on a curve."
)
def main(grade: float, curve):
    logging.debug("Command options defined, about to run the main function.")

    # Convert the match case statemet to an if-elif statement
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
        pass

    logging.debug(f"The grade is: {grade}")
    logging.debug("Main function finished, about to exit.")


if __name__ == "__main__":
    main()
