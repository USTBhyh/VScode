#include <iostream>
using namespace std;
int main()
{
    int arr[10];
    int i, j;
    for (i = 0; i < 10; i++)
        cin >> arr[i];
    for (i = 0; i < 10; i++)
        for (j = 0; j < 10; j++)
        {
            if (arr[j + 1] > arr[j])
            {
                int c;
                c = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = c;
            }
        }
    for (i = 0; i < 10; i++)
        cout << arr[i];
    return 0;
}