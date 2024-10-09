# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if(n%2==0):
        if(n>=2 and n<=5):
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# Write a function
def is_leap(year):
    leap = False
    
    if(year%4==0):
        if(year%100)==0:
            if(year%400==0):
                leap=True
        else:
            leap=True
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    z=''
    for i in range(1,n+1):
        z=z+str(i)
    print(z)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listX=[i for i in range(0,x+1)]
    listY=[j for j in range(0,y+1)]
    listZ=[k for k in range(0,z+1)]
    ListPerm=[[i,j,k] for i in listX for j in listY for k in listZ]
    FinalList=[i for i in ListPerm if sum(i)!=n]
    print(FinalList)  

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listArr=list(arr)
    NoMaxList=[i for i in listArr if i!=max(listArr)]
    print(max(NoMaxList))
    #Finding the runner-up score by removing the maximum values from the list

# Nested Lists
if __name__ == '__main__':
    listScore=[]
    nestedList=[]
    for _ in range(int(input())):
        name = input()
        #listName.append(name)
        score = float(input())
        nestedList.append([name,score])
        listScore.append(score)
   
withoutLowestGradeListScore=[i for i in listScore if i!=min(listScore)]     
withoutLowestGradeList=[i for i in nestedList if i[1]!=min(listScore)]
SecondLowestGradeList=[i for i in withoutLowestGradeList if i[1]==min(withoutLowestGradeListScore)]
SecondLowestGradeList.sort(key=lambda a:a[0])
for i in SecondLowestGradeList:
    print(i[0])

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
listName=list(student_marks.keys())
listAvgScore=["{:.2f}".format(sum(i)/len(i)) for i in student_marks.values()]
dictNameAvgScore = dict(zip(listName, listAvgScore))
print(dictNameAvgScore[query_name])

# Lists
if __name__ == '__main__':
    N = int(input())
    #For this exercise i viewed HackerRank's answers since the requests were not clear to me, then i implemented my own solution.
    list=[]
    
    for i in range(0,N):
        Command=str(input()).split()
        if Command[0]=="insert":
            list.insert(int(Command[1]),int(Command[2]))
        elif Command[0]=="print":
            print(list)
        elif Command[0]=="remove":
            list.remove(int(Command[1]))
        elif Command[0]=="append":
            list.append(int(Command[1]))
        elif Command[0]=="sort":
            list.sort()
        elif Command[0]=="pop":
            list.pop()
        elif Command[0]=="reverse":
            list.reverse()
            

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# String Split and Join

def split_and_join(line):
    return "-".join(line.split(" "))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    print( "Hello "+first+" "+last+"! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string

# Find a string
def count_substring(string, sub_string):
    count=0
    
    for i in range (0,len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)]==sub_string):
            count=count+1
            
    return count

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

# String Validators
if __name__ == '__main__':
    s = input()
    print(True in [x.isalnum() for x in s])
    print(True in [x.isalpha() for x in s])
    print(True in [x.isdigit() for x in s])
    print(True in [x.islower() for x in s])
    print(True in [x.isupper() for x in s])

# Text Wrap

def wrap(string, max_width):
    c=0
    listString=[]
    while c<len(string):
        
        if(c+max_width>=len(string)):
            listString.append(string[c:len(string)])
            c=len(string)
        else:
            listString.append(string[c:c+max_width])
            c=c+max_width
        
    return "\n".join(listString)

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=list(map(int,input().split()))
matList=[]
certer="WELCOME".center(N[1],'-')
[matList.append((".|."*i).center(N[1],'-')) for i  in range(1,N[0],2)] #Top part
downsideList=list(reversed(matList)) #Bottom part
matList.append("WELCOME".center(N[1],'-')) #Center part
matList=matList+downsideList
print("\n".join(matList))

# Capitalize!

# Complete the solve function below.
def solve(s):
    newString=''
    for i in range(0,len(s)):       
        if (i==0 or s[i-1]==' ') and s[i].isalpha():
            newString=newString+s[i].capitalize()
        else:
            newString=newString+s[i]
    return newString

# String Formatting
def print_formatted(number):
    lenBin=len(str(bin(number)).lstrip("0b").rstrip("L"))
    for i in range (1,number+1):
        print(str(i).rjust(lenBin,' ')+str(oct(i)).lstrip("0o").rstrip("L").rjust(lenBin+1,' ')+str(hex(i)).lstrip("0x").rstrip("L").upper().rjust(lenBin+1,' ')+str(bin(i)).lstrip("0b").rstrip("L").rjust(lenBin+1,' '))

