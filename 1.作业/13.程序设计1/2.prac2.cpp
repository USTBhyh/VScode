#include<iostream>
using namespace std;
int main()
{
    char number_base[16];
    int number_o;
    for (int i = 0; i < 16; i++)
    {
        cin >> number_base[i];
    }
    if (number_base[15] == '0')
    {
        int temp=0;
        for (int i = 0; i < 16; i++)
        {
            temp += (number_base[15 - i] - 48) * pow(2,i);
        }
        number_o = temp;
    }
    else
    {
        int temp=0;
        for (int i = 0; i < 15; i++)
        {
            temp += (number_base[15 - i] - 48) * pow(2, i);
        }
        temp -= (number_base[0]-48) * pow(2, 15);
        number_o = temp;
    }
    cout << number_o;
    //cout << (number_base[15-i]-48);
    return 0;
}