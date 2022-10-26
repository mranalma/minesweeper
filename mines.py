#https://github.com/mranalma/minesweeper.git

import random

numberRows=int(input("enter number of rows:"))
listVariable=[]
listVariable2=[]
indexes=[]
numberOfHouses=[]

#tolid moteghayer sefr
for k in range(numberRows*numberRows):
    listVariable.append(0)

print(listVariable)

#random mineha ro mirize to 0ha
for rn in range(numberRows+1):
    randomIndex=random.randint(0,numberRows*numberRows)
    listVariable.remove(listVariable[randomIndex])
    listVariable.insert(randomIndex,'*')

#tolid indexha
for i in range(numberRows):
    for j in range(numberRows):
       indexes.append(f'{i}-{j}')

print(indexes)
#corresponding two list
res = {indexes[i]: listVariable[i] for i in range(len(indexes))}

print(res)

#shekl khoneha
for i in range(1,numberRows+1):
    print(f' {i}',end='..')
    
print('')

for i in range(1,numberRows+1):
    print(' ----'*(numberRows),end='')
    print('-')
    print(i,end='')
    for j in range(numberRows):
        
        print(f'|   ',end='')
    print('|')
    
print(' ----'*(numberRows),end='')
print('-')

#dastebandi moteghayer dar dastehaye chandtaie be tor mosavi
for p in range(0, len(listVariable), numberRows):
    listVariable2.append(listVariable[p:p+numberRows])    

numberOfRow=int(input('enter number of your favorite row:'))
numberOfColomn=int(input('enter number of your favorite colomn:'))

print(f'your choice is:({numberOfRow},{numberOfColomn})')

#sum of mines in the next house that you choose
sumOfMine=0
if res[f'{numberOfRow}-{numberOfColomn}']=='*':
    print('oops! you lost')

#sum of mines in the next house that you choose
if res[f'{numberOfRow}-{numberOfColomn}']==0:
    try:
        if res[f'{numberOfRow-1}-{numberOfColomn-1}']==0:
            pass
        elif res[f'{numberOfRow-1}-{numberOfColomn-1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:
        if res[f'{numberOfRow-1}-{numberOfColomn}']==0:
            pass
        elif res[f'{numberOfRow-1}-{numberOfColomn}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:

        if res[f'{numberOfRow-1}-{numberOfColomn+1}']==0:
            pass
        elif res[f'{numberOfRow-1}-{numberOfColomn+1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:
        if res[f'{numberOfRow}-{numberOfColomn-1}']==0:
            pass
        elif res[f'{numberOfRow}-{numberOfColomn-1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:
        if res[f'{numberOfRow}-{numberOfColomn+1}']==0:
            pass
        elif res[f'{numberOfRow}-{numberOfColomn+1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:
        if res[f'{numberOfRow+1}-{numberOfColomn-1}']==0:
            pass
        elif res[f'{numberOfRow+1}-{numberOfColomn-1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:

        if res[f'{numberOfRow+1}-{numberOfColomn}']==0:
            pass
        elif res[f'{numberOfRow+1}-{numberOfColomn}']=='*':
            sumOfMine+=1
    except KeyError:
        pass
    try:

        if res[f'{numberOfRow+1}-{numberOfColomn+1}']==0:
            pass
        elif res[f'{numberOfRow+1}-{numberOfColomn+1}']=='*':
            sumOfMine+=1
    except KeyError:
        pass

    print(sumOfMine)

res[f'{numberOfRow}-{numberOfColomn}']=sumOfMine
print(res)

print(listVariable2)