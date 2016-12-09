#!/usr/bin/env python
inputfilename = "pbs_additive_v3_bgcorrected.txt"
outputfilename = "averaged_subtracted_" + inputfilename
outputfilename2 = "averaged_subtracted_tabbed_" + inputfilename

import os
filename = inputfilename
fh = open(filename)
all_lines = fh.readlines()

output = ''
for each in all_lines:
    split_line = each.split()
    first_split = split_line[0]
    split_line_length = len(split_line)
    curr_vals = []
    for i in range (1,split_line_length-2,2):
        first=float(split_line[i])
        second=float(split_line[i+1])
        avg=(first+second)/2
        curr_vals.append(avg)
    baseline = (float(split_line[split_line_length-1])+float(split_line[split_line_length-2]))/2
    out_list = []
    for each2 in curr_vals:
        out_list.append(each2-baseline)
    output+=first_split+"\n"
    for each3 in out_list:
        output+=str(each3)+"\n"

fh_output = open(outputfilename, 'w')
fh_output.write(output)
fh.close()
fh_output.close()
out2 = ""
fh_output2 = open(outputfilename2, 'w')
list_len = len(out_list)
periodicity = list_len+1
#print periodicity
out_lines = output.split("\n")
#print out_lines
out_list =[]
for h in range (0,periodicity):
    out_list.append("")
out_lines_len = len(out_lines)
for i in range (0,out_lines_len-1,periodicity):
    counter = 0
    for j in range(i,i+periodicity):
        to_add = str(out_lines[j])+"\t"
        out_list[counter]+=to_add
        counter+=1

for each5 in out_list:
    linetoadd = str(each5)+"\n"
    out2+=linetoadd
fh_output2.write(out2)
fh_output2.close()