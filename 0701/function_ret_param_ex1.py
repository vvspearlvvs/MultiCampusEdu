def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return int(a/b)

a=int(input())
b=int(input())
print("{} + {} = {}".format(a,b,add(a,b)))
print("{} - {} = {}".format(a,b,sub(a,b)))
print("{} * {} = {}".format(a,b,mul(a,b)))
print("{} / {} = {}".format(a,b,div(a,b)))
