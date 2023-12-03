#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]){
    pid_t child_pid;

    switch(child_pid = fork()){
        case 0:
            printf("[PID %d] Child Process. Parent ID = %d.\n", (int)getpid(), (int)getppid());
            break;
        case -1:
            printf("ERROR\n");
            break;
        default:
            printf("[PID %d] Parent Process. Parent ID = %d\n", (int)getpid(), (int)child_pid);
            break;
    }
}