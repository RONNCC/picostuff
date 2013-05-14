f = open('manual.txt','r')
w = open('manualw.txt','w')
from string import lower,ascii_lowercase as lc
lca=[x for x in lc]
l=len(lca)
r=[lower(k) for k in f.read()]
os=19
replace=dict([(lca[i],lca[(i+os)%l]) for i in range(l)])
print replace
for y in r:
    if y in replace:
        w.write(replace[y])
    else:
        w.write(y)
