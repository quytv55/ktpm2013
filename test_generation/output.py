import unittest
import itertools
import collections
import unittest
import inspect
from input import main

#Buoc1: Xu ly de lay cac mien gia tri trong docstring.

#Ham swap

def swap(a,b):
    temp=b;
    b=a;
    a=temp;

#ham sap xep

def sort(minlist,maxlist):
    minlist=[]
    maxlist=[]
    for i in range(len(minlist)):
        for j in range(len(minlist)-1,i,-1):
            if(minlist[j]<minlist[j-1]):
                swap(minlist[j],minlist[j-1])
                swap(maxlist[j],maxlist[j-1])
                           
#Kiem tra du lieu.

def check_value(a):
    t=[]
    k=[]
    for i in range(len(arr)):
        t.append(len(t[i]))
        if(t[i]%2!=0) or (t[i]==0) or len(arr)>10:
            raise Exception("wrong input")
        else:
            for j in range(len(arr[i]),2):
                k.extend(range(arr[i][j],arr[i][j+1]+1))
            t.append(k)        
    return True

def read_String(self):
    variable,doc=self.split(":")
    doc=doc.strip()
    a=doc.replace("][",";").replace("]","").replace("[","").split(";")

    minlist=[]
    maxlist=[]
    i=0
    t=0
    for i in len(a):
        minlist[t]=int(a[i])
        maxlist[t]=int(a[i+1])
        i=i+2
        t+t+2
    dem=0
    sort(minlist,maxlist)
    for i in range(0, len(minlist)):
        if minlist[i+1]<= maxlist[i]:
            dem=dem+1
    if dem>0:
        raise Exception("Wrong input")
    else:
        b=sorted(a, key=int)
        array=[]
        c=int(0)
        i=0
        while True:
            array.append((int(b[c])+int(b[c+1]))/2)
            c=c+2
            if c==len(b):
                break
        return array
class Test(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
doc = inspect.getdoc(main)
docs = doc.splitlines()
def creat_test(docs):
    Array=[]
    i=0
    for j in docs:
        Array.append(read_String(j))
        i=i+1
    return list(itertools.product(*Array))
a=creat_test(docs)
j=0
if__name__=='__main__'
for i in a:
    test_name='test %s' % str(j)
    test=test_generator(i)
    setattr(Test, test_name, test)
    j=j+1
unittest.main()
    
