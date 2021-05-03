from os import chdir, path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class Alias:

    def __init__(self, args):
        self.args = args
    
    def run(self):
        pass

    def create_alias(self):
        pass

    def remove_alias(self):
        pass

parser = ArgumentParser(
    formatter_class=RawDescriptionHelpFormatter,
    description="""
    Allows aliases for specified paths the be created
    speeding up cmd navigation.
    """
)

# check if alias file exists if not creates file
if path.isfile("alias.json"):
    pass
else:
    with open("alias.json", "x"): pass

parser.add_argument("-c", "--create", action="store_true", help="used to create a new alias (-p and -a flags must follow)")
parser.add_argument("-p", "--path", type=str, help="argument is the absolute path that you wish to make a new alias")
parser.add_argument("-a", "--alias", type=str, help="argument is the name of the new alias")

args = parser.parse_args()
alias = Alias(args)
