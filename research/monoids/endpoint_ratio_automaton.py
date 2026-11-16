"""Exact carry automaton for ratios of nonconstant endpoint atoms.

See PAIR_3_10_RATIO_AUTOMATON.md. All calculations use integers or Fractions.
The default search exhausts its finite graph; an optional state cap returns
an explicit unknown/capped result, never a no-path certificate.
"""

from collections import deque
from fractions import Fraction as F
import argparse
D=(0,10,14)
def find(A,B,max_states=None):
 end=2*(A-B);lo=-2*B;hi=2*A
 # state(k,flags), flags indicate not identically r in each word
 prev={};queue=deque()
 for dx in D[1:]:
  for dy in D[1:]:
   z=B*dx-A*dy
   if z%3:continue
   k=z//3
   if not lo<=k<=hi:continue
   flag=(dx!=14)+2*(dy!=14)
   st=(k,flag)
   if st not in prev:
    prev[st]=(None,dx,dy);queue.append(st)
 while queue:
  st=queue.popleft();k,flag=st
  if k==end and flag==3:
   path=[]
   while st is not None:
    old,dx,dy=prev[st];path.append((dx,dy));st=old
   path.reverse()
   q=F(3,10);r=F(7,5);xs=F(2);ys=F(2)
   for dx,dy in reversed(path):
    xs=F(dx,10)+q*xs;ys=F(dy,10)+q*ys
   assert xs==F(A,B)*ys and 1<=xs<2 and 1<=ys<2
   return {'A':A,'B':B,'length':len(path),'path':path,'x':str(xs),'y':str(ys),'states':len(prev)}
  for dx in D:
   for dy in D:
    z=10*k+B*dx-A*dy
    if z%3:continue
    nk=z//3
    if not lo<=nk<=hi:continue
    nf=flag|(dx!=14)|((dy!=14)<<1)
    ns=(nk,nf)
    if ns not in prev:
     prev[ns]=(st,dx,dy);queue.append(ns)
     if max_states is not None and len(prev)>max_states:return {'A':A,'B':B,'capped':len(prev)}
 return {'A':A,'B':B,'no_path':True,'states':len(prev)}
if __name__=='__main__':
 import json
 p=argparse.ArgumentParser();p.add_argument('--max-v',type=int,default=7);args=p.parse_args()
 for v in range(1,args.max_v+1):
  B=5**v
  for u in (B.bit_length()-1,B.bit_length()):
   A=2**u
   if not B<=2*A or not A<=2*B:continue
   z=find(A,B);print(json.dumps(z),flush=True)
