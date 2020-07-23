f = open("input.txt", "r")
lines = f.readlines()
digit = ''.join([line.strip() for line in lines])
f.close()

digit_arr = []
count = 0
total = 0
running_total = 0

for i in digit:
    digit_arr.append(i)

for i in digit_arr:
    if count != 14:
        if running_total > 0:
            running_total = running_total * int(i)
        else:
            running_total += int(i)
        print(running_total)
    if running_total > total:
        total = running_total
    if count == 14:
        count = 0
        running_total = 0
    count += 1
print(total)