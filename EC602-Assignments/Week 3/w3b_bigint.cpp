// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu
// AUTHOR AnindyaPaul akpaul@bu.edu

#include <string>
#include <vector>

using namespace std;

typedef string BigInt;

BigInt multiply_int(const BigInt &a,const BigInt &b) {
    
    long int sizeOfA = a.size();
    long int sizeOfB = b.size();
    vector<double> product ((sizeOfA+sizeOfB - 1),0);
    
    for(long int i=(sizeOfA-1); i>=0; i--) {
        for(long int j=(sizeOfB-1); j>=0; j--) {
            
            long int indexOfProduct = (sizeOfA + sizeOfB) - (i+j) - 2;
            double prodValue = product[indexOfProduct];
            
            long int firstOperand = (((double)a[i]) - '0');
            long int secondOperand = (((double)b[j]) - '0');
            prodValue +=  firstOperand * secondOperand;
            
            if(prodValue >= 10) {
                if((indexOfProduct)==(sizeOfA + sizeOfB - 2)) {
                    product.resize(sizeOfA + sizeOfB);
                }
                
                int tensDigit = (prodValue / 10);
                product[indexOfProduct+1] += tensDigit;
                prodValue -= (10 * tensDigit);
            }
            
            product[indexOfProduct]=prodValue;
        }
    }
    
    BigInt productAsBigInt = "";
    for(vector<double>::iterator it = (product.end() -1); it >= product.begin(); it--) {
        productAsBigInt += (char)((*it) + '0');
    }
    
    return productAsBigInt;
}
