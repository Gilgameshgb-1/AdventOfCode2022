with open('script1.txt') as f:
    lines = f.readlines()

sum = 0
max = 9999

for x in lines:
  if x != "\n":
    q = x.strip()
    sum += int(q)
  else:
    sum = 0
  if sum > max:
    max = sum

print(max)