# Alphabet Rangoli
def print_rangoli(size):
    listAlph=list(map(chr, range(97, 123)))
    listSecondHalf=[]
    for i in range(0,size):
        string=''
        for j in range(0,size):
            if(j==0):
                string=listAlph[i]
            else:
                if(j+i<size):
                    string=string.center(len(string)+2,'-')
                    string=string.center(len(string)+2,listAlph[j+i])
                else:
                    string=string.center(len(string)+4,'-')
        listSecondHalf.append(string)
    listFinal=list(reversed(listSecondHalf[1:]))+listSecondHalf
    print("\n".join(listFinal))

# Introduction to Sets
def average(array):
    aSet=set(array)
    lenSet=len(aSet)
    return round(sum(aSet)/lenSet, 3)

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
listm=list(map (int ,input().split()))
a=set(listm)
n=int(input())
listn=list(map (int ,input().split()))
b=set(listn)
dif1=a.difference(b)
dif2=b.difference(a)
finalSet=dif1.union(dif2)
finalList=list(finalSet)
finalList.sort()
[print(i) for i in finalList]

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
listN=list(map(int,input().split()))
listA=list(map(int,input().split()))
setA=set(listA)
listB=list(map(int,input().split()))
setB=set(listB)
scoreA=0
scoreB=0
for i in listN:
    if i in setA:
        scoreA+=1
    elif i in setB:
        scoreB+=1
print(scoreA-scoreB)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
listN=[]
[listN.append(input()) for i in range(0,n)]
setN=set()
[setN.add(i) for i in listN]
print(len(setN))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
numCommand=int(input())
for i in range(0,numCommand):
    command=str(input()).split()
    if command[0]=="pop":
        s.pop()
    elif command[0]=="remove":
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.discard(int(command[1]))
print(sum(s))   

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setN=set(map(int,input().split()))
b=int(input())
setB=set(map(int,input().split()))
finalSet=setN.union(setB)
print(len(finalSet))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setN=set(map(int,input().split()))
b=int(input())
setB=set(map(int,input().split()))
finalSet=setN.intersection(setB)
print(len(finalSet))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setN=set(map(int,input().split()))
b=int(input())
setB=set(map(int,input().split()))
finalSet=setN.difference(setB)
print(len(finalSet))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setN=set(map(int,input().split()))
b=int(input())
setB=set(map(int,input().split()))
finalSet=setN.symmetric_difference(setB)
print(len(finalSet))

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
setA=set(map(int,input().split()))
n=int(input())
for i in range(0,n):
    command=input().split()
    if(command[0]=="update"):
        setA.update(set(map(int,input().split())))
    elif(command[0]=="intersection_update"):
        setA.intersection_update(set(map(int,input().split())))
    elif(command[0]=="difference_update"):
        setA.difference_update(set(map(int,input().split())))
    elif(command[0]=="symmetric_difference_update"):
        setA.symmetric_difference_update(set(map(int,input().split())))
print(sum(setA))

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
listRoom=list(map(int,input().split()))
setRoom=set(listRoom)
for x in setRoom:
    count=0
    captain=x
    for i in listRoom:
        if x==i:
            count+=1
        if count>1:
            break
    if(count==1):
        break
print(captain)
            
        

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(0,t):
    nA=int(input())
    setA=set(map(int, input().split()))
    nB=int(input())
    setB=set(map(int, input().split()))
    print(setA.issubset(setB))

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int, input().split()))
nB=int(input())
strictSuperSet=True
for i in range(0,nB):
    setB=set(map(int, input().split()))
    if(not(setB.issubset(setA) and len(setA)>len(setB))):
        strictSuperSet=False
    if not strictSuperSet:
        break
print(strictSuperSet)

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
listSize=list(map(int,input().split()))
n=int(input())
earning=0
for i in range(0,n):
    command=input().split()
    if(int(command[0]) in listSize):
        listSize.remove(int(command[0]))
        earning+=int(command[1])
print(earning)

# Merge the Tools!
def merge_the_tools(string, k):
    t=[string[i:i+k] for i in range(0, len(string), k)]
    u=[]
    stringU=''
    for i in t:
        for y in i:
            if str(y) not in stringU:
                stringU=stringU+str(y)
        print(stringU)
        stringU=''       
        

