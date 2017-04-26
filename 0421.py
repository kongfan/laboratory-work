import time
import pdb
import logging

logging.basicConfig(level=logging.DEBUG)
a = 10
b = -2

i = 1
while i < 5:

    try:
        pdb.set_trace()
        print a/b
    except Exception as e:
     #   print "error",e
        print "!!!!!!!!!!!!!!!!!!!!!"
        logging.info(e)

    print "cuowu", i
    i = i + 1
    b = b + 1

print "end"

# def add(a,b):
#     """
#     >>>add(3,3)
#     6
#     >>>add(-12,4)
#     9
#     """
#     return a+b
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
