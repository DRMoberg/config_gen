from __future__ import division

import numpy as np
import sys
from itertools import chain, islice
import math

histfile = sys.argv[1]
hsplit = histfile.split('.')
outp = "config."+hsplit[1]

linebody = open(sys.argv[1]).readlines()
header = linebody[:4]
open('noheader.txt', 'w').writelines(linebody[4:])

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

output = open(outp, 'w')

if (len(sys.argv) != 2):
    print "usage: python executable.py input_file.xyz"
    sys.exit()

vf_line = '     0.000000000         0.000000000         0.000000000     ' + '\n'

with open('noheader.txt', 'r') as filestream:
	with output as f2:

		while True:
		    lines_gen = list(islice(filestream,2))
		    if not lines_gen:
		        break
		    counter = 0
		    for line in lines_gen:
			if (counter == 0):
				numstr = line.split()
				linenew = numstr[0] + '              ' + numstr[1] + '\n'
				f2.write(linenew)

			if (counter == 1):
				f2.write(line)
				f2.write(vf_line)
				f2.write(vf_line)

			counter = counter + 1

filestream.close()
f2.close()

line_prepender(outp,header[3])
line_prepender(outp,header[2])
line_prepender(outp,header[1])
line_prepender(outp,'         2         2        0      0')
line_prepender(outp,'\n')
