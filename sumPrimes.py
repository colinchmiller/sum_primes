primeNumbers = [2];
primeSum = 2;

def primeCalc():
    for x in range(3,1000):
        if primeCheck(x) == False;

def primeCheck(x):
    for y in primeNumbers:
        if x % y == 0:
            return False

newbie();

for x in range(3,1000):
    for y in primeNumbers:
        if x % y == 0:
            primeTest = false;
            return
        else:
            primeTest = true;
    if primeTest == true:
        primeNumbers.push(x);
        primeSum = primeSum + x;
        print(primeSum);
