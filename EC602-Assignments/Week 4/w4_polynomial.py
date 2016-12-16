# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR DiWu wudi@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu


class Element():
        
        def __init__(self, coefficient=complex(0,0), index=0):        
            self.coefficient = coefficient;
            self.index = index
            
            
class Polynomial():

    # Polynomial is represented as a list of consisting of a list of co-efficients and indices
    # Such as, [[complexCoefficient_1, integerIndex_1],[complexCoefficient_2, integerIndex_2]]
    
        
    def __init__(self,sequence=[complex(0,0)]):
        count = 0
        sequenceLength = len(sequence)
        elements = {}
        while count < sequenceLength:
            
            index = sequenceLength - (count + 1)
            
            if complex(sequence[count]) != complex(0,0):
                elements[index] = sequence[count]
                
            count += 1
            
        self.elements = elements


    def __setitem__(self, key, value): 
        self.elements[key] = value


    def __getitem__(self, key):
        if key in self.elements:
            return self.elements[key]
        return complex(0,0)

    def copy(value):
        poly = Polynomial()
        polyElements = dict.copy(value.elements)
        poly.elements = polyElements
            
        return poly
        
        
    def __add__(self,value):
        sumPoly = Polynomial.copy(self)
            
        for valueKey in dict.keys(value.elements):
            if valueKey in sumPoly.elements:
                sumPoly.elements[valueKey] += value.elements[valueKey]
            else:
                sumPoly.elements[valueKey] = value.elements[valueKey]
            
        return sumPoly
        
        
        
    def __sub__(self,value):
        diffPoly = Polynomial.copy(self)
            
        for valueKey in dict.keys(value.elements):
            if valueKey in diffPoly.elements:
                diffPoly.elements[valueKey] -= value.elements[valueKey]
            else:
                diffPoly.elements[valueKey] = (0 - value.elements[valueKey])
            
        return diffPoly
        
        
        
    def __mul__(self,value):
        prodPoly = Polynomial()
        prodPoly.elements = {}
        
        for selfKey in dict.keys(self.elements):
            for valueKey in dict.keys(value.elements):
                
                print(self.elements[selfKey])
                print(value.elements[valueKey])
                print((selfKey + valueKey))
                
                if (selfKey + valueKey) in prodPoly.elements: 
                    prodPoly.elements[(selfKey + valueKey)] += (self.elements[selfKey] * value.elements[valueKey])
                else:
                    prodPoly.elements[(selfKey + valueKey)] = (self.elements[selfKey] * value.elements[valueKey])
                
        return prodPoly
        
        
    def __eq__(self, other):
        for selfKey in dict.keys(self.elements):
            if selfKey not in other.elements: 
                return False
            elif selfKey in other.elements and self.elements[selfKey] != other.elements[selfKey]: 
                return False
        
        return True


    def eval(self, value):
        result = 0
        for selfKey in dict.keys(self.elements):
            result += self.elements[selfKey]*pow(value, selfKey)

        return result
        
        
    def deriv(self):
        poly = Polynomial()
        for selfKey in dict.keys(self.elements):
            if selfKey != 0: 
                poly.elements[selfKey - 1] = (selfKey * self.elements[selfKey])

        return poly
        
        
    def __str__(self):
        
        polyString = "Poly="    
        for selfKey in sorted(dict.keys(self.elements)):
            polyString += "(Co-efficient=" + str(self.elements[selfKey]) + ", Index=" + str(selfKey) + "), "
            
        if(len(polyString) > 7):
            return polyString[:len(polyString) - 2]
            
        return polyString
            

    def __repr__(self):
        return str(self)
                    
                

def readInput(s):
    num = s.split()
    numList = []
    for n in num:
        numList.append(complex(n))
        
    return Polynomial(numList)
    
    
def main():
    #print("Enter a sequence")
    #polynomial1 = readInput(input())
    
    #print("Enter another sequence")
    #polynomial2 = readInput(input())
    
    polynomial1 = Polynomial([4,3.5,6])
    polynomial2 = Polynomial([2.2,1.8,5.9])
    
    polynomial1[3] = 6.1
    polynomial2[3] = 8.2
    
    polynomial1[-1] = -4.5
    polynomial2[-1] = 0.7
    
    polynomial3 = polynomial1 + polynomial2
    print(polynomial3)
    
    polynomial4 = polynomial2 - polynomial1
    print(polynomial4)
    
    print(polynomial1 == polynomial2)
    polynomial5 = Polynomial([6.1,4,3.5,6])
    polynomial5[-1] = -4.5
    print(polynomial5 == polynomial1)
    
    polynomial6 = Polynomial([1.2,3.2,5.6])
    print(polynomial6.eval(1.1))
    
    polynomial7 = Polynomial.deriv(polynomial6)
    print(polynomial7)
    
    polynomial8 = polynomial6 * polynomial7
    print(polynomial8)
    
    polynomial9 = Polynomial([1,3])
    polynomial10 = Polynomial()
    print(polynomial9 == polynomial10)
    

if __name__=="__main__":
	main()