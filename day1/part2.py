with open('script1.txt') as f:
    lines = f.readlines()

sum = 0
max = [0, 0, 0]

for x in lines:
  if x != "\n":
    q = x.strip()
    sum += int(q)
  else:
    max.sort()
    if(max[0] <= sum): max[0] = sum
    sum = 0
   
print(max)

finSum = 0

for elem in max:
  finSum += elem

print(finSum)

# a value of 0 must be added to the end of the given input