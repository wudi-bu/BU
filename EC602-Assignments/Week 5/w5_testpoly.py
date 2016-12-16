# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

import unittest
import sys

authors=['akpaul@bu.edu']

class PolynomialTestCase(unittest.TestCase):
    
    """unit testing for polynomials"""
    
    def setUp(self):
        self.poly1 = Polynomial([1,2.5,complex(2,5)])
        self.poly2 = Polynomial([complex(-1.5,2.4),-1.4,6.9])
        self.poly3 = Polynomial([-complex(-1.5,2.4),1.4,-6.9])
        self.poly_empty = Polynomial()
        
    def test_init(self):
        polyNew = Polynomial()
        self.assertIsInstance(polyNew,Polynomial)
        p = Polynomial()
        q = Polynomial((3,4,5))
        self.assertEqual(q[0],5)
        self.assertEqual(q[1],4)
        self.assertEqual(q[2],3)
        self.assertEqual(p[0],0)
        self.assertEqual(p[-1],0)
        self.assertEqual(self.poly1[0],complex(2,5))
        self.assertEqual(self.poly1[1],2.5)
        self.assertEqual(self.poly1[2],1)

    def test_eq(self):
        polyEq = Polynomial()
        polyEq[0] = complex(2,5)
        polyEq[1] = 2.5
        polyEq[2] = 1
        p = Polynomial()
        p[5]=0
        self.assertTrue(self.poly_empty == p)
        self.assertEqual(self.poly1,polyEq)
        q = Polynomial([2,1,2.5,complex(2,5)])
        self.assertFalse(self.poly1 == q)
        self.assertFalse(q == self.poly1)
        
        
    def test_add(self):
        polyAdd = self.poly1 + self.poly2
        polyAddAssert = Polynomial()
        polyAddAssert[0] = (complex(2,5) + 6.9)
        polyAddAssert[1] = (2.5 + (-1.4))
        polyAddAssert[2] = (1 + complex(-1.5,2.4))
        self.assertEqual(polyAdd,polyAddAssert)
        self.assertEqual(self.poly2+self.poly3,self.poly_empty)
        
        
    def test_sub(self):
        polySub = self.poly2 - self.poly1
        polySubAssert = Polynomial([0,(complex(-1.5,2.4) - 1),((-1.4) - 2.5),(6.9 - complex(2,5))])
        self.assertEqual(self.poly2-self.poly2,self.poly_empty)
        self.assertEqual(self.poly_empty-self.poly2,self.poly3)
        self.assertEqual(polySub,polySubAssert)
        
    def test_mul(self):
        polyMul = self.poly1 * self.poly2
        polyMulAssert = Polynomial()
        polyMulAssert[0] = complex(2,5) * 6.9
        polyMulAssert[1] = (complex(2,5) * (-1.4)) + (2.5 * 6.9)
        polyMulAssert[2] = (1 * 6.9) + (2.5 * (-1.4) + (complex(2,5) * complex(-1.5,2.4)))
        polyMulAssert[3] = (2.5 * complex(-1.5,2.4)) + (1 * (-1.4))
        polyMulAssert[4] = (1 * complex(-1.5,2.4))
        self.assertEqual(polyMul,polyMulAssert)
        self.assertEqual(self.poly_empty*(self.poly1),Polynomial())
        p = Polynomial([2,3])
        q = Polynomial([2,-3])
        r = Polynomial([-9])
        r[2] = 4
        self.assertEqual(p*q,r)
    
    
    def test_deriv(self):
        a = Polynomial([3])
        self.assertEqual(a.deriv(), self.poly_empty)
        self.assertEqual(self.poly_empty.deriv(), Polynomial())
        p1 = Polynomial([5, 7, 13])
        p1[-5] = 10
        p2 = Polynomial()
        p2[1] = 10
        p2[0] = 7
        p2[-6] = -50

        self.assertEqual(p1.deriv(), p2)
    
    def test_eval(self):
        self.assertEqual(self.poly1.eval(0),complex(2,5))
        p = Polynomial([3, -4.69, complex(2,7)])
        q = Polynomial()
        q[-1]=complex(1,0)
        q[2]=complex(0,1)
        q[4]=10
        x = 4.1
        y=complex(1,0)

        self.assertEqual(p.eval(4.1), eval('3*x**2 + -4.69*x + complex(2,7)'))
        self.assertEqual(q.eval(y), (10*pow(y,4)) + (complex(0,1)*pow(y,2)) + (complex(1,0)*pow(y,-1)))
    
    def test_setitem(self):
         a = Polynomial()
         a[-3] = complex(2,5)
         self.assertEqual( a.eval(0.5),complex(2,5)*pow(0.5,-3))
         p = Polynomial([3, 7, 6])
         p[2] = 3.17
         self.assertEqual(p, Polynomial([3.17, 7, 6]))
         p1 = Polynomial()
         p1[-5] = 7.5
         p2 = Polynomial()
         p2[-5] = 10
         p2[-10] = 5
         p3 = Polynomial()
         p3[-5] = 10 + 7.5
         p3[-10] = 5

         self.assertEqual(p1+p2, p3)
         p = Polynomial()
         p[-5] = complex(5.99, -3)

         self.assertEqual(p[-5], complex(5.99, -3))
         p = Polynomial()
         p[1] = 3.7
         p[5] = 4
         p[7] = complex(1,1)
         p[7] = complex(0,0)
         q = Polynomial([complex(0,0), 0, 4, 0, 0, 0, 3.7, 0])
         self.assertTrue(p == q)
       
    
    def test_getitem(self):
        self.assertEqual(self.poly1[8],0)
        self.assertEqual(self.poly1[-9],0)
        self.assertEqual(self.poly1[1],2.5)
        self.assertEqual(self.poly1[0],complex(2,5))
     
    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial()

        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))
        
        
    def tearDown(self):
        pass
