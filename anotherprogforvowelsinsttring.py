name = input("Enter the string:")
count = 0
for index in range(len(name)):
    if name[index] in "aeiouAEIOU":
        count += 1
print(count)