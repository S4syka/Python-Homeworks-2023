# ITERATOR

"""
iterator is an object which enables you to
iterate iterable things(some collections:list,tuple,dict,range)
only one time.

you have access by iterator on some collection's
element and then you can jump on next element.

iterator Object have 2 methods:
1. iter() : 'a iterable -> 'a iterator
which gives us presentation of iterator of some collection
return type - iterator object
parameter type - iterable object

2. next() : 'a iterable -> 'a  (iterable object changes)
the way to access next item in iterator on collection
return type - next item in collection ( 'a iterable -> 'a)
parameter type - iterator object
"""


lst = [1,2,3]

# 1. iter() , __iter__() :  'a list -> 'a iterator object
# create iterator object
iter1=lst.__iter__()
iter2=lst.__iter__()
iter3=iter(lst)

# 2 next() :
# use next to access next elements
print("1,next of iter1: ", next(iter1)) #1
print("2,next of iter1: ", iter1.__next__()) #2
print(iter1.__init__())
print("3,next of iter1: ", next(iter1)) #1
print("1,next of iter2: ", next(iter2))
print("1,next of iter3: ", next(iter3))

try:
    next(iter1)
except(StopIteration):
    print("we can imagine now iterator gone away and it's on null pointer")

# Iterators Purpose: enable you to work with large data sets efficiently
# hey allow you to process data one item at a time,
# without having to load the entire collection into memory at once.

"""
In Python, many built-in functions and modules use iterators
behind the scenes. For example, the range() function
returns an iterator that generates a sequence of numbers
"""

# now let's try to write my iterator which idea is as range()

class Naturalnumbers:
    # where iterator locates current position on 1
    def __init__(self):
        self.current = 1
    # gives iterator object
    def __iter__(self):
        return self
    # change current position by adding 1
    # returns new position where iterator locates
    def __next__(self):
        result =  self.current
        self.current += 1
        return result


class my_range:
    def __init__(self,start,end):
        self.curr=start
        self.end=end
        self.step=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr>self.end:
            raise StopIteration
        else:
            result=self.curr
            self.curr+=self.step
            return result

class Range:
    def __init__(self,start,end,step):
        self.curr=start
        self.endpoint=end
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr >= self.endpoint:
            raise StopIteration
        else:
            result =  self.curr
            self.curr += self.step
            return result

class FibonacciIterator:
    def __init__(self, n):
        self.size = n
        self.f1 = 1
        self.f2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.size:
            raise StopIteration
        self.count += 1
        self.f1, self.f2 = self.f2, self.f2 + self.f1
        return self.f1


smth = FibonacciIterator(5)
print("AQA VAR: " + str(smth.__next__()))
print("AQA VAR: " + str(smth.__next__()))
print("AQA VAR: " + str(smth.__next__()))
print("AQA VAR: " + str(smth.__next__()))
print("AQA VAR: " + str(smth.__next__()))
print("AQA VAR: " + str(smth.__next__()))


naturals=Naturalnumbers()
my_range = Range(0,10,1)
print("range:",next(my_range))
print("range:",my_range.__next__())



print("call naturals object:",naturals)
print("call naturals __iter__() method:",naturals.__iter__())
print("call constructor:",naturals.__init__())
print("call next() method:",naturals.__next__())
# what does it change ??? print("call constructor:",naturals.__init__())
print("call position (current) attribute:",naturals.current)
print("second next:",naturals.__next__())

"""
Create an iterator that generates a sequence of Fibonacci numbers.
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones,
starting from 0 and 1. The first few numbers in the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Your iterator should have the following methods:

__init__(self) - initializes the starting values of the sequence to 0 and 1.
__iter__(self) - returns the iterator object itself (i.e., self).
__next__(self) - generates the next number in the sequence and updates the current values.
"""
class fibonacci:
    def __init__(self,end):
        self.position1 = 0
        self.position2 = 1
        self.endpoint = end
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.endpoint:
            raise StopIteration

        result = self.position1
        self.position1, self.position2 = self.position2, self.position1 + self.position2
        self.count+=1
        return result