# The Minion Game
def minion_game(string):
    vowels = "AEIOU"
    consonants = "".join([chr(i) for i in range(65, 91) if chr(i) not in vowels])
    scoreStuart=0
    scoreKevin=0
    
    for i in range(0,len(string)):
        if string[i] in vowels:
                scoreKevin+=len(string)-i
        else:
                scoreStuart+=len(string)-i
    if scoreStuart<scoreKevin:
        print("Kevin "+str(scoreKevin))
    elif scoreStuart>scoreKevin:
        print("Stuart "+str(scoreStuart))
    else:
        print("Draw")
    print()

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m=input().split()
listN=[]
listM=[]
[listN.append(input()) for i in range(0,int(n))]
dictN=defaultdict(list)
[dictN[listN[i]].append(i+1) for i in range(0,len(listN))]
    
[listM.append(input()) for i in range(0,int(m))]
for i in listM:
    if i in dictN.keys():
        print(" ".join(map(str,dictN[i])))
    else:
        print("-1")
        
        d1 = defaultdict(list)

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
#I viewed HackerRank's discussions for this question
from collections import namedtuple
n=int(input())
count=0
Spreadsheet=namedtuple("Spreadsheet",input().split())
for i in range(0,n):
    ss=Spreadsheet(*input().split())
    count+=int(ss.MARKS)
print(round(count/n,2))

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(list(reversed(arr)),dtype=float)

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
ordered_dictionary = OrderedDict()
for i in range(n):
    listInput=input().split()
    item_name=" ".join(listInput[:-1])
    price=int(listInput[-1])
    if(item_name in ordered_dictionary):
        ordered_dictionary[item_name]=ordered_dictionary[item_name]+price
    else:
        ordered_dictionary[item_name]=price
[print(key+" "+str(value))for key, value in ordered_dictionary.items()]

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
ordered_dictionary = OrderedDict()
for i in range(n):
    word=input()
    if(word in ordered_dictionary):
        ordered_dictionary[word]=ordered_dictionary[word]+1
    else:
        ordered_dictionary[word]=1
print(len(ordered_dictionary))
print(" ".join(map(str,ordered_dictionary.values())))

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n=int(input())
for _ in range(n):   
    command=str(input()).split()
    if command[0]=="popleft":
        d.popleft()
    elif command[0]=="pop":
        d.pop()
    elif command[0]=="append":
        d.append(command[1])
    elif command[0]=="appendleft":
        d.appendleft(command[1])
print(" ".join(d))

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
from collections import OrderedDict
if __name__ == '__main__':
    s = input()
    [print(key+" "+str(value)) for key,value in OrderedDict(sorted(OrderedDict(Counter(s)).items(),key=lambda item: (item[1], -ord(item[0])),reverse=reversed)[:3]).items()]

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t=int(input())
for i in range(t):
    n=int(input())
    dequeN=deque(map(int,input().split()))
    lenDequeN=len(dequeN)
    listPile=[]
    while len(listPile)<lenDequeN:
        if(len(dequeN)>1):
            popLeft=dequeN.popleft()
            popRight=dequeN.pop()
            if(popLeft>=popRight):
                greater=popLeft
                dequeN.append(popRight)
            else:
                greater=popRight
                dequeN.appendleft(popLeft)
            if( len(listPile)==0 or greater<=listPile[-1]):
                listPile.append(greater)
            else:
                break
        elif(len(dequeN)>0):
            pop=dequeN.pop()
            if(len(listPile)==0 or pop<=listPile[-1]):
                listPile.append(pop)
            else:
                break
    if(len(listPile)==lenDequeN):
        print("Yes")
    else:
        print("No")    

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month,day,year=map(int,input().split())
dayName = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(dayName[ calendar.weekday(year, month, day)])

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime
    timeFormat = '%a %d %b %Y %H:%M:%S %z'
    datetimeT1 = datetime.strptime(t1, timeFormat)
    datetimeT2 = datetime.strptime(t2, timeFormat)
    timeDifference = datetimeT1 - datetimeT2
    return(str(int(abs(timeDifference.total_seconds()))))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError as e:
        print ("Error Code:",e)

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x=input().split()
listN=[]
for i in range(int(x)):
    listN.append(map(float,input().split()))
print("\n".join(map(str,[sum(i)/int(x) for i in zip(*listN)])))

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr.sort(key=lambda i:i[k])
    [print(*i) for i in arr]

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
print("".join(
sorted([i for i in s if i.islower()])+
sorted([i for i in s if i.isupper()])+
sorted([i for i in s if i.isdigit() and int(i)%2!=0])+
sorted([i for i in s if i.isdigit() and int(i)%2==0])))

# Map and Lambda Function
cube = lambda x: x*x*x# complete the lambda function 
def fibonacci(n):
    
    if(n==0):
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        listF=[0,1]
        [listF.append(listF[len(listF)-1]+listF[len(listF)-2]) for _ in range(2,n)]
        return listF
    # return a list of fibonacci numbers

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t=int(input())
pattern = r'^[-+]?[0-9]*\.[0-9]+$'
for _ in range(t):
    print(re.fullmatch(pattern, input()) is not None)

# Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
m = re.search(r'([a-zA-Z0-9])\1',s)
if m is None:
    print(-1)
else:
    print(m.group(1))

# Concatenate
import numpy
n,m,p=input().split()
array1=numpy.array([list(map(int,input().split()) )for _ in range(int(n))])
array2=numpy.array([list(map(int,input().split())) for _ in range(int(m))])
print(numpy.concatenate((array1,array2),axis=0))

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
pattern=r'(?i)(?=[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})[qwrtypsdfghjklzxcvbnm])'
match=re.findall(pattern,s)
if(len(match)==0):
    print("-1")
else:
    print("\n".join(match))

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
#I viewed HackerRank's solution for this exercise
s=input()
k=input()
import re
m =  list(re.finditer(f"(?=({k}))",s))
if(len(m)>0):
     [print((i.start(), i.end() + len(k)-1)) for i in m]
else:
    print((-1,-1))

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def sub(text):
    newText= str(text.group(0))
    if newText.strip()=='||':
        return "or"
    else:
        return "and"
n=int(input())
text=""
for i in range(n):
    text=text+input()+"\n"
pattern=r"(?<!^)(?<= )(&&|\|\|)(?= )(?!$)"
print(re.sub(pattern,sub,text))

# Shape and Reshape
import numpy

arr=list(map(int,input().split()))
npArray = numpy.array(arr)
npArray.shape=(3, 3)
print(npArray)

# Transpose and Flatten
import numpy

n,m=input().split()
listN=[]
for i in range(int(n)):
   listM= list(map(int,input().split()))
   listN.append(listM)
print(numpy.transpose(listN))
listN=numpy.array(listN)
print(listN.flatten())

# Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# Do not delete 'r'.

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern="^[7-9][0-9]{9}$"
def printMsg(msg):
    if msg:
        print("YES")
    else:
        print("NO")
for _ in range(n):
    printMsg(bool(re.match(pattern, input())))

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern=r"^[a-zA-Z][a-zA-Z0-9_.-]*[@][a-zA-Z]+[.][a-zA-Z]{1,3}$"
for i in range(n):
    listInput=input()
    mail=listInput.split()[-1]
    if(bool(re.match(pattern, mail[1:-1]))):
        print(listInput)
    

# Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
patternValue=r"(:.*;)"
patternHex="(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})"
text=""
for _ in range(n):
    text=text+input()+"\n"
match=re.findall(patternValue,text)
if(len(match)>0):
    matchHex=re.findall(patternHex,"\n".join(match))
    if(len(matchHex)>0):
        print("\n".join(matchHex))

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if attrs:
            for i in attrs:
                if i[1] is not None:
                    print(f'-> {i[0]} > {i[1]}')
                else:
                    print(f'-> {i[0]} > None')
            
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if attrs:
            for i in attrs:
                if i[1] is not None:
                    print(f'-> {i[0]} > {i[1]}')
                else:
                    print(f'-> {i[0]} > None')
            
        
n=int(input())
text=""
for i in range(n):
    text=text+input()
parser = MyHTMLParser()
parser.feed(text)



# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        text=data.split("\n")
        if(len(text)>1):
            print (">>> Multi-line Comment\n"+"\n".join(text))
        else:
            print(">>> Single-line Comment\n"+"\n".join(text))
    def handle_data(self, data):
        if(data!='\n'):
            print (">>> Data\n"+data)
          
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
n=int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if attrs:
            print(tag)
            for i in attrs:
                if i[1] is not None:
                    print(f'-> {i[0]} > {i[1]}')
        else:
            print(tag)
            
text=""
for i in range(n):
    text=text+input()
parser = MyHTMLParser()
parser.feed(text)



# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    i=input()
    countUpper=sum([x.isupper() for x in i])
    countDigit=sum([x.isdigit() for x in i])
    isAlpha=i.isalnum()
    tenNoRepeatChar=len(set(i))==10
    if(countUpper>=2 and countDigit>=3 and isAlpha and tenNoRepeatChar):
        print("Valid")
    else:
        print("Invalid")
    

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern=r"^(?!.*(\d)(?:-?\1){3})[456]\d{3}(-?\d{4}){3}$"
def printMsg(msg):
    if msg:
        print("Valid")
    else:
        print("Invalid")
for _ in range(n):
    printMsg(bool(re.match(pattern, input())))

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?=\d\1))"	# Do not delete 'r'.

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
text=""
for i in range(m):
    for j in matrix:
        text=text+j[i]
