print("----")
var = 10
print("var is: ", var)
print("----")
def foo():
    var = 20
    print("in foo, var is: ", var)
    print("----")

foo()

print("outside, var is: ", var)
print("----")

def bar():
    global var
    var = 30
    print("in bar, var (now global) is: ", var)
    print("----")

bar()

print("outside, var is: ", var)
print("----")