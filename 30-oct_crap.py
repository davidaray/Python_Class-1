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
