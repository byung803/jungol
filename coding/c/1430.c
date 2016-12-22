#include <stdio.h>

int main(){

	int i,j,k, check, jarisu=0;
	int a0=0,a1=0,a2=0,a3=0,a4=0,a5=0,a6=0,a7=0,a8=0,a9=0; 
	double val, val2=0; 

	scanf("%d", &i);
	scanf("%d", &j);
	scanf("%d", &k);

	val = i * j * k; 
	check = val; 
	val2 = val; 
//	printf("%f\n", val);

	while(check){
		check = check/10;
		val2 = val2/10;
	//printf("check: %d\n", check);	
	//printf("%f\n", val);
		jarisu++;    

	}
	check = val;	
	while(check % 10==0){
		
		a0++;
		check = check/10; 
		
	}
	
	jarisu = jarisu - a0;

	while(jarisu){
		
	val2 = val2*10;
	
	check = val2; 
	if(jarisu==1)
		check++;
//	printf("val2: %f\n", val2);
//	printf("check: %d\n", check);	
	val2 = val2 - check;
//	printf("val2 - check: %f\n", val2);
	if(check==0)
		a0++; 
	else if(check==1)
		a1++;
	else if(check==2)
		a2++;
	else if(check==3)
		a3++;
	else if(check==4)
		a4++;
	else if(check==5)
		a5++;
	else if(check==6)
		a6++;
	else if(check==7)
		a7++;
	else if(check==8)
		a8++;
	else if(check==9)
		a9++;
	jarisu--;
	}

//	printf("jarisu: %d\n", jarisu);	
	printf("%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n",a0,a1,a2,a3,a4,a5,a6,a7,a8,a9);

}
