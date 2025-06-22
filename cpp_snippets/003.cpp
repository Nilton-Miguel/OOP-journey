
#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    while (i < 10) cout << i++ << ' ';
    cout << '\n';

    i = 0;
    do cout << i++ << ' '; while(i < 10);
    cout << '\n';

    return 0;
}
