# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

import numpy as np
from numpy import pi,cos,sin,linspace,ones_like,zeros_like
import unittest
from numpy import pi,cos,sin,linspace,ones_like,zeros_like
import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
import time

def read_wave(fname,debug=False):
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels
    
def loudest_band(music, frame_rate, bandwidth):
    energy = 0.0
    low = 0
    high = 0
    
    FFT = np.fft.fft(music) #FFT of the input signal

    N_ponit = len(FFT) #length of the inputsignal which is equal to length of FFT
    print(N_ponit)
# following code is just for plotting
    """ xf = np.linspace(0.0, 500, N_ponit/2)
    import matplotlib.pyplot as plt
    plt.plot(xf, np.abs(FFT[0:N_ponit/2]))
    plt.grid()
    plt.show()"""
# Caculate the magnitude of FFT 
    Magnitude = np.abs(FFT[0:N_ponit])

# The Frequency resolution is defined to be Fs/N
    Interval_Hertz=frame_rate/N_ponit
    print(Interval_Hertz)
#The number of intervals which the bandwidth correspond to
    freq_in_point = int(bandwidth/Interval_Hertz)
    print(freq_in_point)
#lowest possible high end, in case for DC it won't update
    high = freq_in_point
#If bandwidth is shorter than one interval,set it to 1
    if(freq_in_point==0):
        freq_in_point = 1
#do summition of magnitude sqaured to get energy
    temp = 0
    for k in range(freq_in_point+1):
        energy += pow(Magnitude[k],2)
    print(energy)
        
    for n in range(0,int(N_ponit/2)-freq_in_point): 
        temp = temp + pow(Magnitude[n+freq_in_point],2) - pow(Magnitude[n],2)
        #here when n is 895 temp is the same as energy,the difference is 1.16415321827e-10
        if(temp>energy):
                if(n==2):
                    print(temp)
                    print(energy)
                energy = temp
                low = n+1
                high = low+freq_in_point
    #set points to 0 other than the filtered frequency in FFT

    for n in range(N_ponit):
        if(n<low or (n>high and n<N_ponit-high) or n>N_ponit-low):
            FFT[n]= 0  
    print(low)
    print(high)
    result = (low*Interval_Hertz,high*Interval_Hertz,np.fft.ifft(FFT))
    return result
    

def main():
        frame_rate,T,ftest,bandwidth = 1000,1,100,20
        t = linspace(0,T,T*frame_rate,endpoint=False)
        m = ones_like(t) + sin(2*pi*bandwidth//2*t)
        low,high,filtered = loudest_band(m,frame_rate,bandwidth)

if __name__=="__main__":
    main()
