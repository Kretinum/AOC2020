
def add_s_rem_space(x):
    x=x[1:]
    if x[-1]!="s":
        x+="s"
    return x

auxi = {}
def recursion_task_1(position,dict):

    if position in auxi:
        return auxi[position]
    for i in dict[position]:
        if "shiny gold" in i:
            auxi[position] = 1
        if "no other" not in i:
            if recursion_task_1(i[2:],dict)==1:
                auxi[position] = 1
        else:
            auxi[position] = 0
            return 0
    if position not in auxi:
        auxi[position]=0
    return auxi[position]

def solve_task_1(dict):

    for key in dict:
        if key not in auxi:
                recursion_task_1(key,dict)
    result = 0
    for key in auxi:
        result+=auxi[key]
    return result


auxi2 = {}
def solve_task_2(dict,position):
    if position in auxi2:
        return auxi2[position]
    auxi2[position] = 1
    for i in dict[position]:
        if "no other" in i:
            return 1
        number_of_bags = int(i[:1])
        bag_type = i[2:]
        auxi2[position]+=number_of_bags*solve_task_2(dict,bag_type)

    return auxi2[position]

file = open("input.txt")
inp = file.readlines()
file.close()
graph = {}

for i in inp:
    l_r = i.split("contain")
    array = l_r[1].split(",")
    array[-1] = array[-1][:-2]
    for j in range(len(array)):
        array[j]=add_s_rem_space(array[j])
    graph.update({l_r[0][:-1]:array})


print(solve_task_1(graph))
print(solve_task_2(graph,"shiny gold bags")-1)