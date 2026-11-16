"""Prefix-word certificates stable on exact 5-adic arithmetic progressions."""
from fractions import Fraction as F
from collections import deque
from math import gcd


def evaluate(n,word):
    x=F(1);q=F(3,5*n);digits=(F(0),F(1),F(7,5))
    for label in word:x=digits[label]+q*x
    return x


def tree(n,max_words=10000):
    if n<=2 or gcd(n,21)!=1 or n%5==0:
        raise ValueError('require n>2, gcd(n,21)=1, and5 not dividing n')
    q=F(3,5*n);digits=(F(0),F(1),F(7,5))
    pending=deque([((),F(1))]);words=[]
    while pending:
        word,x=pending.popleft();words.append(word)
        for label,d in enumerate(digits):
            y=d+q*x
            if y.denominator%5!=0:
                pending.append((word+(label,),y))
        if len(words)+len(pending)>max_words:return None
    return tuple(words)


def verify(n,words):
    if n<=2 or gcd(n,21)!=1 or n%5==0:return False
    words=set(map(tuple,words))
    if any(label not in (0,1,2) for word in words for label in word):return False
    if () not in words:return False
    for word in words:
        if word and word[:-1] not in words:return False
        x=evaluate(n,word)
        if x.denominator%5==0:return False
        for label in range(3):
            child=word+(label,)
            retained=evaluate(n,child).denominator%5!=0
            if retained!=(child in words):return False
    return True


def progression(n,words):
    exponent=1+max(map(len,words))
    modulus=5**exponent
    return {'representative':n,'residue':n%modulus,'exponent':exponent,
            'modulus':modulus,'words':[list(w) for w in words]}


if __name__=='__main__':
    import json,argparse
    from pathlib import Path
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit',type=int,default=10000)
    parser.add_argument('--write',action='store_true',
                        help='write regenerated certificates adjacent to this script')
    args=parser.parse_args()
    if args.limit<4:parser.error('--limit must be at least4')
    records={}
    for n in range(4,args.limit+1):
        if n%5!=1 or gcd(n,21)!=1:continue
        words=tree(n)
        assert words is not None and verify(n,words)
        rec=progression(n,words)
        records.setdefault((rec['residue'],rec['exponent']),rec)
    minimal=[]
    for (residue,exponent),rec in sorted(records.items(),key=lambda kv:kv[0][1]):
        if any(residue%old['modulus']==old['residue'] for old in minimal):continue
        minimal.append(rec)
    density=sum((F(1,rec['modulus']) for rec in minimal),F(4,5))
    data={'scope':'All progressions require n>2 and gcd(n,21)=1','source_limit':args.limit,
          'density_including_n_not_1_mod5':str(density),
          'uncovered_density':str(1-density), 'progressions':minimal}
    if args.write:
        Path(__file__).with_name('nearby_progression_certificates.json').write_text(json.dumps(data,indent=2)+'\n')
    print('unique classes',len(records),'minimal classes',len(minimal),
          'max exponent',max((rec['exponent'] for rec in minimal),default=0),
          'density',density,float(density),'uncovered',1-density)
    for rec in minimal[:10]:print(rec['residue'],rec['modulus'],len(rec['words']))
