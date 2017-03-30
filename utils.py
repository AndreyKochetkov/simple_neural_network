import argparse


def create_parser():
    """ Create parser for command-line arguments

    Returns:
        instance of argparse.ArgumentParser . It has all command-line arguments: host, port, db, getErrors.
        If they haven't been sent, they will be set by default values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr",
                        type=float,
                        default=None,
                        help="get error messages - send \'yes\' ")

    return parser


