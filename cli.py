import click
from controller.math_controller import handle_operation


@click.command()
@click.argument("operation")
@click.argument("inputs", nargs=-1, type=int)
def main(operation, inputs):
    """
    Usage:
    python cli.py fibonacci 10
    python cli.py power 2 8
    python cli.py factorial 5
    """
    try:
        result = handle_operation(operation.lower(), list(inputs))
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {str(e)}")


if __name__ == "__main__":

    main()
