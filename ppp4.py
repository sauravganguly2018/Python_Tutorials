# The Next Palindrome
# problem content
# A palindrome is a string which when reversed is equal to itself:
# Examples of palindrome includes 616,mom,676,100001
# You have to take a number as an input from the user. You have to find the next palindrome corresponding
# to that number.Your first input should be 'number of test cases' and then take all the cases asinput from
# the user
#
# Input:
# 3
# 451
# 10
# 2113
#
# Output:
# Next palindrme for 451 is 454
# Next palindrme for 10 is 11
# Next palindrme for 2133 is 2222

n=int(input("Enter the no. of inputs you want to provide : "))
lst=[]
for i in range(n):
    lst.append(int(input(f"Enter number {i+1} : ")))
print(lst)
for i in range(n):
    c=1
    temp=lst[i]+1
    k=lst[i]
    while(c==1):
        sum=0
        temp = lst[i] + 1
        while (temp != 0):
            rem = temp % 10
            sum = 10 * sum + rem
            temp = int(temp / 10)
        if sum==lst[i]+1:
            print(f"The next palindrome of {k} is {sum}")
            c=0
        else:
            lst[i]=lst[i]+1
