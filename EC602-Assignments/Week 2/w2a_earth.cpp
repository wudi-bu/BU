// AUTHOR AnindyaPaul akpaul@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu


#include <iostream>
#include <iomanip>
#include <cassert>
#include <math.h>

using namespace std;

int main() {
    
    long double massOfEarthInKG = ((long double)5.972) * pow(10,24);
    
    /*Assuming earth is made of iron, as earth's core is mostly made of iron.
      We'll use hydrogen (lightest element) to calculate the upper bound.
      and uranium (heaviest element) to calculate the lower bound*/
    
    long double massOfIronAtomInKG = ((long double)9.27) * pow(10,-26);
    long double massOfHydrogenAtomInKG = ((long double)1.6727) * pow(10,-27);
    long double massOfUraniumAtomInKG = ((long double)3.952) * pow(10,-25);
    
    long double numberOfIronAtoms = massOfEarthInKG/massOfIronAtomInKG;
    long double numberOfHydrogenAtoms = massOfEarthInKG/massOfHydrogenAtomInKG;
    long double numberOfUraniumAtoms = massOfEarthInKG/massOfUraniumAtomInKG;
    
    //Number of protons and number of electrons are the same
    
    //There are 26 protons in an Iron atom.
    long double numberOfIronElectrons = 26 * numberOfIronAtoms;
    
    //There is 1 proton in a Hydrogen atom.
    long double numberOfHydrogenElectrons = 1 * numberOfHydrogenAtoms;
    
    //There are 92 protons in a Uranium atom.
    long double numberOfUraniumElectrons = 92 * numberOfUraniumAtoms;
    
    //Number of bits in 1TB
    long double oneTB = pow(2,43);
    
    long double estimate = numberOfIronElectrons/oneTB;
    
    long double upperBound = numberOfHydrogenElectrons/oneTB;
    long double lowerBound = numberOfUraniumElectrons/oneTB;
    
    cout << estimate << endl;
    cout << lowerBound << endl;
    cout << upperBound << endl;
    
    return 0;
}
