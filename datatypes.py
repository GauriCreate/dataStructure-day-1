####collection of datatypes#####
##mylist=["prashant","ashish","komal","anush","ashish",77,"sandip",60.52,"prashant"]
##print(mylist)
##print(type(mylist))
##print(mylist[0])
##print(mylist[1])
##print(mylist[2])
##print(mylist[-1])
##print(mylist[2:5])
##print(mylist[:5])
##print(mylist[1:])
##print(mylist[1:8:2])
##print(mylist[:])
##print(mylist[::-1])
##mylist[2]="akshay"
##print(mylist)


##if "ankush" in mylist:
##    print("yes prashant is available")
##else:
##    print("prashant is not avialable")

##mylist.append('harsh')
##mylist.append('laxman')
##print(mylist)

##mylist.insert(1,"sanket")
##print(mylist)

##mylist.remove("sandip")
##print(mylist)

##newlist=mylist.copy()
##print(newlist)

##
##mylist=[['gauri','mochemdkar'],['85','56'],[440022,"yyy"]]
# mytuple=("Dipali","Harsha","Rahul","sandip","ankush","rajesh",23,3,15,77,"sandip")
# print(mytuple)
# print(type(mytuple))

# mytuple[2]="sunil"
# print(mytuple)

# init_tuple=()
# print(init_tuple.__len__())

# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a==init_tuple_b)
# print(id(init_tuple_a))
# print(id(init_tuple_b))

# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a + init_tuple_b)

# init_tuple=('python',)*3
# print(type(init_tuple))

# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)

# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))

##print("example of multi dimensional list:")
#print(myligest[0][0])
#print(mylist[0][1])
##print(mylist[1][0])

##print(mylist[2][0])
##p1rint(mylist[2][1])

##list1=["gauri","mochemadkar"]
##print(list1*2)

##list2=[50,25.50,'gauri']
##list2.clear()
##print(list2)

##mylist=[40,30,20,10]
##mylist.sort()
##print(mylist)

##mylist=[40,30,20,10]
##mylist.reverse()
##print(mylist)


##mylist=[40,30,20,10]
##mylist.sort()#reverse=true
##print(mylist)


##mylist=[44,22,77,0,9,88]
##newlist=mylist
##print(id(mylist))
##print(id(newlist))
##mylist[0]="siya"
##print(mylist)
##prnt(newlist)


##arr=[[1,2,3,4],
##     [4,5,6,7],
##     [8,9,10,11],
##     [12,13,14,15]]
##for i in range(0,4):
##    print(arr[i].pop())


##arr=[1,2,3,4,5,6]
##for i in range(1,6):
##    arr[i-1]=arr[i]
##for i in range(0,6):
##    print(arr[i],end="")


##a=[1,2,3,4,5,6,7,8,9]
##a[::2]=10,20,30,40,50,60
##print(a)

##a=[1,2,3,4,5]
##print(a[3:0:-1])

###

##init_tuple_a='1','2'
##init_tuple_b=('3','4')
##print(init_tuple_a+init_tuple_b)

##init_tuple=('python',)*3
##print(type(init_tuple))

##init_tuple=((1,2),)*7
##print(len(init_tuple[3:8]))

# mytuple=("Dipali","Harsha","Rahul","sandip","ankush","rajesh",23,3,15,77,"sandip")
# print(mytuple)
# print(type(mytuple))

# mytuple[2]="sunil"
# print(mytuple)
# init_tuple=()
# print(init_tuple.__len__())

# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a==init_tuple_b)
# print(id(init_tuple_a))
# print(id(init_tuple_b))

# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a + init_tuple_b)

# init_tuple=('python',)*3
# print(type(init_tuple))

# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)

# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))

##names=[4,2,5,6,8,2]
##for i in names:
##    print()

##a=[4,0,2,5,0,1]
##for i in a:
##    if i==0:
##        a.remove(i)
##        a.append(i)
##print(a)

##a = [1, 2, 2, 3, 4, 4, 5]
##newlist=[]
##for i in a:
##    if i not in newlist:
##        newlist.append(i)
##printn(newlist)

##a=[1,2,3]
##b=[2,3,4]
##c=[3,4,5]
##common_elements = set(a).intersection(b).intersection(c)
##print(common_elements)


##n=int(input("enter the size of array:"))
##arr=[]
##for i in range(n):
##      val=int(input("enter the value of array:"))
##      arr.append(val)
##print(arr)val


##n=int(input("enter size of array"))
##arr=[]
##for i in range(n):
##    val=int(input("enter the value of array:"))
##    arr.append(val)
##    sum=0
##print(arr)
##for i in range(n):
##    if i+1 in range(n):
##        sum+=abs(arr[i]-arr[i+1])
##print(sum)    
##

##for i in range(1,5):
##    if i==3:
##        continue
##    print(i)


##for i,j in zip(range(1,6),range(5,0,-1)):
##    if i==3 and j==3:
##       continue
##    print(i,"",j)
####    
##    
##a="siya*is*a*good*programmer"
##a=a.replace("*","")
##output="*****"+a.lower()
##print(output)


##a=50
##b=30
##c=20
##d=10
##print((a+b)*c/d)
##print((a-b)*c/d)
##print(a+(b*c)/d)




##x=['a','b','c']
##y=['a','b','c']
##z=[1,2,3,4]
##print(x==y)
##print(x==z)
##print(x!=z)


##from collections import Counter
##
##def are_anagrams(str1, str2):
##    str1 = str1.replace(" ", "").lower()
##    str2 = str2.replace(" ", "").lower()
##    return Counter(str1) == Counter(str2)
##
### Test the function
##str1 = "Listen"
##str2 = "Silent"
##print(are_anagrams(str1, str2))  # Output: True


#import re

#def count_words(s):
#    return len(re.findall(r'\b\w+\b', s))

# Test the function
#s = "Hello world, this is Python!"
#print(count_words(s))  # Output: 5
