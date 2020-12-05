def get_row_column(input):
    row = None
    column = None
    left = 0
    right = 128
    for i in range(7):
        if input[i]=='B':
            left=int((left+right+1)/2)
        else:
            right=int((left+right+1)/2)-1
    row  = left

    left = 0
    right = 7
    for i in range(7,10):
        if input[i]=='R':
            left=int((left+right+1)/2)
        else:
            right=int((left+right+1)/2)-1
    column = left
    return row, column


def get_id(row,column):
    return row*8+column


file = open("input.txt")
tickets = file.readlines()


occupied = [0]*1024
max = 0
for i in tickets:
    row , column = get_row_column(i)
    if get_id(row,column) > max:
        max = get_id(row,column)
    occupied[get_id(row,column)]=1

for i in range(1023):
    if occupied[i]==0:
        if i>=40 and i<=980:
            print(i)


