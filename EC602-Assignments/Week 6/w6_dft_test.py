# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

import unittest
import sys
import random
import numpy as np

class MyDFTTestClass(list):
    pass
    

class DFTTestCase(unittest.TestCase):
    
    def setUp(self):
        self.signal1 = [complex(1,2),123.123, 562.12, -367.09, complex(-98.32,-287.76)] #check for output shape
        self.signal2 = [complex(1,2),1, "A", -1]#check for char as element in input signal
        self.signal3 = np.random #check for single number as input signal
        self.signal4 = {1:complex(2,3), 2:complex(4,-1)} #check for dictionary as input signal
        self.signal5 = complex(0,1)#check for single number as input signal
        self.signal6 = "A,B,C"#check for string as input signal
        self.signal7 = ('A','B','C') #check for tuple with char element as input signal
        self.signal8 = MyDFTTestClass([1,2,3])#  check for self-written class as input signal
        

    def test_init(self): #test cases built upon signals in setup
        output1 = DFT(self.signal1)
        self.assertIsInstance(output1,np.ndarray)
        self.assertEqual(output1.shape, (5,))
        with self.assertRaises(ValueError):
            DFT(self.signal2)
        with self.assertRaises(ValueError):
            DFT(self.signal3)
        with self.assertRaises(ValueError):
            DFT(self.signal4)
        with self.assertRaises(ValueError):
            DFT(self.signal5)
        with self.assertRaises(ValueError):
            DFT(self.signal6)
        with self.assertRaises(ValueError):
            DFT(self.signal7)
        output2 = DFT(self.signal8)
        output3 = np.fft.fft(self.signal8)
        self.assertAlmostEqual(output2[1], output3[1])
    

    def test_compare(self): #check for calculation given the input signal is valid ,using loop to generate random complex numbers
        N=2
        while N <= 20:
            inputSignal = []
            for i in range(N):
                real = random.uniform(-1,1)
                imag = random.uniform(-1,1)
                inputSignal.append(complex(real,imag))
            
            try:
                dft=DFT(inputSignal)
                systemDFT = np.fft.fft(inputSignal)
            
                self.assertEqual(dft.shape, systemDFT.shape)
            
                for x in range(len(dft)):
                    self.assertAlmostEqual(dft[x], systemDFT[x])
            except:
                with self.assertRaises(ValueError):
                    DFT(inputSignal)
        
            N += 1

    def tearDown(self):
        pass
    
    
