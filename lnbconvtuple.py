'''Q10. Convert tuple to list using given string
    ● Take input from the user in the form of tuple
    ● Take another input from the user in the form of string
    ● Convert the tuple to list
    ● Add string to the list after each element
    ● Convert list to tuple again
    ● File name must be lnbconvtuple.py in which you are writing the code
    ● Commit this code on your github link under pythonbasic branch
    Sample Input: (21,37,18), K= “Age”
    Sample output: (21,”Age”,37,”Age”,18,”Age”)'''


# tuple_input = tuple(input("Enter tuple:"))
# print(tuple_input,type(tuple_input))
# str_input = str(input("Enter string: "))
# print(str_input,type(str_input))
# l=list(tuple_input)
# print("Tuple converted to list:",l,type(l))
# l.append(str_input)
# print("Additiion of List and str:",l)
# print("Tuple:",tuple(l))

lst=[]
# u=tuple(input("No.of times:"))
# b=list(u)
s=str(input("Enter str:"))
for i in range(3):
    user=(input("Enter value:"))
    lst.append(user)
    lst.append(s)
# z=tuple(lst)
# print(z,type(z))
print(lst)
#Add
