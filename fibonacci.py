#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 1, 1;
c=a+b;
print(a);
print(b);
print(c);
r=b/a;
while b < 1000:
    a,b=b,c;
    c=a+b;
    r=b/a;
    print(b,r);

print("phi= ") # or print('phi = ' + str(r))
print(r)

