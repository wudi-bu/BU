// AUTHOR AnindyaPaul akpaul@bu.edu
// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

typedef vector< vector<int> > int_matrix;
typedef vector< vector<double> > double_matrix;

typedef struct {
    int returnCode;
    int_matrix matrix;
} int_matrix_return;

typedef struct {
    int returnCode;
    double_matrix matrix;
} double_matrix_return;

int_matrix_return readIntMatrix (string fileName, int rows, int cols) {
    
    int returnCode = 0;
    int_matrix matrix;
    int_matrix_return returnStruct;
    
    try {
        ifstream infile(fileName);
        string line;
        
        if(!infile) {
            returnCode = 2;
        } else {
    
            while (getline(infile, line)) {
                istringstream iss(line);
                int data;
                vector<int> matrix_row;
        
                while (iss >> data) {
                    matrix_row.push_back(data);
                }
        
                if(matrix_row.size() != cols) {
                    returnCode = 3;
                }
        
                matrix.push_back(matrix_row);
            }
    
            if(matrix.size() != rows) {
                returnCode = 3;
            }
        }
    } catch (exception e) {
        returnCode = 2;
    }
    
    returnStruct.returnCode = returnCode;
    returnStruct.matrix = matrix;
    
    return returnStruct;
}


double_matrix_return readDoubleMatrix(string fileName, int rows, int cols) {
    
    int returnCode = 0;
    double_matrix matrix;
    double_matrix_return returnStruct;
    
    try {
        ifstream infile(fileName);
        string line;
        
        if(!infile) {
            returnCode = 2;
        } else {
    
            while (getline(infile, line)) {
                istringstream iss(line);
                double data;
                vector<double> matrix_row;
        
                while (iss >> data) {
                    matrix_row.push_back(data);
                }
        
                if(matrix_row.size() != cols) {
                    returnCode = 3;
                }
        
                matrix.push_back(matrix_row);
            }
    
            if(matrix.size() != rows) {
                returnCode = 3;
            }
        }
    } catch (exception e) {
        returnCode = 2;
    }
    
    returnStruct.returnCode = returnCode;
    returnStruct.matrix = matrix;
    
    return returnStruct;
}


int_matrix multiply(const int_matrix& A,const int_matrix& B)
{
    
    int M = A.size();
    int N = A[0].size();
    int L = B[0].size();
    
    cout << "M=" << M << endl;
    cout << "N=" << N << endl;
    cout << "L=" << L << endl;
    
    int_matrix c(M,vector<int>(L));
    
    for (int i=0;i<M;i++)
        for (int j=0;j<L;j++)
            for (int k=0;k<N;k++)
                c[i][j] += A[i][k] * B[k][j];
    
    return c;
}


double_matrix multiply(const double_matrix& A,const double_matrix& B)
{
    
    double M = A.size();
    double N = A[0].size();
    double L = B[0].size();
    
    double_matrix c(M,vector<double>(L));
    
    for (int i=0;i<M;i++)
        for (int j=0;j<L;j++)
            for (int k=0;k<N;k++)
                c[i][j] += A[i][k] * B[k][j];
    
    return c;
}


int writeIntMatrix (string fileName, int_matrix matrix) {

    int_matrix_return returnStruct;

    try {
        ofstream fileStream;
        fileStream.open(fileName);
        
        if(!fileStream.good()) {
            return 4;
        }
    
        for (auto it = matrix.begin(); it!=matrix.end(); ++it) {
            vector<int> rows = *it;
        
            bool firstCol = true;
            for (auto rowIterator = rows.begin(); rowIterator != rows.end(); ++rowIterator) {
                
                int data = *rowIterator;
                if(firstCol) {
                    firstCol = false;
                    fileStream << data;
                } else {
                    fileStream << " " << data;
                }
            }
            
            fileStream << endl;
        }
    
        fileStream.close();
    } catch (exception e) {
        return 4;
    }
    
    return 0;
}


int writeDoubleMatrix (string fileName, double_matrix matrix) {
    
    double_matrix_return returnStruct;
    
    try {
        ofstream fileStream;
        fileStream.open(fileName);
        
        if(!fileStream.good()) {
            return 4;
        }
        
        for (auto it = matrix.begin(); it!=matrix.end(); ++it) {
            vector<double> rows = *it;
            
            bool firstCol = true;
            for (auto rowIterator = rows.begin(); rowIterator != rows.end(); ++rowIterator) {
                
                double data = *rowIterator;
                if(firstCol) {
                    firstCol = false;
                    fileStream << data;
                } else {
                    fileStream << " " << data;
                }
            }
            
            fileStream << endl;
        }
        
        fileStream.close();
    } catch (exception e) {
        return 4;
    }
    
    return 0;
}