# fibonacci = fibonacci(3)
# print("mine")
# print(fibonacci.__next__())
# print(fibonacci.__next__())
# print(fibonacci.__next__())
# print(fibonacci.__next__())

class Fibonacci:
    def __init__(self):
        self.position1 = 0
        self.position2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        pos1 = self.position1
        self.position1 , self.position2 = self.position2 , self.position1+self.position2
        return pos1

fibo =  Fibonacci()
print(fibo)
print(fibo.position1,fibo.position2)
for i in range(0,10):
    print(fibo.__next__())

"""
In Python, a generator is a special type of iterator that generates values on-the-fly
 instead of storing them in memory all at once. It allows you to iterate
 over a sequence of items, but instead of returning a complete sequence, 
 it returns one item at a time.

A generator function is defined using the yield keyword instead of return.
 When the function is called, it returns a generator object, 
 which can be iterated over using the next function or a for loop. 
 Each time the yield keyword is encountered, the function pauses and 
 returns the value of the expression following the yield keyword. The next time the next function is called on the generator object, execution of the function resumes from where it left off, and continues until the next yield statement is encountered
"""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
generator0=infinite_sequence()
print("infinity",next(generator0))
print("infinity",next(generator0))
print("infinity",next(generator0))

def evens():
    num=2
    while True:
        yield num
        num+=2
print(next(evens()))

evens= (i for i in range(0,10) if i%2==0)
print(evens)
print(next(evens))


def sequence(endpoint):
    num=0
    count=0
    while count<endpoint:
        yield num
        num+=1
        count+=1
seq=  sequence(3)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

generator10 = (i for i in range(0,10))


gen = infinite_sequence()
print("infinity:",next(infinite_sequence()))

for i in range(10):
    print(next(gen))

# generator creation :

generator = (i for i in range(0,10))

"""
Generators are useful in situations where you need to process large amounts of data, but you don't want to load it all into memory at once. Instead, you can generate the data on-the-fly, and process it one item at a time. 
This can save memory and improve performance.
"""
# Create a list of the squares of the first 10 integers using a generator expression
squares = [x ** 2 for x in range(10)]

# Create a list of the squares of the first 10 even integers using a generator expression and filter function
even_squares = [x ** 2 for x in range(20) if x % 2 == 0]


# word -> length in sentence
sentence="asddfasdfasdf dfasdfa fasdfasdf asdfasdf"
word_len= { word:len(word) for word in sentence}

"""
Generators are lazy: When you call a generator function, it doesn't start executing the function immediately. Instead, it returns a generator object, which you can use to iterate over the items one at a time. This is known as lazy evaluation, and it allows generators to work efficiently with large amounts of data.

Generators use less memory: Because generators only generate items on-the-fly, they use much less memory than other collection types. This is especially important when working with large data sets.

Generators are iterable: A generator object is also an iterable object, which means you can use it in a for loop or any other function that expects an iterable. You don't have to worry about implementing the __iter__ and __next__ methods yourself.

Generators can be infinite: Because generators generate values on-the-fly, they can be infinite. This means that you can create a generator that generates an infinite sequence of values without running out of memory.

Generators can be chained: The itertools module in Python provides many functions for working with iterators and generators. One useful function is chain, which allows you to chain together multiple iterators or generators into a single sequence. This can be useful for processing data from multiple sources.

Generators can be filtered: Another useful function in the itertools module is filter, which allows you to filter items from an iterator or generator based on a certain condition. This can be useful for selecting specific items from a large data set.

Overall, generators are a powerful tool in Python for working with large data sets or infinite sequences. They are easy to use, memory-efficient, and can be combined with other tools like the itertools module to perform complex operations on data.

"""

class fibIterator:
    def __init__(self,n):
        self.pos1=0
        self.pos2=1
        self.number=n
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        current_pos = self.pos1
        if self.count < self.number:
            self.pos1 , self.pos2 = self.pos2 , self.pos1 + self.pos2
            self.count += 1
        else:
            raise StopIteration
        return current_pos



fibIter =  fibIterator(5)
print(fibIter)
print(fibIter.__next__())
print(fibIter.__next__())
print(fibIter.__next__())
print(fibIter.__next__())
print(fibIter.__next__())
print(fibIter.__next__())
