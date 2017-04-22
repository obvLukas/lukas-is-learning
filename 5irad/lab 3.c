#include
<stdio.h>


int a = 3;
double d = 3.0;
d = a;
d = (double) a;
int[] v1 = {1,2,5};


int * v2;
v2 = malloc(205 * sizeof(int));
//free(v2);
*v2 = 3;
int * p2 = v2+1;
* p2 = 5;
p2 = p2+2;
* p2 = 7;
p2 = 8;


int a = 3;
int b = 4;
int c = 5;
int * p = &b
*p = 6;
p = p+1;
*p = 7;



int * foo() {
  int a = 3;
  return &a;
}
int x = 3;
int * p = &x;
p = foo();
printf("p=%d",*p);

int i = 0;
i++;
printf(i++);
++i;
printf(++i);

char * s = "Hej";

// &a = adressen till a (det a pekar på).
// s[1] = *(s+1) kommutativt med 1[s] = *(1+s)


//Lab 3

while(*t++ = *s++);
