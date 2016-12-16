# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

from numpy import zeros,exp,array,pi

     
class my(list):
    def __getitem__(self,key):
        return list

def DFT_Matrix(n):
    dft_matrix = zeros((n,n),dtype=complex)
    for k in range(n):
        for m in range(n):
            dft_matrix[k,m] = exp(((k*m)%n)*(((-1)*2*pi*complex(0,1))/n))
    return dft_matrix

def DFT(x):
    input_signal = Convert_Signal(x)
    size = (input_signal.shape)[0]
    return (DFT_Matrix(size).dot(input_signal)).reshape(size,)
       
def Convert_Signal(x):
    if(type(x)==type(dict()) or hasattr(x, '__call__')):   
        raise ValueError
    size = len(x)
    count = 0
    input_signal = zeros((size,1),dtype=complex)
    for n in x:
        if(type(n)==type('a')):
            raise ValueError
        else:
            input_signal[count,0] = n
            count+=1
    return input_signal

