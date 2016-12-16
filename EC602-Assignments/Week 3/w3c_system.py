# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR DiWu wudi@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu

import numpy as np

def generateOutput(signal, impulse):  
    
    output = np.convolve(signal, impulse)
    
    stringValue = ''
    for item in output:
        stringValue += str(item) + ' '
        
    return stringValue[:len(stringValue) - 1]


def readInput(s):
    num = s.split()
    numList = []
    for n in num:
        numList.append(float(n))
        
    return numList


def main():
    
    signal = readInput(input())
    impulse = readInput(input())
    output = generateOutput(signal,impulse)
    print(output);
            

if __name__ == '__main__':
    main()