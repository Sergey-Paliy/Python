n = 385916
firstHalf=0
secondHalf=0
while n>1000:
    firstHalf=firstHalf+n%10
    n=n//10
while n>0:
    secondHalf=secondHalf+n%10
    n=n//10
if firstHalf==secondHalf:
    print("yes")
else:
    print("no")
