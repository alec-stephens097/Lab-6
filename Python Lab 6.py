total = 0
userInput = int(raw_input())
for x in range(userInput):
    print "how much does the item cost?"
    userInput = int(raw_input())
    total = total + userInput
print total

TotalList = []
for x in range(3):
    print 'how much does the item cost?'
    userInput = int(raw_input())
    TotalList.append(userInput)
print sum(TotalList)

range(1,userInput):
    