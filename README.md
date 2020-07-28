# skyfilabs-mobile-robot
code done using Keil uVision5 for project of mobile controlled robot done through online course in skyfilabs
// include header files

#include <reg52.h>
#include <stdio.h>

// define the motor conditions
#define lt 0x06;
#define rt 0x09;
#define st 0x0a;
#define stop 0x00;
#define rev 0x05;

unsigned int a;

void main()
{
	while(1)
	{
		a=P0&0x0f; //Masking is done on Port0 with 0x0f
		if(a==0x02)
		{
			P2=st;
		}
		if(a==0x08)
		{
			P2=rev;
		}
		if(a==0x04)
		{
			P2=lt;
		}
		if(a==0x06)
		{
			P2=rt;
		}
		if(a==0x05)
		{
			P2=stop;
		}
	}
}
