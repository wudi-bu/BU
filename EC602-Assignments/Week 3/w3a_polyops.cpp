// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu
// AUTHOR AnindyaPaul akpaul@bu.edu

#include <vector>

using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)

{
    long int x = (a.size() > b.size())? a.size() : b.size();
    
    Poly sum(x,0);
    
    for (long int m = 0; m < x; m++)
    {
        
        if (m < a.size())
        {
            sum[m]+=a[m];
        }
        if (m < b.size())
        {
            sum[m]+=b[m];
        }
    }
    return sum;
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a,const Poly &b){
    vector<double> result(a.size()+b.size()-1,0.0f);
    for(int i = 0;i<a.size();i++)
        for(int j = 0;j<b.size();j++)
            result.at(i+j) += a.at(i)*b.at(j);
    return result;
}
