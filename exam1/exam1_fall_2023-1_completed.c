#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define STR(x) #x

void check_code(int n, char **arg);
char *itoa(int i, char b[]);

// Your progam should take two command line arguments
// ./exam1 name value
// where name and value can be anything a user requests.

int main(int argc, char *argv[])
{
    // Step 1
    // If args is not equal to 3, print usage and exit
    if(argc != 3){
        fprintf(stderr, "Usage Error: %s name value\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // Step 2
    // Set environment variable using name and value
    // hint: argv[1] contains the name
    //       argv[2] contains the value
    unsetenv(argv[1]);
    setenv(argv[1], argv[2], 1);

    // Step 3 (Bonus Points)
    // Get the PID
    // Set environment variable "PID" to the PID value
    // hint: you need to convert the PID to a string first (there might be an example...)
    
    pid_t currentPID = getpid();
    char buffer[15];
    sprintf(buffer, "%d", currentPID);

    unsetenv("PID");
    setenv("PID", buffer ,1);

    check_code(argc, argv);
    return 0;
}

// Code below is just to grade the exam
// You MAY NOT use the asm code below for the bonus portion
// (use getpid as in the lectures)
void check_code(int n, char **arg)
{
    // Check environment variable
    printf("\x1b[32m*** Checking environment variable result ***\n");
    if (n < 3)
    {
        printf("\x1b[31m[x] Test Failed!: not enough arguments\n");
    }
    else
    {
        char *env_name = *++arg;
        char *env_value = *++arg;
        char *env_result = getenv(env_name);

        if (env_result != NULL)
        {
            int result = strcmp(env_value, env_result);

            if (result == 0)
            {
                printf("\x1b[32m[\xE2\x9C\x93] Test Passed!: %s == %s\n", env_name, env_value);
            }
            else
            {
                printf("\x1b[31m[x] Test Failed!: %s != %s\n", env_value, env_name);
            }
        }
        else
        {
            printf("\x1b[31m[x] Test Failed!: environment var `%s` does not have a value\n", env_name);
        }
    }

    // Check bonus
    printf("\n\x1b[32m*** Bonus: Checking if PID set correctly\n");
    pid_t pid;
    asm volatile("syscall"
                 : "=a"(pid)
                 : "0"(39));

    char buf[64] = {0};
    itoa(pid, buf); // ahem

    char *env_result = getenv("PID");
    if (env_result != NULL)
    {
        int result = strcmp(buf, env_result);
        printf("\x1b[32m[\xE2\x9C\x93] Test Passed!: %s == %s\n", env_result, buf);
    }
    else
    {
        printf("\x1b[31m[x] Test Failed!: environment var `PID` does not have a value\n");
    }
}

char *itoa(int i, char b[])
{
    char const digit[] = "0123456789";
    char *p = b;
    if (i < 0)
    {
        *p++ = '-';
        i *= -1;
    }
    int shifter = i;
    do
    { // Move to where representation ends
        ++p;
        shifter = shifter / 10;
    } while (shifter);
    *p = '\0';
    do
    { // Move back, inserting digits as u go
        *--p = digit[i % 10];
        i = i / 10;
    } while (i);
    return b;
}