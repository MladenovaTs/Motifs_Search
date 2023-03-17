#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

#### This is a short Bash script that invokes a Python script, which is used to classify a nucleotide sequence as either DNA or RNA. The script uses the argparse module to define and handle command-line arguments ####

## The script expects two arguments:
## "-s" or "--seq" argument: This is the input sequence to be classified. It is a required argument, and the script will exit with an error if it is not provided.
## "-m" or "--motif" argument: This is an optional argument that specifies a motif to search for in the input sequence. ##
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

## The script first checks if any arguments were passed to it. If no arguments were passed, it prints the usage message and exits with an error. ##
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

## Then it parses the arguments passed to it using the ArgumentParser class from the argparse module. ##
args = parser.parse_args()

## The script then converts the input sequence to uppercase, in order to standardize it and make it easier to work with. ##
args.seq = args.seq.upper()                 # Note we just added this line

## It uses the re module to search the input sequence for a pattern that matches either DNA or RNA. It does this by searching for the presence of either 'T' or 'U', which are specific to DNA and RNA, respectively. If it finds 'T', it declares the sequence as DNA; if it finds 'U', it declares the sequence as RNA. If it finds neither 'T' nor 'U', it declares that the sequence could be either DNA or RNA. If the sequence contains any characters that are not A, C, G, T, or U, it declares the sequence as neither DNA nor RNA. ##
if re.search('^[ACGTU]*$', args.seq):
    if 'T' in args.seq and 'U' not in args.seq:
        print(f'The sequence "{args.seq}" is DNA')
    elif 'U' in args.seq and 'T' not in args.seq:
        print(f'The sequence "{args.seq}" is RNA')
    else:
        print(f'The sequence "{args.seq}" can be DNA or RNA')
else:
    print(f'The sequence "{args.seq}" is not DNA nor RNA')

## Finally, if the optional "--motif" argument is provided, the script searches for the motif in the input sequence using the re module. It prints a message indicating whether the motif was found or not. ##
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND the motif")
    else:
        print("NOT FOUND the motif")

