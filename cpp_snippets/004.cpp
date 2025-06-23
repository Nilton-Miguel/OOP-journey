
#include <iostream>
#include <math.h>
using namespace std;

class Vector2D
{
// portion that´s gonna be publicly available outside the class, info is private by default in classes
public:
    // attributes
    float x,y;

    // methods
    float norm()
    {
        return sqrt(pow(x,2) + pow(y,2));
    }
    void scale(float factor)
    {
        x *= factor;
        y *= factor;
    }
};

int main()
{
    Vector2D v1;
    v1.x = 3;
    v1.y = 4;

    cout << "Norm of vector (" << v1.x << "," << v1.y << ") is " << v1.norm() << "\n";

    float scale = 2;
    cout << "Scaling it by " << scale << "\n";
    v1.scale(scale);

    cout << "Norm of vector (" << v1.x << "," << v1.y << ") is " << v1.norm() << "\n";

    return 0;
}
