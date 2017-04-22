#include <limits.h>
#include <stdio.h>
int main(char ** argv, int argc) {
  short s = 32760;
  for (int i = 0; i < 12; ++i)
    printf("s = %d\n", s++);
  int x = INT_MAX - 6;
  for (int i = 0; i < 12; ++i)
    printf("x = %d\n", x++);
  unsigned int y = 5;
  for (int i = 0; i < 12; ++i)
    printf("y = %u\n", y--);
}
