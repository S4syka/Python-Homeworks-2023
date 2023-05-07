"""
- difference between arguments and parameters
- Positionl and keyword arguments
_ Default arguemnts
_ Variable length arguments ( *args and **kwargs)
_ Container unpacking into function arguments
_ local vs global arguments
_ parameter passing ( by value or by reference)

"""

def foo(name):
    print(name)

x=foo(1)

def foo(a,b,c):
    print(a,b,c)

foo(1,2,3)
# we can
foo(b=1,a=2,c=3)

def foo(a,b,c,d=4):
    print(a,b,c,d)

foo(1,2,3,d=3)

def foo(a, b, *args, **kwargs):
    print(a,b)
    print(args)
    for i in args:
        print(i)
    print(kwargs)
    for i in kwargs.items():
        print(i[0],"=",i[1])

foo(1,2, 3,4,5,6 , e=-1,f=-2,d=-3)



def foo(a,b,*,c,d):
    print(a,b,c,d)

foo(1,2,c=3,d=4)



def foo(*args,last):
    for arg in args:
        print(arg)
    print(last)
foo(1,2,3,4, last=4)




def foo(a,b,c):
    print(a,b,c)

foo(*range(1,6,2))

foo(**{'a':1,'b':2,'c':1})




def foo():
    x = number
    print("number inside function",x)

number=0
foo()

#
#
#
#


# def foo():
#     x = number
#     number=3
#     print("number inside function",x)
#
# number=0
# foo()



def foo():
    global number
    x = number
    number=3
    print("number inside function",x)

number=0
foo()
print("3:",number)




def foo():
    number=3
    print("number in f:",number)

number = 0

foo()
print(number)
#



def foo():
    global number
    number=3

number = 0
foo()
print(number)

# immutable object

def foo(x):
    x+=5

var = 10
foo(var)
print(var)

def foo(lst):
    lst.append(0)

lst0=[1,2,3]
foo(lst0)
print(lst0)





# value passed (immutable)

def foo(lst):
    lst.append(0)
lst1=[1,1,1]
foo(lst1)
print(lst1)



def foo(lst):
    lst=[1,2,3]
    lst.append(4)
    lst[0]=-1

lst0=[0,0,0]
foo(lst0)
print(lst0)


l0=[1,2,3]
# when l0 pass on function
l0_copy=l0.copy()
# operation
l0_copy.append(1)

print(l0)