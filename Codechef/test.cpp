    #include <iostream>
    #include <string>
    using namespace std;
    int main()
    {

        int t;
        cin >> t;
        string preference;
        string offers;
        for (int i = 0; i < t; i++)
        {
            preference = "";
            offers = "";
            cin >> preference;
            cin >> offers;
            cout << preference[0];
            // if (preference[0] == offers[0])
            // {
            //     cout << preference[0];
            // }
            // else if (preference[2] == offers[2])
            // {
            //     cout << preference[2];
            // }
        }
        return 0;
    }