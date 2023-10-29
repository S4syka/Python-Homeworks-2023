#Write a function 'isSecondBitOn' which takes a number as an argument and checks if it's second bit (corresponding to 4). Function should return True if the bit is on or False otherwise.
#Ex. 6 -> 1
#     10 -> 0

def isSecondBitOn(num):
    if num & 4:
        return True
    else:
        return False
    
