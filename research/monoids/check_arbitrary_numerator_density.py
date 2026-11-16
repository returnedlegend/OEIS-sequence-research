"""Exact carry, simple-root, and boundary checks for arbitrary numerators."""
from fractions import Fraction as F
from itertools import product
from math import factorial, gcd

if __package__:
    from .reciprocal_factorizations import factor_integer, cyclic_digits, valuation
else:
    from reciprocal_factorizations import factor_integer, cyclic_digits, valuation


def validate(a,D,A,n):
    if not (a>=3 and D>a and gcd(a,D)==gcd(A,D)==1
            and (a-2)*D<A<(a-1)*D and (A+D)%a==0):
        raise ValueError('invalid fixed digit parameters')
    blocks=factor_integer(D)
    if not all(p**e>a for p,e in blocks.items()):
        raise ValueError('each denominator block must exceed a')
    if not (n>=max(a,4) and gcd(n,a*A*factorial(a-2))==1
            and set(factor_integer(n))-set(blocks)):
        raise ValueError('invalid admissible parameter, including factorial condition')
    return blocks


def numerator(a,D,A,n,seed,word):
    h,derivative=seed,0
    for depth,digit in enumerate(word,1):
        h*=a;derivative*=a
        coefficient=(A*D**(depth-1) if digit==a-1 else digit*D**depth)
        h+=coefficient*n**depth
        derivative+=coefficient*depth*n**(depth-1)
    return h,derivative


def integral_closure(a,D,A,n,p,limit=10000):
    q,r=F(a,D*n),F(A,D);digits=[F(i) for i in range(a-1)]+[r]
    states={F(i) for i in range(1,a-1)};stack=list(states)
    while stack:
        x=stack.pop()
        for d in digits:
            y=d+q*x
            if y.denominator%p and y not in states:
                states.add(y);stack.append(y)
                if len(states)>limit:raise RuntimeError('inconclusive cutoff')
    return states


def check():
    count=0
    for a,D,A,n in [(4,5,11,7),(5,16,49,11),(6,7,29,11),(4,35,101,11)]:
        blocks=validate(a,D,A,n);b=D*n;q,r=F(a,b),F(A,D)
        digits=[F(i) for i in range(a-1)]+[r]
        C0=F(a-1)/(1-q);C=r/(1-q)
        assert C0<a and a-2<C<a-1 and r*r>C
        for x,y in product(digits,repeat=2):
            for z in (x+y,x*y):
                residue=z.numerator*pow(z.denominator,-1,a)%a
                carry=(z-digits[residue])/q
                assert carry>=0 and cyclic_digits(carry,a,b) is not None
                count+=1
        for p,e in blocks.items():
            for seed in range(1,a-1):
                for depth in range(1,5):
                    for tail in product(range(a),repeat=depth-1):
                        word=(a-1,)+tail
                        root=(-a*seed*pow(A,-1,p))%p;modulus=p
                        for _ in range(1,e*depth):
                            lifts=[root+j*modulus for j in range(p)
                                   if numerator(a,D,A,root+j*modulus,seed,word)[0]%(p*modulus)==0]
                            assert len(lifts)==1
                            root=lifts[0];modulus*=p
                        h,derivative=numerator(a,D,A,root,seed,word)
                        assert h%p**(e*depth)==0
                        assert derivative%p==A*pow(a,depth-1,p)%p!=0
                        count+=1
    assert integral_closure(4,5,11,7,5)=={F(1),F(2),F(17,7)}
    assert integral_closure(5,16,49,11,2)=={F(1),F(2),F(3),F(34,11)}
    assert integral_closure(5,8,27,7,2)=={F(1),F(2),F(3)}
    assert F(49,16)*2**4==49
    assert F(27,8)*2**3==3**3
    count+=5
    # This parameter satisfies the earlier weaker gcd(n,aA)=1 condition,
    # but violates the necessary factorial condition in the actual theorem.
    assert gcd(6,5*49)==1
    try:
        validate(5,16,49,6)
    except ValueError:
        pass
    else:
        raise AssertionError('factorial-condition violation accepted')
    q=F(5,96)
    assert 5==q*3*2**5
    assert 3*q==F(5,32) and valuation(3*q,3)==0
    count+=3
    print(f'Passed {count} exact arbitrary-numerator carry, lifting, and boundary checks.')


if __name__=='__main__':check()
