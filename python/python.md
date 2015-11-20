p:ython learning
===============

a,b,c = 10,15,2
a
>> 10
b
>> 15

(tuples) = cannot be updated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
[list] = can be updated
~~~~~~~~~~~~~~~~~~~~~~~
<list_name>.append(item)
  
{dict} = can updated
~~~~~~~~~~~~~~~~~~~~

dictionary = {}
dictionary["new key"] = "some new entry" # add new dictionary entry
dictionary["dictionary_within_a_dictionary"] = {} # this is required by python
dictionary["dictionary_within_a_dictionary"]["sub_dict"] = {"other" : "dictionary"}
print (dictionary)

star programing
===============
    for i in range(1,6):  
        for j in range (1,i+1):  
            print i,  
        print  
        
o/p
~~~
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  

    for i in range (1,6):  
        for j in range (5,i-1,-1):  
            print "*",  
        print  
        
o/p
~~~
* * * * *  
* * * *  
* * *  
* *  
*  

if(condition): elif eles 
for <variable> in <sequence>:  xrange, range
while <expression>:break,continue
pass will skip! 

"\t" tap in the programe
Replication operation *

slice notation
~~~~~~~~~~~~~~

    >>> str="sambath"  
    >>> str[0:7]  
    'sambath'  
    >>> str[0:3]  
    'sam'  
    >>> str[2:5]  
    'mba'  
    >>> str[:7]  
    'sambath'  
    >>> str[3:]  
    'bath'  

input form keyboard
~~~~~~~~~~~~~~~~~~~

    n=input("Enter your expression ");  
    print "The evaluated expression is ", n  
    
    Enter your expression 10*2  
    The evaluated expression is  20  

oop
~~~
__init__ in the constructor of the class

if we print the object after the constructor is created it will call the __str__ and in default it will have the address location


