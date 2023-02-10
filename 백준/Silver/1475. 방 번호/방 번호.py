n = input()
plate = [0]*10
for i in n:
    plate[int(i)] += 1
six_and_nine = (plate[6] + plate[9])//2 + (plate[6] + plate[9])%2
plate[6] = plate[9] = 0
print(max(max(plate), six_and_nine))