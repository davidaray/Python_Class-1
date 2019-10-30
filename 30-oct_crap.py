import os
import re

for FILE in os.listdir():
    if FILE.endswith(".fasta"):
        OUTPUT = open(FILE+".lft",'w')
        with open(FILE, 'r') as FIN:
            for LINE in FIN:
                if LINE.startswith('>'):
                    HEADER = re.sub('>','',LINE)
                    HEADER2 = re.sub('\n','',HEADER)
                    PART1_HEADER = HEADER2.split(":")
                    CONTIG = str(PART1_HEADER[0])
                    PART2_HEADER = PART1_HEADER[1]
                    SPLIT_PART2 = PART2_HEADER.split("-")
                    START = int(SPLIT_PART2[0])
                    END = int(SPLIT_PART2[1])
                    LENGTH = END-START
                    OUTPUT.write(str(START) + '\t' + str(HEADER2) + '\t' + str(LENGTH) + '\t' + str(CONTIG) + '\t' + str(END) + '\n')

                    
                    
### THINGS TO DO ###

# 1. Make this script fit in with the batch numbering system originally used. 
# 2. Adjust the directory structure to match the desired format... i.e. the RMPart plus all the 001, 002, 003, etc. 
# 3. Figure out why the last fasta file in the batch (i.e. the 50th batch) is not being included in the loop.
        # i.e. There isn't a .lft file made for the last batch.
    
    
