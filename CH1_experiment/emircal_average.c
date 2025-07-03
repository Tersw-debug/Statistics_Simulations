#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define TRIALS 10000

float experiment(int n, double p){
    int heads = 0;
    for(int i = 0; i < n; i++)
    {
        if((double) rand() / RAND_MAX < p){
            heads++;
        }
    }
    return heads;
}

int main(void) {
    int nk[3] = {10,100,1000};
    double p = 0.3;
    
    srand(time(NULL));

    for(int i = 0; i < 3; i++)
    {
       int n = nk[i];
       long long heads = 0;
       for(int j = 0; j < TRIALS;j++)
       {
            heads += experiment(n,p);
       }
       double average_heads = (double) heads / TRIALS;
       double expected = n * p;
       printf("n = %d\n", n);
       printf("Average Heads %d over Trials: %0.4f\n", average_heads, TRIALS);
       printf("Expected Heads = n*p = %0.4f\n",expected);
       printf("Average Heads - Expected Heads = %0.4f\n", (average_heads - expected));
    }
    return 0;
}