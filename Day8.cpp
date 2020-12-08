#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
std::ifstream fin("C:\\Users\\mihai\\CLionProjects\\AOCDay8\\input.txt");
typedef struct instruction{
    int type;
    int value;
};
int task_1(int postion,instruction ins_list[],bool visited_array[],int cr_acc,int size)
{
    if (visited_array[postion] == 1)
        return cr_acc;

    if (postion == size) {
        return cr_acc;
    }

    visited_array[postion] =1;
    if (ins_list[postion].type == 1)
        cr_acc+=ins_list[postion].value;
    else if (ins_list[postion].type == 2) {
        return task_1(postion + ins_list[postion].value, ins_list, visited_array, cr_acc,size);
    }
    else
        ;

    return task_1(postion+1,ins_list,visited_array,cr_acc,size);
}

bool check_loop(int postion,instruction ins_list[],bool visited_array[],int size)
{
    if (postion == size)
        return 1;
    if (visited_array[postion] == 1) {
        return 0;
    }
    visited_array[postion] =1;
    if (ins_list[postion].type == 1)
        ;
    else if (ins_list[postion].type == 2) {
        return check_loop(postion + ins_list[postion].value, ins_list, visited_array,size);
    }
    else
        ;
    return check_loop(postion+1,ins_list,visited_array,size);
}

int task_2(instruction ins_list[],int size)
{
    bool visited_array[655];
    for (int i=0;i<size;i++)
    {
        int original_type = ins_list[i].type;
        if (ins_list[i].type==2)
            ins_list[i].type = 3;
        else if (ins_list[i].type==3)
            ins_list[i].type = 2;
        memset(visited_array,0,size);
        if (check_loop(0,ins_list,visited_array,size-1)==1) {
            memset(visited_array,0,size);
            return task_1(0, ins_list, visited_array, 0, size - 1);
        }
        ins_list[i].type = original_type;
    }
}
bool visited_array[655];
int main() {
    std::string ins;
    int value;
    int position = 0;
    instruction ins_list[655];
    while (fin>>ins>>value)
    {
        if (ins == "acc")
            ins_list[position].type=1;
        else if (ins == "jmp")
            ins_list[position].type=2;
        else
            ins_list[position].type=3;
        ins_list[position].value = value;
        position++;
    }
    std::cout<<task_1(0,ins_list,visited_array,0,position-1)<<"\n";
    std::cout<<task_2(ins_list,position);
    return 0;
}
