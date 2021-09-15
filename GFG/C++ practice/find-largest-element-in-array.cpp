//Link to Question
//https://www.geeksforgeeks.org/c-program-find-largest-element-array/

#include <iostream>
using namespace std;

int main()
{
    int maximum = 0;
    int numbers[9] = {1, 3, 5, 2, 55, 24, 5, 2, 34};
    for (int i = 0; i < sizeof(numbers) / sizeof(numbers[0]); i++)
    {
        if (maximum < numbers[i])
        {
            maximum = numbers[i];
        }
    }
    cout << maximum;
    return 0;
}