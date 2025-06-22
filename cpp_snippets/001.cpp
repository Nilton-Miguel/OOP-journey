
#include <iostream>

using namespace std;

int main()
{
    int x;

    cout << "Enter a interger: ";
    if(cin >> x)
    {
        cout << "You have entered: " << x << endl;
    }
    else
    {
        cin.clear();
        cout << "Invalid input\n";
    }

    return 0;
}
