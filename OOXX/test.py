row = [{1:0, 2:0} for _ in range(3)]
row[2][1] += 1


for i in row:
    for j in i:
        print(i[j])
    # print(i[1])

# print(row[2][1])