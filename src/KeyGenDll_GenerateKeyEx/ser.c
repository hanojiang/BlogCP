#include "stdio.h"

typedef unsigned int uint32;
typedef unsigned char uint8;
uint32 GENERIC_ALGORITHM(uint32 wSeed, uint32 SECURITYCONSTANT);

void GenerateKeyEx(
      const unsigned char*  iSeedArray,     /* Array for the seed [in] */
      unsigned int          iSeedArraySize, /* Length of the array for the seed [in] */
	  unsigned char*        ioKeyArray
      //unsigned int*         oSize           /* Length of the key [out] */
      )
{
  	uint32 keyout;
	uint8 keyin[4] = {0};
	for (unsigned int i = 0; i < iSeedArraySize; i++)
		keyin[i] = iSeedArray[3 - i];


	keyout = GENERIC_ALGORITHM(*(uint32*)keyin, 0xDC8FE1AE);
	
	for(unsigned int i = 0; i < iSeedArraySize; i++){
		ioKeyArray[i]=keyout >> (8*(3-i));
	}
		
		//0 24
		//1 16
		//2 8
		//3 0
		
		
    //*oSize=iSeedArraySize;
}

// 28 27 7c 00  >> 77 5f bf 00
// 25 66 a9 00 >> c9 25 aa 00
// 5a 86 d3 00 >> 4b 1b 72 00
// 84 c9 70 00 >> 58 a6 7b 00 0x58A67B6F
// 27 e5 ce 00 >> 90 d2 a4 00
uint32 GENERIC_ALGORITHM(uint32 wSeed, uint32 SECURITYCONSTANT)//#define SECURITYCONSTANT_EXTENDED 	(0xDC8FE1AE)
{
	uint8 iterations;
	uint32 wLastSeed;
	uint32 wTemp;
	uint32 wLSBit;
	uint32 wTop31Bits;
	uint8 jj,SB1,SB2,SB3;
	uint32 temp;

/*Calculate Number of passes*/
	wLastSeed = wSeed;
	temp = (uint32)((SECURITYCONSTANT&0x00000800)>>10) | ((SECURITYCONSTANT&0x00200000)>>21);
	switch(temp)
	{
		case 0:
		{
			wTemp = (uint8)((wSeed & 0xff000000) >> 24);
			break;
		}
		case 1:
		{
			wTemp = (uint8)((wSeed & 0x00ff0000) >> 16);
			break;
		}
		case 2:
		{
			wTemp = (uint8)((wSeed & 0x0000ff00) >> 8);
			break;
		}
		case 3:
		{
			wTemp = (uint8)(wSeed & 0x000000ff);
			break;
		}
	}

/*SB2 and SB3 determin the maximum number of passes through the loop.*/
/*Size of SB2 and SB3 can be limited to fewer bits, to minimise the maximum number of passes through the algorithm*/
	SB1 = (uint8)((SECURITYCONSTANT&0x000003FC) >> 2);
	SB2 = (uint8)(((SECURITYCONSTANT&0x7F800000) >> 23) ^ 0xA5);
	SB3 = (uint8)(((SECURITYCONSTANT&0x001FE000) >> 13) ^ 0x5A);

/*The iterations calculation; where wSeedItByte, SB1, SB2 and SB3 are generated from fixed SECURITYCONSTANT*/
	iterations = (uint32)(((wTemp ^ SB1) & SB2) + SB3);
	for(jj=0; jj<iterations; jj++)
	{
		wTemp = ((wLastSeed & 0x40000000)/0x40000000) ^ ((wLastSeed & 0x01000000)/0x01000000) ^ ((wLastSeed & 0x1000)/0x1000) ^ ((wLastSeed & 0x04)/0x04);
		wLSBit = (wTemp & 0x00000001);
		wLastSeed = (uint32)(wLastSeed << 1);			/*Left Shift the bits*/
		wTop31Bits = (uint32)(wLastSeed & 0xFFFFFFFE);
		wLastSeed = (uint32)(wTop31Bits | wLSBit);
	}

/*Do byte swap, as per spec		0 1 2 3*/
	if(SECURITYCONSTANT & 0x00000001)
	{
		wTop31Bits = ((wLastSeed & 0x00FF0000)>>16) |		/* KEY[0] = Last_Seed[1]*/
					((wLastSeed & 0xFF000000)>>8) |			/* KEY[1] = Last_Seed[0]*/
					((wLastSeed & 0x000000FF)<<8) |			/* KEY[2] = Last_Seed[3]*/
					((wLastSeed & 0x0000FF00)<<16);			/* KEY[3] = Last_Seed[2]*/
	}
	else
	{
		wTop31Bits = wLastSeed;
	}

	wTop31Bits = wTop31Bits ^ SECURITYCONSTANT;
	
	return wTop31Bits;
}

/*
int main()
{
	uint8 out[4] = {0u};
	//uint8 in[4] = {0x28, 0x27, 0x7c, 0x00};//77 5f bf 93
	//uint8 in[4] = {0x25, 0x66, 0xa9, 0x00};//c9 25 aa f3
	//uint8 in[4] = {0x5a, 0x86, 0xd3, 0x00};//4b 1b 72 6e
	//uint8 in[4] = {0x84, 0xc9, 0x70, 0x00};//58 a6 7b 6f
	uint8 in[4] = {0x27, 0xe5, 0xce, 0x00};//90 d2 a4 87
	unsigned int len = 0;
	GenerateKeyEx(
      &in[0], 4, &out[0], &len
      );
	  
	printf("length is %d\n", len);
	for(unsigned int i=0; i<4; i++)
	{
		printf("%x ", out[i]);
		
	}
	return 0;
}
*/