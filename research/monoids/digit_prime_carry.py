"""Exact finite prime-valuation closure certificates for inverse digit maps."""
from collections import deque
from fractions import Fraction as F

if __package__:
    from .reciprocal_factorizations import valuation
else:
    from reciprocal_factorizations import valuation


def closure(q,digits,p,max_states=10000):
    q=F(q);digits=tuple(map(F,digits))
    if valuation(q,p)>=0:raise ValueError('require negative q valuation')
    threshold=min(valuation(d,p) for d in digits if d)-valuation(q,p)
    seeds={d for d in digits if d and valuation(d,p)>=threshold}
    states=set(seeds);pending=deque(seeds)
    while pending:
        x=pending.popleft()
        for d in digits:
            y=d+q*x
            if valuation(y,p)<threshold:continue
            if y not in states:
                states.add(y);pending.append(y)
                if len(states)>max_states:return None
    return {'prime':p,'threshold':threshold,'states':list(map(str,sorted(states)))}


def verify(q,digits,record):
    q=F(q);digits=tuple(map(F,digits));p=record['prime']
    if valuation(q,p)>=0:return False
    threshold=min(valuation(d,p) for d in digits if d)-valuation(q,p)
    if record['threshold']!=threshold:return False
    states=set(map(F,record['states']))
    seeds={d for d in digits if d and valuation(d,p)>=threshold}
    if not seeds<=states:return False
    if any(x<=0 or valuation(x,p)<threshold for x in states):return False
    return all(valuation(d+q*x,p)<threshold or d+q*x in states
               for x in states for d in digits)


def upper_bound(record):
    p=record['prime']
    return max([0,record['threshold']-1]+
               [valuation(F(x),p) for x in record['states']])
