'''Q 1) Take User input and process
    # ● Take 5 integer input from the user.
    # ● Remove all numbers less than 9.
    # ● Calculate the sum of remaining numbers
    # ● File name must be lnbsum.py in which you are writing code
    # ● Commit this code on your github link under pythonbasic branch'''

list = []
for i in range(5):
    user = int(input("Enter a integer number: "))
    if(user>=9):
        list.append(user)
print("Sum of greater than 9 numbers: ",sum(list))
