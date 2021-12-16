# Python Practice Problem 5 (Easy, 10 Points)
# Palindromify the list
#
# You are given a list which contains some numbers. You have to print a list of next palindromes only if the
# number is greater than 10 otherwise you will print that number
#
# Input:
# [1,6,87,43]
#
# Output:
# [1,6,88,44]

n=int(input("Enter the no. of inputs you want to provide : "))
old_lst=[]
for i in range(n):
    old_lst.append(int(input(f"Enter number {i+1} : ")))
lst=old_lst[:]
new_lst=[]
for i in range(n):
    if lst[i]>9:
        c=1
        temp=lst[i]+1
        while(c==1):
            sum=0
            temp = lst[i] + 1
            while (temp != 0):
                rem = temp % 10
                sum = 10 * sum + rem
                temp = int(temp / 10)
            if sum==lst[i]+1:
                new_lst.append(sum)
                c=0
            else:
                lst[i]=lst[i]+1
    else:
        new_lst.append(lst[i])
print(old_lst)
print(new_lst)
