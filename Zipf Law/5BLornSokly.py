# This is my solution and I didn't copy or sent it to the others
#Lorn Sokly N42TNN


from __future__ import print_function  # using print as a function

import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

def zipf(filename):
    frequency_dic = {}
    count = 0
    with open (filename,"r") as file:
        words=[word.strip(',.-_?!;/ ').lower() for line in file for word in line.strip().split()]
        for word in words:
            if word != '':
                count = frequency_dic.get(word,0)
                frequency_dic[word] = count + 1  
        data = sorted(frequency_dic.values(), reverse=True)    
        plt.loglog(range(1, len(data)+1), data)
        plt.show()
        print(sorted(frequency_dic.items(), key=lambda x:x[1], reverse=True)[0:10])

def main():
    zipf(filename)

if __name__ == "__main__":
    main()
