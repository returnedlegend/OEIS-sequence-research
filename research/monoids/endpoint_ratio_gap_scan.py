import json,time,sys
if __package__:
    from .endpoint_ratio_automaton import find
else:
    from endpoint_ratio_automaton import find
limit=int(sys.argv[1]) if len(sys.argv)>1 else 10000
start=time.time();B=1;largest=(0,None,None);out=[]
for v in range(1,limit+1):
 B*=5
 for u in (B.bit_length()-1,B.bit_length()):
  z=find(1<<u,B)
  if z.get('states',0)>largest[0]:largest=(z['states'],u,v)
  if not z.get('no_path'):
   out.append({'u':u,'v':v,**{k:w for k,w in z.items() if k not in ('A','B')}})
   print('exception',out[-1],flush=True)
 if v%1000==0:print(json.dumps({'through_v':v,'max_states':largest,'elapsed':time.time()-start}),flush=True)
print(json.dumps({'through_v':limit,'max_states':largest,'exceptions':out,'elapsed':time.time()-start}),flush=True)
