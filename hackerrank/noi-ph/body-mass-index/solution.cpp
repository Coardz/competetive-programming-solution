/* Learning C++
 * Prince Jeric D. Banal
 * 6/15/2024
 * Grade 12 ICT
 */

#include <iostream>
using namespace std;

int main()
{
    int w; // weight
    int h; // height

    std::cin >> w; // input weight
    std::cin >> h; // input height

    std::cout << (w / (h * h)) << std::endl;

    if (w / (h * h) >= 25) {
        std::cout << "GO ON A DIET" << std::endl;
    }
    else {
        std::cout << "YOU ARE TOO THIN" << std::endl;
    }
    return 0;
}

