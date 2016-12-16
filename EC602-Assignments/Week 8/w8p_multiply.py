#!/usr/bin/env python
# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu
import sys
from numpy import zeros
def main():
    print("6")
    if(len(sys.argv)==6):
        print("7")
        try:
            size = int(sys.argv[2])
            if(size==0):
                exit(1)   
        except :
            print("exit 1 10")
            exit(1)
        size = int(sys.argv[2])
        if(sys.argv[1]=='int'):
            Matrix_A = readin_matrix(0,sys.argv[3],[size])
            Matrix_B = readin_matrix(0,sys.argv[4],[size])
            Matrix_result = Matrix_A @ Matrix_B
            print(Matrix_result)
            write_matrix(Matrix_result,sys.argv[5])
        elif(sys.argv[1]=='double'):
            Matrix_A = readin_matrix(1,sys.argv[3],[size])
            print(Matrix_A)
            Matrix_B = readin_matrix(1,sys.argv[4],[size])
            print(Matrix_B)
            Matrix_result = Matrix_A @ Matrix_B  
            print(Matrix_result)
            write_matrix(Matrix_result,sys.argv[5])
        else:
            print("exit 1 30")
            exit(1)
    elif(len(sys.argv)==8):
        for k in range(2,5):
            try:
                if(int(sys.argv[k])==0):
                    exit(1)
            except:
                print("exit 1 36")
                exit(1) 
        size1 = int(sys.argv[2])
        size2 = int(sys.argv[3])
        size3 = int(sys.argv[4])
        if(sys.argv[1]=='int'):
            Matrix_A = readin_matrix(0,sys.argv[5],[size1,size2])
            Matrix_B = readin_matrix(0,sys.argv[6],[size2,size3])
            Matrix_result = Matrix_A @ Matrix_B
            print(Matrix_result)
            write_matrix(Matrix_result,sys.argv[7])
        elif(sys.argv[1]=='double'):
            Matrix_A = readin_matrix(1,sys.argv[5],[size1,size2])
            Matrix_B = readin_matrix(1,sys.argv[6],[size2,size3])
            Matrix_result = Matrix_A @ Matrix_B
            write_matrix(Matrix_result,sys.argv[7])
        else:
            print("exit 1 53")
            exit(1)
    else:
        print("exit 1 56")
        exit(1)

def readin_matrix(dtype,filename,size_arr):
    if(len(size_arr)==1):
        size = size_arr[0]
        try:
            f = open(filename, 'r')
        except:
            print("exit 2 65")
            exit(2)
        count = 0
        print("69")
        if(dtype==0):
            matrix = zeros((size,size),dtype=int)
            for x in f.readlines():
                x = x.split()
                for k in x:
                    try:
                        matrix[int(count/size),count%size] = int(k)
                    except:
                        print("exit 3 76")
                        exit(3)
                    count+=1
        else:
            matrix = zeros((size,size),dtype=float)
            for x in f.readlines():
                x = x.split()
                for k in x:
                    try:
                        matrix[int(count/size),count%size] = float(k)
                    except:
                        print("exit 3 87")
                        exit(3)
                    count+=1
        print(count)
        if(count!= size*size):
            print("exit 3 92")
            exit(3)
    else:
        row = size_arr[0]
        column = size_arr[1]
        try:
            f = open(filename, 'r')
        except:
            print("exit 2 100")
            exit(2)
        count = 0
        if(dtype==0):
            matrix = zeros((row,column),dtype=int)
            for x in f.readlines():
                x = x.split()
                for k in x:
                    try:
                        matrix[int(count/column)][count%column] = int(k)
                    except :
                        print("exit 3 111")
                        exit(3)
                    count+=1
        else:
            matrix = zeros((row,column),dtype=float)
            for x in f.readlines():
                x = x.split()
                for k in x:
                    try:
                        matrix[int(count/column)][count%column] = float(k)
                    except :
                        print("exit 3 122")
                        exit(3)
                    count+=1
        print(count)
        if(count!= row*column):
            print("exit 3 127")
            exit(3)
    f.close()
    return matrix
        
def write_matrix(matrix,filename):
    row = matrix.shape[0]
    column = matrix.shape[1]
    try:
        f = open(filename, 'w')
    except:
        print("exit 4 145")
        exit(4)
    count = 0
    for i in range(row):
        for j in range(column):
            f.write(str(matrix[i][j]))
            if(count%column == (column-1)):
                print(count)
                f.write('\n')
            else:
                f.write(' ')
            count+=1
    f.close()

if __name__=="__main__":
    main()            

        
