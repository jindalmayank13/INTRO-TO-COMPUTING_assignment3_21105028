      #Question:1


print("\nQ.1")
#Taking Input
string_name=str(input("Enter the string:"))
#Taking each string as element in list
list1=string_name.split()
#empty list which will contain lowercase words only
list_l=[]
#converting each element of list1 to lowercase and inserting it to list_l
for e in list1:
    lower_e=e.lower()
    list_l.append(lower_e)
#converting list_l to set to avoid repeatation
set1=set(list_l)
dic={}
#forming a dictionary with key string and value string count
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
#Code when string contains only one word
dic2={}       #empty dictionary
set2={1,2}
set2.clear()  #empty set2
list2=[]      #empty list2
#Condition when only one word is detected in string
if len(list1)==1:
    #Code for counting letter
    #Adding all letters of input string into  list2
    for elements in string_name:
        list2.append(elements)
    #lowering elements of list2 to lowercase and adding to set2
    for el in list2:
        set2.add(el.lower())
    #lowering main input string to lowercase
    string_l=string_name.lower()
    for elem in set2:
        #Adding count values to dic2
        dic2.update({elem:string_l.count(elem)})
    # printing the dic2 containing 'letter':'letter count'
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)
#printing the dic when string contains more than one word
else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic)      #dic contains 'word':'word count'


           #Question:2


print("\nQ.2")
print("Enter Date below to get date of next day.\n")
#Defining leap year function
def leapyear(x):
    #for leap year this condition must be True
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False
#Taking input day,month,year
day=int(input("Enter Day [1-31]:"))
month=int(input("Enter Month [1-12]:"))
year=int(input("Enter Year [1800-2025]:"))
#Applying condition1 for dates out of range
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

#Applying condition2 when day entered does not present in that month
month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days
#for day entered 31 does not present in that month
c1a= day==31 and (month in month_30)
#for day entered greater than 29 in month february i.e 2
c1b= day>29  and month==2
#for day entered greater than 28 in february in non leapyear
c1c= day==29 and (not leapyear(year)) and month==2
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True
#printing error when date entered is not correct
if c1a:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1b:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1c:
    print(f"\nError\n{day} day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")

#Code when date entered is correct
if condition1==True and condition2==True :
    month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
    month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days
    #For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1
    #For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1
    #for february month i.e. month 2
    elif month == 2:
        # If year is leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1
        # If year is not leap year
        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1
    # Printing Next date
    print(f"\nNext Date in format Day/Month/Year is: {day}/{month}/{year}")


#Question:3


print("\nQ.3")
#Taking input list
list1=list(map(int,input("Enter the numbers separated by space:").split()))
#Empty list
list2=[]
#Forming square and storing in tuple
for e in list1:
    t=(e,e*e)
    list2.append(t)
#Printing the final result
print("\nList containing (n,n^2) is shown below:")
print(list2)


            #Question:4


print("\nQ.4")
#Taking grade point input
grade_point=int(input("Enter grade points:"))
#Forming a dictionary of statements
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_point<=10:
    #Taking required statement from dictionary
    statement=dic.get(grade_point)
    #printing final result
    print(statement)
else:
    #printing error message when grade is out of range
    print("\nError\nPlease enter grade in range [4,10]")


        #Question:5


print("\nQ.5")
print("The pattern is printed below:\n")
# Letters to be printed
abcd = "ABCDEFGHIJK"
# forming a list of letters
list_abcd = []
for i in abcd:
    list_abcd.append(i)
# Applying while loop to print only required rows
k = 1
while k <= 6:
    # printing 1st row intially when k=1
    for el in list_abcd:
        print(el, end="")
    # forming second row elements to be printed
    list_abcd.pop(len(list_abcd) - 1)  # removng las element of list
    list_abcd.pop(len(list_abcd) - 1)  # removing last element of list
    list_abcd.insert(0, " ")  # insertind space
    print()  # changing line using print()
    k = k + 1


        #Question:6


print("\nQ.6")
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
#List containing Y or N
liste=["Y","y","n","N"]
#Main code
while repeat=="Y" or repeat=="y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'(will be helpful while sorting)
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")


              #Question 7


print("\nQ.7")
#Taking input
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
#printing error message when N<=0
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {two_decimal}")


        #Question:8


print("\nQ.8")
#Given Sets
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
#printing the given sets
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)
#b
#set1 Union set2
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

#set1 Union set2 Union set3
set_uf=set_u1.union(set3)

#set1 intersection set2
set_i1=set1.intersection(set2)

#set1 intersection set2 intersection set3
set_if=set_i1.intersection(set3)

#set1 intersection set2
set_12=set1.intersection(set2)

#set2 intersection set3
set_23=set2.intersection(set3)

#set3 intersection set1
set_13=set1.intersection(set3)

#final required set
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)
#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)
#d
#forming a set containing values from 1 to 10
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
#printing final set
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)
#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)




















