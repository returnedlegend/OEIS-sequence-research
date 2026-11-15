"""Finite exact-arithmetic checks of the constructive conductor proof.

These checks validate the implementation on 300 targets; the general theorem
is proved separately in TWO_SMALL_GENERATORS.md.
"""
from fractions import Fraction as F
from math import gcd,lcm,ceil

def check(q,r,n,extra):
 D=lcm(q.denominator,r.denominator)
 A=int(q*D);B=int(r*D)
 if A>B:q,r,A,B=r,q,B,A
 g=gcd(A,B);u=A//g;v=B//g;z=F(g,D)
 C=F(g,1-z)+F((u-1)*v*z,(1-u*z)*(1-v*z))
 K=[0]
 for i in range(1,n+1):K.append(u*K[-1]+(u-1)*v**i)
 N=ceil(C*D**n)+extra
 hs=[];rem=N
 for i in range(n):
  residue=(rem*pow(D**(n-i),-1,g))%g if g>1 else 0
  h=K[i]+(residue-K[i])%g
  hs.append(h);rem=(rem-h*D**(n-i))//g
 hs.append(rem)
 assert hs[-1]>=K[-1]
 def H(h,i):
  if i==0:return [h]
  j=(h*pow(v**i,-1,u))%u if u>1 else 0
  w=(h-j*v**i)//u
  out=H(w,i-1)+[0]
  out[-1]+=j
  assert all(c>=0 for c in out)
  assert sum(c*u**(i-k)*v**k for k,c in enumerate(out))==h
  return out
 total=F(0)
 for i,h in enumerate(hs):
  co=H(h,i)
  total+=sum(c*q**(i-j)*r**j for j,c in enumerate(co))
 assert total==F(N,D**n)
 return C
for q,r in [(F(2,3),F(2,5)),(F(6,35),F(10,21)),(F(4,9),F(2,5)),(F(2,3),F(3,5)),(F(5,6),F(5,8))]:
 for n in range(1,7):
  for extra in range(10):C=check(q,r,n,extra)
 print(q,r,'C0=',C,'60 exact reconstructions passed')
