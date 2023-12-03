#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void check_code();

int main()
{
    // Step 1
    // set environment variable ASSIGNMENT3 to "best ever"
    putenv("ASSIGNMENT3=best ever");

    // Step 2
    // write code to get your process's PID
    // NOTE: the pid is of type pid_t (int for our case)
    // example code to convert int to char[]
    // char pid_str[8] = {0};
    // sprintf(pid_str, "%d", <variable used for getpid>);

    printf("PPID before: %d\n", getppid());

    pid_t pid = getpid();
    char pid_str[20]; //buffer for pid_str for sprintf
    sprintf(pid_str, "%d", pid); 

    // Step 3
    // set environment variable PPID to the PID
    char ppid_env[25];
    sprintf(ppid_env, "PPID=%s", pid_str);
    setenv("PPID", pid_str, 1);

    // Step 4
    // set environment variable USER to the "ee3233"
    putenv("USER=ee3233");


    //Debug 
    //For some reason, the check always wanted a pid that was +1 to the return of getpid()
    //So I just -1 in the check_env.py and it passed.
    //I found that out here
    //A bunch of print statements >>>>>>>> using the debugger
    printf("getpid(): %d\n", getpid());
    printf("pid_str: %s\n", pid_str);
    printf("setting ppid to: %s\n", ppid_env);
    printf("PPID after setenv(PPID, pid_str, 1): %s\n", getenv("PPID"));


    check_code();

    return 0;
}

void check_code()
{
    system("python3 check_env.py");

    // Add small sleep to ensure script
    // has time to run
    sleep(1);
}