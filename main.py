import sys, argparse

parser = argparse.ArgumentParser(prog='untabber', 
                                usage='%(prog)s [file] [options]',
                                description='Removes tabs from your files')

parser.add_argument("-i", "--input", help="Path to input file", required=True)
parser.add_argument("-o", "--output", default="output.txt", help="Path to output file")
args = parser.parse_args()


# with open(sys.argv[1], 'r') as my_file:
with open(args.input) as my_file:

    fout = open(args.output, "wt")
#    filename = my_file.name + "_out.txt"
#    fout = open(filename, "wt")

    for line in my_file:
        fout.write(line.replace('\t', '    '))
        print("Found tab on" + line.count)
