from stack import stack
from node import node

l=[]
path = input("Enter the filepath:  ")
s = open(path, "r").read()

stk = stack()
linestk = stack()
lno = 0

for i in range(len(s)):
    if s[i] == "\n":
        lno+=1
    elif s[i] == "{":
        stk.s_push(i)
        linestk.s_push(lno)
    elif s[i] == "}":
        n = node()
        n.level = stk.length()
        n.start = stk.s_peek()
        n.text = s[stk.s_pop():i+1]
        if stk.length()==0:
            n.parent = 0
        else:
            n.parent = stk.s_peek()
        n.lineNum = linestk.s_pop()
        l.append(n)


def lineIndex(text,n):
    count = 0
    for i in range(len(text)):
        if text[i] == "\n":
            count+=1
        if count == n :
            return i

l2 = []
startToNode = {}

for element in l:
    linestart = lineIndex(s,element.lineNum)
    singleline = s[linestart:element.start+1]
    if singleline.find("if")!= -1 or singleline.find("else if")!= -1 or singleline.find("else")!= -1:
        l2.append(element)
    startToNode[element.start] = element
def checkin(l1, st):
    for el in l1:
        if el.start == st:
            return True
    return False

for element in l2:
    while(not checkin(l2,element.parent)):
        if element.parent == 0:
            break
        else:
            element.parent = startToNode[element.parent].parent
            element.level-=1
            
def maxLevel(l):
    mx = 0
    for e in l:
        if e.level > mx:
            mx = e.level
    return mx

for el in l2:
    if el.parent != 0 and (el.level - startToNode[el.parent].level) >1 :
        el.level-=1

counter = 2
for j in range(1,maxLevel(l2)+1):
    for e in l2:
        if e.level == j:
            e.id = counter
            counter+=1

d={}
for element in l2:
    if element.parent not in d:
        d[element.parent] = [element.id]
    else:
        d[element.parent].append(element.id)
    


adjecencyList = {}

for keys in d:
    if keys == 0:
        adjecencyList[1] = d[keys]
    for ele in l:
        if keys == ele.start:
           adjecencyList[ele.id] = d[keys]



leaves = []
childToParent = {}
for key in adjecencyList:
    for e in adjecencyList[key]:
        childToParent[e] = key
        if e not in adjecencyList:
            leaves.append(e)
print("The control flow paths for this code are: ")
for k in leaves:
    toprint = [k]
    current = k
    while(current in childToParent):
        current = childToParent[current]
        toprint.append(current)

    toprint.reverse()
    
    for node in toprint:
        if node == toprint[-1]:
            print(node)
        else:
            print(node, end = "  ==> ")

        















