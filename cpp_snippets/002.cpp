
#include <iostream>

using namespace std;

int main()
{
    /*
    string name;

    cout << "Enter your name: ";
    getline(cin, name, '\n');
    cout << "Hello " << name << ", welcome to C++\n";

    cout << '\n';
    */

    double height, width, area = 0;
    cout << "Enter height and width space separated: ";
    cin >> height >> width;
    area = height * width;
    cout << "With the height " << height << " and the width " << width << " you get area " << area << '\n';

    return 0;
}
