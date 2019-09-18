import argparse

parser = argparse.ArgumentParser()

#these are optional arguments
parser.add_argument('-d', '--dev', help='provide the private developer key file')
parser.add_argument('-p', '--pub', help='provide the public key file')

#this is a required command line argument
parser.add_argument('time', help='provide the timestamp')
args = parser.parse_args()

print(args)
print(args.dev)
print(args.pub)
print(args.time)
