import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-o', # Name of option
                dest='outfile', # Variable name to store option (optional)
                help='output file of merged intervals of 2 input bed files', # Help text (optional)
                )
parser.add_argument('-a', # Name of option short form
                    dest='infile_a', # Variable name to store option (optional)
                    help='Input file1 in bed format', # Help text (optional)
                    )

parser.add_argument('-b', # Name of option short form
                    dest='infile_b', # Variable name to store option (optional)
                    help='Input file2 in bed format', # Help text (optional)
                    )

parser.add_argument('--std', # Name of option short form
                    action='store_true',
                    default = False, # Variable name to store option (optional)
                    help='option for standard output', # Help text (optional)
                    )

args = parser.parse_args() # Parse arguments

with open(args.outfile, mode="wt") as bed_intersect:
    with open(args.infile_a,mode="r") as bed_a, open(args.infile_b,mode="r") as bed_b: # Create file handle
        
        for index_a, line_a in enumerate(bed_a): # Iterate line by line through the file
                col_a = line_a.strip().split('\t')  #make tuple of columns
                bed_b.seek(0) # start comparing from the first line of file b
                chr_a = col_a[0]
                start_a = int(col_a[1])
                end_a = int(col_a[2])

                for index_b, line_b in enumerate(bed_b):
                    col_b = line_b.strip().split('\t')  #make tuple of columns
                    chr_b = col_b[0]
                    start_b = int(col_b[1])
                    end_b = int(col_b[2])
                    if chr_a == chr_b:
                        if (start_a >= start_b and start_a <= end_b) or (start_b >= start_a and start_b <= end_a):
                            if args.std==True:
                                sys.stdout.write(f'{chr_a}\t{start_a}\t{end_a}\n')
                            else:
                                bed_intersect.write(f'{chr_a}\t{start_a}\t{end_a}\n')
                                break

                        elif(start_b >= start_a and start_b <= end_a):
                            if args.std==True:
                                sys.stdout.write(f'{chr_a}\t{start_a}\t{end_a}\n')
                            else:
                                bed_intersect.write(f'{chr_a}\t{start_a}\t{end_a}\n')
