#include <stdio.h>

int main() {
  bool match = false;
  match &= 1;
  if (match)
    printf("Yes\n");
}