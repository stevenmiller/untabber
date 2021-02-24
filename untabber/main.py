import sys, argparse

parser = argparse.ArgumentParser(prog='untabber', 
                                usage='%(prog)s [file] [options]',
                                description='Replaces all tabs in the specified file with 4 spaces.')

parser.add_argument("-i", "--input", help="Path to input file", required=True)
parser.add_argument("-o", "--output", default="output.txt", help="Path to output file")
args = parser.parse_args()

with open(args.input) as my_file:

    fout = open(args.output, "wt")

    for line in my_file:
        fout.write(line.replace('\t', '    '))

