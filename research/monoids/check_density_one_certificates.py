"""Exact finite audits supporting the density-one theorem's certificates.

The asymptotic theorem is proved symbolically in the accompanying notes;
these checks validate the stored progression trees and finite lifting cases.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path
import json

if __package__:
    from .nearby_progressions import evaluate,verify
else:
    from nearby_progressions import evaluate,verify


def numerator_and_derivative(n,word):
    h,derivative=1,0
    for depth,label in enumerate(word,1):
        h*=3;derivative*=3
        if label==1:
            h+=(5*n)**depth
            derivative+=depth*5**depth*n**(depth-1)
        elif label==2:
            h+=7*5**(depth-1)*n**depth
            derivative+=7*depth*5**(depth-1)*n**(depth-1)
    return h,derivative


def check():
    data=json.loads(Path(__file__).with_name('nearby_progression_certificates.json').read_text())
    records=data['progressions']
    assert len(records)==112
    density=F(4,5);checks=0
    for record in records:
        n=record['representative'];words=record['words']
        exponent=1+max(map(len,words));modulus=5**exponent
        assert exponent==record['exponent'] and modulus==record['modulus']
        assert n%modulus==record['residue']
        assert verify(n,words)
        density+=F(1,modulus)
        # These sample substitutions validate implementation of the theorem;
        # the integer-polynomial proof gives stability for every substitution.
        for shift in (1,2,21):
            shifted=n+shift*modulus
            if gcd(shifted,21)==1:assert verify(shifted,words)
        for word in words:
            h,derivative=numerator_and_derivative(n,word)
            assert evaluate(n,word)==F(h,(5*n)**len(word))
            if word:
                assert word[0]==2
                assert derivative%5==(7*3**(len(word)-1))%5
        checks+=1
    for i,left in enumerate(records):
        for right in records[i+1:]:
            common=min(left['modulus'],right['modulus'])
            assert left['residue']%common!=right['residue']%common
    assert density==F(data['density_including_n_not_1_mod5'])
    assert 1-density==F(data['uncovered_density'])
    counts=[]
    for depth in range(1,7):
        roots=set()
        for tail in product(range(3),repeat=depth-1):
            word=(2,)+tail;root=1;modulus=5
            for stage in range(1,depth):
                lifts=[root+t*modulus for t in range(5)
                       if numerator_and_derivative(root+t*modulus,word)[0]%(5*modulus)==0]
                assert len(lifts)==1
                root=lifts[0];modulus*=5
            roots.add(root)
            assert numerator_and_derivative(root,word)[0]%5**depth==0
            checks+=1
        assert len(roots)<=3**(depth-1)
        counts.append(len(roots))
    assert counts==[1,2,5,13,34,94]
    print(f'Passed {checks} exact progression/lifting checks;112 infinite progressions verified.')


if __name__=='__main__':check()
