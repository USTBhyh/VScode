#include <iostream>
using namespace std;
int transport(char*a);//定义函数转换
int gety(int a, int b)//定义函数求幂
{
int c=1;
while(b--)
	c=c*a;
return c;
}
int getz(char*a)//定义函数负整数的补码转换
{
for (int i = 15; i >= 0;i --)
{
if (*(a+i)=='0')
	*(a+i)='1';
else *(a+i)='0';
}
*(a+15)+=('1'-'0');
for (int i = 15; i >= 0;i --)
{
if (*(a+i)=='2')
{
*(a+i)='0';
*(a+i-1)+=('1'-'0');
}

}
return 0;
}

int transport(char*a)
{
int value=0;
if (*a=='0')
{
for (int i = 15; i >= 0;i --)
{
if (*(a+i)== '1')
value += gety(2,15-i); 
}
}
else
{
getz(a);
for (int i = 15; i > 0;i --)
{
if (*(a+i)== '1')
value += gety(2,15-i); 
}
value=0-value;
}	
	
	return value;
}


int main()
{
char a[17];
cin.get(a,17);
cout<<transport(a)<<endl;
return 0; 
} 
