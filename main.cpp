#include "lib/examples.h"

/* Check if creation of a library like this would work without cython
syclcc --hipsycl-targets="cuda:sm_75" main.cpp -Llib -lexamples -o test -Ilib/examples.h
Run ./test to see it is working
*/

int main(){
  hello("Test");
}
