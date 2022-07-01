nums = []
add = 0
avg = 0

print("Enter the numbers")
for i in range(10):
    num = int(input())
    nums.append(num)

for num in nums:
    add = add+num

avg = add/10
k = str(add)
m = str(avg)
print("Sum=" + k)
print("Average=" + m)

