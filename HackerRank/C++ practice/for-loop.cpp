//Link to Question
//https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    // Complete the code.
    int a, b;
    cin >> a;
    cin >> b;
    string arr[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for (int i = a; i < b + 1; i++)
    {
        if (i > 9)
        {
            if (i % 2 == 0)
            {
                cout << "even" << endl;
            }
            else
            {
                cout << "odd" << endl;
            }
        }
        else
        {
            cout << arr[i - 1] << endl;
        }
    }
    return 0;
}
