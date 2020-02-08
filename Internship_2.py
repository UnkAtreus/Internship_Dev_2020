__author__ = 'KittipatDechkul'

import math

def Check_Prime(number):
    limit = int(number)
    limit += 1
    prime = []
    for i in range(2,limit):
        prime.append(i)
    i = 2
    while(i <= int(math.sqrt(number))):
        if i in prime:
            for j in range(i * 2,limit,i):
                if j in prime:
                    prime.remove(j)
        i += 1
    if number in prime:
        return True
    return False
    
def MoveDot(pos,str):
    str = str[0:pos] + str[pos + 1] + str[pos] + str[pos + 2:]
    return str

def isFloatingPrime(buffer):
    for i in range(3):
        pos = buffer.find('.')
        buffer = MoveDot(pos,buffer)
        pos = buffer.find('.')
        number = float(buffer[:pos])
        bPrime = Check_Prime(number)
        if(bPrime == True):
            print(True)
            return 0
    print(False)

def Check_Digit(buffer):
    if (len(buffer) > 13 or len(buffer) <= 0):
        return False
    return True

def main():
    while True:
        buffer = input("")
        if (buffer == '0.0'): # check exit
            break
        if (buffer.find('.') == -1): # check dot
            buffer = ""
            continue
        if (Check_Digit(buffer) == False): # check digit
            buffer = ""
            continue
        if (float(buffer) < 1 or float(buffer) > 10): # check num
            continue
        if len(buffer) < 5:
            buffer = buffer + "000"
        
        isFloatingPrime(buffer)
    
if __name__ == '__main__':
    main()