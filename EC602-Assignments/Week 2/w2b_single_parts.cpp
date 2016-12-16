// AUTHOR AnindyaPaul akpaul@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu

// single_parts
#include <iostream>
#include <iomanip>

using namespace std;

typedef unsigned long int raw32;    //raw32 is a pseudonym for unsigned long int

// A structure which mimics exactly the internal representation of float
// Single Parts uses  32-bits of storage
struct Single_Parts {
    raw32 fraction : 23;    // use 23 bits for this
    raw32 exponent : 8;     // then 8 bits for this
    raw32 sign : 1;         // then 1 bit for this
};

// these represent the positions of the SIGN, EXPONENT, and FRACTION of double.
const raw32 MASK_SIGN = 1UL << 31;
const raw32 MASK_BEXP = 0xffUL << 23;
const raw32 MASK_FRAC = 0x7fffffUL;


// build and take_apart are inverse functions.
Single_Parts take_apart(float d)
{
    Single_Parts sp;
    raw32 x =  *reinterpret_cast<raw32*>(&d);
    sp.sign = (x bitand MASK_SIGN) >> 31;
    sp.exponent = (x bitand MASK_BEXP) >> 23;
    sp.fraction = (x bitand MASK_FRAC);
    return sp;
}

float build(Single_Parts sp)
{
    // read this from inside out:
    // this means get the address of sp, then think of it as a pointer to a float
    // then get the float and return it.
    return *reinterpret_cast<float*>(&sp);
}

float build_alt(Single_Parts sp)
{
    raw32 c=0;
    // explicitly move the single parts to their correct locations, and add.
    c = ( (raw32)sp.sign << 31) + ( (raw32)sp.exponent << 23) + sp.fraction;
    // read this from inside out:
    // this means get the address of c, then think of it as a pointer to a float
    // then get the float and return it.
    return *reinterpret_cast<float*>(&c) ;
}


// print out the parts of the structure Single_Parts
void print_sp(Single_Parts sp)
{
    if (sp.sign==1)
        cout << "negative"  << endl;
        else
        cout << "positive" << endl;
        cout << hex
        << setfill('0')
        << "expo: " << sp.exponent << endl
        << "frac: " << sp.fraction << endl
        << dec;
}

// define Single_Parts, build(), and take_apart() for float

int main()
{
    
    float num_from_build;
    
    float numbers[5]={1.0/3,2,1.3e10,3e11,6};
    
    // show the structure of the numbers
    for (int i=0;i<5;i++)
    {
        // take apart the numbers, then re-build to test that it works.
        
        Single_Parts s = take_apart(numbers[i]);
        num_from_build = build(s);
        
        cout << endl;
        print_sp(s);
        cout << numbers[i] << " " << num_from_build  << endl;
    }
    
    // example of a weird number, negative zero.
    double neg_zero = -0.0;
    
    cout << endl;
    cout << neg_zero << endl;
    
    print_sp(take_apart(neg_zero));
    
    return 0;
}
