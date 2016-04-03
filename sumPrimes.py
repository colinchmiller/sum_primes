primeNumbers = [2];
primeSum = 2;

def primeCalc(primeSum, primeNumbers):
    for x in range(3,1000):
        if primeCheck(x) != False:
            primeNumbers.append(x);
            primeSum = primeSum + x;
            print "Prime Sum is:" primeSum;
            print "Prime Numbers:" primeNumbers

def primeCheck(x):
    for y in primeNumbers:
        if x % y == 0:
            return False;

primeCalc(primeSum, primeNumbers);
