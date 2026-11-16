"""Finite 5-integral critical-orbit certificates for q=3/(5n), r=7/5.
A successful closed graph is an all-height IDF certificate; a search cutoff
is inconclusive and is never interpreted as mathematical nontermination.
"""
from fractions import Fraction as F
from collections import deque
from math import gcd


def certificate(n,max_states=10000):
 if n<=2 or gcd(n,21)!=1:raise ValueError('require n>2 and gcd(n,21)=1')
 q,r=F(3,5*n),F(7,5)
 states={F(1)};todo=deque([F(1)]);edges={}
 while todo:
  x=todo.popleft();row=[]
  for d in (F(0),F(1),r):
   y=d+q*x
   if y.denominator%5==0:row.append(None);continue
   row.append(y)
   if y not in states:
    states.add(y);todo.append(y)
    if len(states)>max_states:return None
  edges[x]=tuple(row)
 return tuple(sorted(states)),edges


def verify(n,states):
 q,r=F(3,5*n),F(7,5)
 states=set(states)
 return F(1) in states and all(x>0 and x.denominator%5!=0 for x in states) and all(
  (d+q*x).denominator%5==0 or d+q*x in states
  for x in states for d in (F(0),F(1),r))

if __name__=='__main__':
 import argparse,json
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('n',type=int,nargs='+');parser.add_argument('--max-states',type=int,default=10000)
 args=parser.parse_args()
 for n in args.n:
  result=certificate(n,args.max_states)
  if result is None:print(json.dumps({'n':n,'status':'inconclusive cutoff'}));continue
  states,edges=result
  assert verify(n,states)
  print(json.dumps({'n':n,'status':'verified finite closure','states':list(map(str,states)),'edges':{str(x):[str(y) if y is not None else 'negative 5-adic valuation' for y in row] for x,row in edges.items()}}))
