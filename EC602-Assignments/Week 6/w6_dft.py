# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

from numpy import zeros,exp,array,pi

def DFT(sequence=[complex(0,0)]):
    
    #X[k]=DFT(x)=N−1∑n=0 x[n]e−j2πnk/N
    
    if type(sequence) == type(dict()) or hasattr(sequence, '__call__'):
        raise ValueError('Input is not a sequence')
    
    N = 0
    try:            
        N = len(sequence)
    except: 
        raise ValueError('Input contains non-numeric value')
        
    dft = zeros(shape=(N,), dtype=complex)
    k=0
    while k < N:
        n = 0
        dft[k] = 0
        for element in sequence:
            if (type(element) is not complex) and (type(element) is not float) and (type(element) is not int):
                raise ValueError('Input contains non-numeric value')
                
            dft[k] += element * exp((complex(0,-1)*2*pi*n*k)/N)
            n += 1
        k += 1
    
    return dft
