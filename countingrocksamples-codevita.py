S, R = input().split(" ")
S,R = int(S), int(R)
samples = input().split(" ")
samples = list(map(int,samples))
count=0
output = []
if len(samples) == S:
    for x in range(R):
        range1,range2 = input().split(" ")
        range1,range2 = int(range1),int(range2)
        for sample in samples:
            int(sample)
            if range1<sample<range2:
                count += 1
        x += 1
        output.append(count)
        count=0
    for x in range(0,len(output)):
        print(output[x],end=" ")
else:
    exit(0)