string upperCase(string input) {
    for (std::string::iterator it = input.begin(); it != input.end(); ++ it)
        *it = toupper((unsigned char)*it);
    return input;
}


int main(int argc, const char * argv[]) {
    
    bool isTypeInt = false, isSquareMatrix = false;
    int size1 = 0, size2 = 0, size3 = 0;
    string inputFile1 = "", inputFile2 = "", outputFile = "";
    int_matrix intMatrix1, intMatrix2;
    double_matrix doubleMatrix1, doubleMatrix2;
    
    if (argc < 6 || argc > 8) {
        return 1;
    }
    
    for (int i=1; i<argc ; i++) {
        
        if (i == 1) {
            string s(argv[i]);
            if (s == "int") {
                isTypeInt = true;
            } else if (s == "double") {
                isTypeInt = false;  //Already initialized as false, so this line is not required
            } else {
                return 1;
            }
        } else {
            if (i == 2) {
                try {
                    string argv2 = argv[i];
                    string::size_type sz;
                    size1 = stoi(argv2, &sz);
                    
                    if(argv2.substr(sz) != "") {
                        return 1;
                    }
                    
                    if(size1 < 1) {
                        return 1;
                    }
                }
                catch (exception e) {
                    return 1;
                }
            } else {
                if (i == 3) {
                    try {
                        string argv3 = argv[i];
                        string::size_type sz;
                        size2 = stoi(argv3, &sz);
                        
                        if(argv3.substr(sz) != "") {
                            inputFile1 = argv[i];
                            isSquareMatrix = true;
                        }
                    }
                    catch (exception e) {
                        inputFile1 = argv[i];
                        isSquareMatrix = true;
                    }
                } else {    //i > 3
                    if(isSquareMatrix) {
                        if (i == 4) {
                            inputFile2 = argv[i];
                        } else if (i == 5) {
                            outputFile = argv[i];
                        } else if (i > 5) {
                            return 1;
                        }
                    } else {    //Not a square matrix
                        if(i == 4) {
                            string argv4 = argv[i];
                            string::size_type sz;
                            try {
                                size3 = stoi(argv4, &sz);
                                
                                if(argv4.substr(sz) != "") {
                                    return 1;
                                }
                            }
                            catch (exception e) {
                                return 1;
                            }
                        } else if (i == 5) {
                            inputFile1 = argv[i];
                        } else if (i == 6) {
                            inputFile2 = argv[i];
                        } else if (i == 7) {
                            outputFile = argv[i];
                        } else if (i > 7) {
                            return 1;
                        }
                    }
                }
            }
        }
    }
    
    if(isSquareMatrix) {
        size2 = size1;
        size3 = size1;
    } else {
        if (size2 < 1 || size3 < 1) {
            return 1;
        }
    }
    
    if(inputFile1 == "" || inputFile2 == "" || outputFile == "") {
        return 2;
    }
    
    if(isTypeInt) {
        int_matrix_return matrix1WithReturnCode = readIntMatrix(inputFile1, size1, size2);
        if(matrix1WithReturnCode.returnCode != 0) {
            return matrix1WithReturnCode.returnCode;
        } else {
            intMatrix1 = matrix1WithReturnCode.matrix;
        }
        
        int_matrix_return matrix2WithReturnCode = readIntMatrix(inputFile2, size2, size3);
        if(matrix2WithReturnCode.returnCode != 0) {
            return matrix2WithReturnCode.returnCode;
        } else {
            intMatrix2 = matrix2WithReturnCode.matrix;
        }
        
        int_matrix prodMatrix = multiply(intMatrix1, intMatrix2);
        
        return writeIntMatrix(outputFile, prodMatrix);
        
    } else {
        double_matrix_return matrix1WithReturnCode = readDoubleMatrix(inputFile1, size1, size2);
        if(matrix1WithReturnCode.returnCode != 0) {
            return matrix1WithReturnCode.returnCode;
        } else {
            doubleMatrix1 = matrix1WithReturnCode.matrix;
        }
        
        double_matrix_return matrix2WithReturnCode = readDoubleMatrix(inputFile2, size2, size3);
        if(matrix2WithReturnCode.returnCode != 0) {
            return matrix2WithReturnCode.returnCode;
        } else {
            doubleMatrix2 = matrix2WithReturnCode.matrix;
        }
        
        double_matrix prodMatrix = multiply(doubleMatrix1, doubleMatrix2);
        
        return writeDoubleMatrix(outputFile, prodMatrix);
    }
    
    return 0;
}



