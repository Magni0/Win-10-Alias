from os import chdir, path
from json import loads, dumps
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class Alias:

    def __init__(self, args):
        self.args = args
    
    def use_alias(self):
        pass

    def create_alias(self):
        # print(self.args)
        path = self.args.path
        alias = self.args.alias

        # loads json content
        with open("alias.json", "r") as file:
            try:
                aliases = loads(file.read())
            except:
                aliases = {}
        
        aliases[f"{alias}"] = f"{path}"

        with open("alias.json", "w") as file:
            file.write(dumps(aliases))

    def remove_alias(self):
        alias = self.args.alias

        with open("alias.json", "r") as file:
            try:
                aliases = loads(file.read())
            except:
                raise Exception("No stored aliases")
        
        del aliases[f"{alias}"]

        with open("alias.json", "w") as file:
            file.write(dumps(aliases))

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
parser.add_argument("-p", "--path", type=str, help="argument is absolute path")
parser.add_argument("-a", "--alias", type=str, help="argument is the name of alias")
parser.add_argument("-r", "--remove", action="store_true", help="")

args = parser.parse_args()
alias = Alias(args)
