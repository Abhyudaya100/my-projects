T = int(input())
x=0
results = []
answer = 0
for x in range(0,T):
    output = []
    time = []
    total = 0
    candies = []
    sum = 0
    N = int(input())
    candies = input().split(" ")
    candies = list(map(int, candies))
    if len(candies) == N:
        for candy in range(0,len(candies)):
            sum = sum + candies[candy]
            candy +=1
            time.append(sum)
        for z in range(1, len(time)):
            total = total + time[z]
            z+=1
        output.append(total)
    results.append(*output)
    x += 1
for result in results:
    answer = answer + result
print(answer)