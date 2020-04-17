#!/usr/bin/python3
#
# https://gist.github.com/rocket-pig/762585e45fcd2211932689f0fb993133

import re
import subprocess

stats=subprocess.getoutput('gnunet-statistics').split('\n')

while True:
    lines,j=[],[]
    c=0
    for i in stats:
        process = re.findall(' +([a-zA-Z]+) +(\#.+\:) +(\d+)',i)
        try:
            lines.append(list(process[0]))
        except:
            continue

    categories = list(set([i[0] for i in lines]))

    # have user pick category
    for i in categories:
        print(c,i)
        c+=1
    selection = input('---------------------------------\npick a category: ')
    #display ONLY ones from category
    results = []
    for i in lines:
        if i[0] == categories[int(selection)]:
            i[1] = " ".join(i[1].split()[1::]) # remove the leading hash.
            results.append(i[1::])
    results.sort()
    for i in results:
        print('{:<50}{:<}'.format(i[0],i[1])) #print a nice column for easy listenin'
    print('---------------------------------')
