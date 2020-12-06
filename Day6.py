def string_2_number(input):
    result = 0;
    check = [0] * 26
    for i in input:

        if i != '\n' and check[ord(i)-ord('a')] == 0:
            result += 1 << (ord(i)-ord('a'))
            check[ord(i) - ord('a')] = 1
    return result

def count_1_bits(x):
    result = 0
    while x:
        if x%2==1:
            result+=1
        x = x >> 1
    return result

def task_1(x):
    result = 0
    for i in x:
        result |= i
    return count_1_bits(result)

def task_2(x):
    result = 0x3FFFFFF

    for i in x:
        result &= i
    return count_1_bits(result)

file = open("input.txt")

input = file.readlines()
file.close()

T1_result = 0
T2_result = 0

answers = []

for i in input:
    if i != '\n':
        answers.append(string_2_number(i[:-1]))
    else:
        T1_result += task_1(answers)
        T2_result += task_2(answers)
        answers=[]

print(T1_result)
print(T2_result)