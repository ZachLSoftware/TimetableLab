import re
def expandModule(module):
    n=re.search(r'\d+$', module)
    num=int(n.group())
    base = re.search(r'^\d+\D', module)
    base = base.group()
    expanded=[]
    for i in range(1,num+1):
        expanded.append(base+str(i))
    return expanded

