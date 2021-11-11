#include <stdio.h>
#include <math.h>
#define PI 3.1415926535
int main(){
    float x, result, rad;
    x = 30.0;
    rad = (x/180)*PI;
    result = sin(rad);
    printf("%lf\n", sin(30/180*PI)); // 0.000
    printf("%lf", sin(30.0/180*PI)); // 0.500 
}