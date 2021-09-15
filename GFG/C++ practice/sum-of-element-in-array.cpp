//Link to Question
//https://www.geeksforgeeks.org/program-find-sum-elements-given-array/

#include <iostream>
using namespace std;

int main()
{
    int numbers[9] = {1, 3, 5, 2, 55, 24, 5, 2, 34};
    int length = sizeof(numbers) / sizeof(int);
    int total = 0;
    for (int i = 0; i < length; i++)
    {
        total += numbers[i];
    }
    cout << total;
    return 0;
}