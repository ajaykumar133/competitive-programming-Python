''' You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
arr_house =[]

arr_odd = []
arr_even = []

houses = int(input("Enter the number of houses in street:"))

for i in range(0,houses):
    money = int(input("Enter the money in house no. "+str(i+1)+" :"))
    arr_house.append(money)


for i in range(0,houses):
    if(i%2 == 0):
        #money_odd = int(input("Enter the money in house no. "+str(i+1)+" :"))
        #arr_odd.append(money_odd)
        arr_odd.append(arr_house[i])
    else:
        # money_even = int(input("Enter the money in house no. "+str(i+1)+" :"))
        # arr_even.append(money_even)
        arr_even.append(arr_house[i])

total_odd = 0
total_even = 0
total_odd = sum(arr_odd)
total_even = sum(arr_even)

print(arr_house)

if(total_odd<total_even):
    print("\nRobber will go to even number house's and will get money :"+str(total_even))
else:
    print("\nRobber will go to odd number house's and will get money :"+str(total_odd))

