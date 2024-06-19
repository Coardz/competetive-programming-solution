#include <iostream>
#define ll long long int
using namespace std;

int main()
{
    ll n = 3;

    while (n != 1) // != means is not so we check if our variable is not equal to 1 we repeat the loop 
    {
        cout << n << " " ;
        if (n % 2 != 0) 
        {
            n = n * 3 + 1;
        }
        else 
        {
            n /= 2;
        }
    cout << 1;
    }
}