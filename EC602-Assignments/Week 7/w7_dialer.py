# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

# WAV file support
import scipy.io.wavfile as wavfile
import numpy as np
from numpy import pi

# Define DTMF keypad frequencies
fl_list = [697, 770, 852, 941]
fh_list = [1209, 1336, 1477]

# Define function to find the indices of each key within DTMF keypad frequencies
def find_key(key):
    if key == '*':
        pos = [4, 1]
    elif key == '0':
        pos = [4, 2]
    elif key == '#':
        pos = [4, 3]
    else:
        j = ((int(key) - 1)%3) + 1
        i = (int(key) - j)//3 + 1
        pos = [i, j]
    return pos
        
def dialer(file_name, frame_rate, phone, tone_time):
    result_list = []
    for digit in phone:
        
        # Find the corresponding DTMF keypad frequencies using the indices found
        [i, j] = find_key(digit)
        fl = fl_list[i - 1]
        fh = fh_list[j - 1]
        
        # Calculate the number of samples
        n = tone_time*frame_rate
        
        # Create the time array
        t = np.linspace(0, tone_time, n)
        
        # Generate two waveforms using the DTMF keypad frequencies
        tone_a = np.sin(2*pi*fl*t)
        tone_b = np.sin(2*pi*fh*t)
        
        # Average the two waveforms
        tone = (tone_a + tone_b)/2
        
        # Store resulting waveform in a list
        for data in tone:
            result_list.append(data)
            
    # Convert the list containing the waveforms into an array
    result = np.asarray(result_list)

    # Write to specified file name
    wavfile.write(file_name, frame_rate, result)
    
def main():
    pass

if __name__=="__main__":
    main()

        
        
        

        

    
