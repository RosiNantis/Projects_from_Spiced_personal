import argparse

parser = argparse.ArgumentParser()
# add arguments
parser.add_argument("echo", help="echo the string you use here")
# add argument with type
parser.add_argument("square", help="display a square of a given number", type=int)
# add optional arguments
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()

print(args.echo)
print(args.square**2)
if args.verbosity:
    print("verbosity turned on")
