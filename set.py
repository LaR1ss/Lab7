thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
for x in thisset:
  print(x)
print("banana" in thisset)
x = thisset.pop()

print(x)

print(thisset)