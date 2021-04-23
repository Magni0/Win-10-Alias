from os import chdir
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class Alias:

    def __init__(self, args):
        self.args = args

    def create_alias(self):
        pass

    def remove_alias(self):
        pass

    def use_alias(self):
        pass

parser = ArgumentParser(
    formatter_class=RawDescriptionHelpFormatter,
    description="""
    """
)

# add arguments

args = parser.parse_args()
alias = Alias(args)
