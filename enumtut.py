lst=["aloo","bhindi","onion","tomato"]
i=1
# for item in lst:
#     if i%2 != 0:
#         print(f"saurav please buy {item}")
#     i+=1

for index,item in enumerate(lst):
    if index%2==0:
        print(f"saurav please buy {item}")