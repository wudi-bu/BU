# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR DiWu wudi@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

massOfEarthInKG = 5.972 * pow(10,24);
    
    
# Assuming earth is made of iron, as earth's core is mostly made of iron.
# We'll use hydrogen (lightest element) to calculate upper bound
# and uranium (heaviest element) to calculate lower bound

massOfIronAtomInKG = 9.27 * pow(10,-26);
massOfHydrogenAtomInKG = 1.6727 * pow(10,-27);
massOfUraniumAtomInKG = 3.952 * pow(10,-25);

numberOfIronAtoms = massOfEarthInKG/massOfIronAtomInKG;
numberOfHydrogenAtoms = massOfEarthInKG/massOfHydrogenAtomInKG;
numberOfUraniumAtoms = massOfEarthInKG/massOfUraniumAtomInKG;

#Number of protons and number of electrons are the same

#There are 26 protons in an Iron atom.
numberOfIronElectrons = 26 * numberOfIronAtoms;

#There is 1 proton in a Hydrogen atom.
numberOfHydrogenElectrons = 1 * numberOfHydrogenAtoms;

#There are 92 protons in a Uranium atom.
numberOfUraniumElectrons = 92 * numberOfUraniumAtoms;

#Number of bits in 1TB
oneTB = pow(2,43);

estimate = numberOfIronElectrons/oneTB;

upperBound = numberOfHydrogenElectrons/oneTB;
lowerBound = numberOfUraniumElectrons/oneTB;
"""Control the number of the output of the scientific notation 
   so that it is the same with the output of C++ program"""  
upperBound = format(upperBound,'.5e')
estimate = format(estimate,'.5e')
lowerBound = format(lowerBound,'.5e')
print(estimate);
print(lowerBound);
print(upperBound);
