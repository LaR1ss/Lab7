sum = 0
a = int(input())
for number in range(1, 101):
    if number % a == 0:
        sum += number
print(sum)
