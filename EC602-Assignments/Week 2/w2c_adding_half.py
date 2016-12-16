# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

from math import inf

def number_from_half(s : str):

    #Convert the input string to binary in string format
    binaryRepresentation = (str(bin(int(s, 16)))[2:]).zfill(16)
    #Get the first bit of the converted string to determine sign
    sign = pow(-1, int(binaryRepresentation[0]))
    #Split the bits 2-6 as the exponential part
    exponent = binaryRepresentation[1:6]
    #Split the rest bits as the fraction part
    fraction= binaryRepresentation[6:]
    #Handle the case when the exponential part is all '0'

    if exponent == "00000":
        
        value = decimalRepresentation(fraction)
        return sign * (2**(-14)) * value

    #Handle the case when the exponential part is all '1' which indicates infinity    
    elif exponent == "11111":
        return sign * inf
    #Calculating the sum of the interger part 1 and the fraction part
    #then mutiply it with 2 to the power of exopnential and times the sign
    #The exponential is stored in the format of frameshift code
    # so the exponential = the value of the (exponential part - 01111(15 in decimal))
    else: 
        value = 1
        value += decimalRepresentation(fraction)
        exponentValue = int(exponent, 2)
        return sign * (2**(exponentValue - 15)) * value

#Convert the binary string(fraction part) to caculable number and sum up to return result in decimal
#Remember that range(a,b) is a,a+1,...,b-1 does not include b
def decimalRepresentation(s : str):
    
    value = 0
    for count in range(len(s)):
        value += int(s[count])*(2**(-(count+1)))
    
    return value
    

def main():
#Flag to jump out of the loop    

    total = 0
    flag = True
    
    while flag:
        s = input()
        try:
            num = number_from_half(s)
            total += num
        except ValueError:
            print(str(total))
            flag = False
            

if __name__ == '__main__':
    main()


