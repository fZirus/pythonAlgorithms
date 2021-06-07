from math import sqrt
import time

aceptingInput = True
startingNum = 0
finalNum = 0


primeNums = []
while aceptingInput:
    print("First Num")
    try:
        startingNum = int(input())
        if (startingNum == 0):
            startingNum = 1
        aceptingInput = False
    except:
        print("Must be a valid integer.")
if (startingNum == 1 or startingNum == 2):
    startingNum = 5
    primeNums = [1,2,3]

aceptingInput = True
while aceptingInput:
    print("Last Num")
    try:
        finalNum = int(input())
        if (finalNum >= startingNum):
            aceptingInput = False
        else:
            print('Final Number must be larger than starting number')
    except:
        print("Must be a valid integer.")


start_time = time.time()
currentNum = startingNum
if (currentNum/2 - int(currentNum/2) == 0):
    currentNum += 1

while (currentNum <= finalNum):
    isPrime = True
    currentDevisor = 3
    currentNumSqrRoot = int(sqrt(currentNum))
    while (isPrime and currentDevisor <= currentNumSqrRoot):
        currentDevision = currentNum/currentDevisor
        currentDevisor += 2
        if (currentDevision - int(currentDevision) == 0):
            isPrime = False
    if(isPrime):
        primeNums.append(currentNum)
    else:
        isPrime = True
    currentNum += 2
finishTime = time.time() - start_time
print("--- " + str(finishTime) +" seconds ---")
f= open("output.txt","w+")
f.write( "---" + str(startingNum) + " to " + str(finalNum) + " in " + str(finishTime) +" seconds ---\n" + str(primeNums))
