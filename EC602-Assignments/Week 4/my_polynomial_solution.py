class Polynomial(dict):
    def __init__(self,seq=None):
        if seq:
            i = len(seq)-1
            for coeff in seq:
                self[i] = coeff
                i = i - 1

    def __add__(self,value):
        N=Polynomial()
        for exp in self:
            N[exp]=self[exp]
        for exp in value:
                N[exp] += value[exp]
        return N

    def __sub__(self,value):
        N=Polynomial()
        for exp in self:
            N[exp]=self[exp]
        for exp in value:
                N[exp] -= value[exp]
        return N

    def __getitem__(self,exp):
        return dict.__getitem__(self,exp) if exp in self else 0

    def __setitem__(self,exp,coeff):
        if coeff:
            dict.__setitem__(self,exp,coeff)
        elif exp in self:
            del self[exp]

    def eval(self,x):
        return sum( x**exp * self[exp] for exp in self)

    def deriv(self):
        P=Polynomial()
        for exp in self:
            P[exp-1] = exp * self[exp]
        return P

    def __mul__(self,other):
        P=Polynomial()
        for exp1 in self:
            for exp2 in other:
                P[exp1+exp2] += self[exp1]*other[exp2]
        return P
