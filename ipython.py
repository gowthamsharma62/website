def bs(a,x,l,h):
    if l<=h:
        m=(l+h)//2
        if a[m]==x:
            return m
        elif a[m]>x:
            return bs(a,x,l,m-1)
        else:
            return bs(a,x,m+1,h)
    else:
        return -1
a=[2,3,11,2,33,1,22,32,44,55]
x=33
l=0
h=len(a)-1
print("it is located in index:",bs(a,x,l,h))

