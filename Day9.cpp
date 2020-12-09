#include <iostream>
#include <fstream>
std::ifstream fin("C:\\Users\\mihai\\CLionProjects\\AOCDay9\\input.txt");
long long arr[1001];
bool check_valid(long long arr[],int position)
{
    for (int i=position-25;i<position-1;i++)
    {
        for (int j=i+1;j<position;j++)
            if (arr[i]+arr[j]==arr[position])
                return 1;
    }
    return 0;
}
long long task_1(long long arr[],int len)
{
    for (int i=25;i<len;i++)
        if (!check_valid(arr,i))
            return arr[i];
}
//i could have use segment trees for these two,but there was no purpose to overcomplicate myself since i only search for min and max once in the whole program anyway
//besides since i'm only calling them once the complexity would have been slightly bigger
long long get_min(long long arr[],int left,int right)
{
    long long min = arr[left];
    for (int i=left+1;i<=right;i++)
        if (min<arr[i])
            min = arr[i];
    return min;
}
long long get_max(long long arr[],int left,int right)
{
    long long max = arr[left];
    for (int i=left+1;i<=right;i++)
        if (max>arr[i])
            max = arr[i];
    return max;
}

long long task_2(long long arr[],int len,long long value)
{
    long long sum_2_here[1000];
    sum_2_here[1]=arr[1];
    for (int i=1;i<len;i++) {
        sum_2_here[i] = sum_2_here[i - 1] + arr[i];
    }

    for (int i=0;i<len-1;i++)
        for (int j=i+1;j<len;j++)
            if (i==0) {
                if (sum_2_here[j] == value)
                    return get_min(arr, 0, j) + get_max(arr, 0, j);
            }
            else {
                if (sum_2_here[j] - sum_2_here[i - 1] == value)
                    return get_min(arr, i, j) + get_max(arr, i, j);

            }
}
int main() {
    long long x;
    int poz=0;
    while (fin>>arr[poz++]);
    long long result1 = task_1(arr,poz);
    std::cout<<result1<<"\n"<<task_2(arr,poz,result1);
    return 0;
}
