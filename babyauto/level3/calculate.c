#include <stdio.h>

int main(void)
{
    int iteration;
    unsigned long long val, input[50];

    scanf("%d", &iteration);
    //printf("iteration: %d\n", iteration);

    for (int i = 0; i < iteration; i++)
    {
        scanf("%llx", &input[i]);
        //printf("input[%d]: %llx\n", i, input[i]);
    }

    scanf("%llx", &val);
    //printf("val: %llx\n", val);

    for (int i = 0; i < iteration; i++)
    {
        val -= input[i];
    }

    printf("%llu\n", val);
    return 0;
}