pattern=r"(?<=[a-zA-Z0-9])[! @#$%&]+(?=[a-zA-Z0-9])"
print(re.sub(pattern," ",text))

# Zeros and Ones
import numpy

n=input().split()
print(numpy.zeros(tuple(map(int,n)), dtype = int))
print(numpy.ones(tuple(map(int,n)), dtype = int))

# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
print(numpy.eye(n,m))


# XML 1 - Find the Score

def get_attr_number(node):
    count=len(node.attrib)
    for child in node:
        count += get_attr_number(child)
    return count

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if maxdepth<=level+1:
        maxdepth=level+1
    
    for child in elem:
        depth(child,level+1)

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        newList=[]
        for i in l:
            if len(i)==12:
                newList.append("+"+i)
            elif len(i)==11:
                newList.append("+91"+i[1:])
            elif len(i)==10:
                newList.append("+91"+i)
            else:
                newList.append(i)
        for i in range(0,len(newList)):
            newList[i]=newList[i][0:3]+" "+newList[i][3:8]+" "+newList[i][8:13]
        f(newList)    
    return fun

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        listPeople=[]
        [listPeople.append(f(i)) for i in sorted(people,key=lambda item:int(item[-2]))]            
        return listPeople
    return inner

# Array Mathematics
import numpy

a,b=map(int,input().split())
listA=numpy.array([list(map(int,input().split())) for _ in range(a)] )
listB=numpy.array([list(map(int,input().split())) for _ in range(a)])
print(numpy.add(listA,listB))
print(numpy.subtract(listA,listB))
print(numpy.multiply(listA,listB))
print(numpy.floor_divide(listA,listB))
print(numpy.mod(listA,listB))
print(numpy.power(listA,listB))

# Floor, Ceil and Rint
import numpy

numpy.set_printoptions(legacy='1.13')
a=numpy.array(list(map(float,input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

# Sum and Prod
import numpy

n,m=map(int,input().split())
listN=numpy.array([list(map(int,input().split())) for _ in range(n)] )
print(numpy.prod(numpy.sum(listN, axis = 0)))

# Min and Max
import numpy

n,m=map(int,input().split())
listN=numpy.array([list(map(int,input().split())) for _ in range(n)] )
print(numpy.max(numpy.min(listN, axis = 1)))

# Mean, Var, and Std
import numpy
#I viewed this exercise's answer because there might be a mistake in the expeceted Output
n,m=map(int,input().split())
listN=numpy.array([list(map(int,input().split())) for _ in range(n)] )
print(numpy.mean(listN,axis=1))
print(numpy.var(listN,axis=0))
print(round(numpy.std(listN),11))

# Dot and Cross
import numpy

n=int(input())
listA=numpy.array([list(map(int,input().split())) for _ in range(n)])
listB=numpy.array([list(map(int,input().split())) for _ in range(n)])
print(numpy.dot(listA,listB))

# Inner and Outer
import numpy

listA=numpy.array(list(map(int,input().split())))
listB=numpy.array(list(map(int,input().split())))
print(numpy.inner(listA,listB))
print(numpy.outer(listA,listB))

# Polynomials
import numpy

p=list(map(float,input().split()))
x=int(input())
listP=numpy.array(p)
print(numpy.polyval(p,x))

# Linear Algebra
import numpy

n=int(input())
listA=numpy.array([list(map(float,input().split())) for _ in range(n)])
print(round(numpy.linalg.det(listA),2))

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    highest=max(candles)
    return sum([1 for i in candles if i==highest])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    if((x2>x1 and v2>=v1) or (x1>x2 and x1>=x2)):
        return "NO"
    elif (max(x1,x2)-min(x1,x2)) % (max(v1,v2)-min(v1,v2))==0:
        return "YES"
    else: 
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    count=0
    liked=0
    shared=5
    for i in range(1,n+1):
        liked=shared//2
        shared=liked*3        
        count=count+liked
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    p=str(sum([int(i)*k for i in n]))
    while len(p)>1:
        p= str(sum([int(i) for i in p]))
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    newValue=arr[-1]
    for i in range(n-1,-1,-1):
        if(i==0):
            arr[0]=newValue
            print(" ".join(map(str,arr)))
        elif(arr[i-1]<newValue):
            arr[i]=newValue
            print(" ".join(map(str,arr)))
            break
        else:
            arr[i]=arr[i-1]
            print(" ".join(map(str,arr)))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    for i in range(n):
        for j in range(i):
            if arr[i]<arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
        if i>0:
            print(" ".join(map(str,arr))) 
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

