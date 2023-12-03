#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void signal_handler(int signum) {
    if (signum == SIGUSR1) {
        printf("This is the signal handler!\n");
    }
}

void signal_handler_child(int signum) {
    if (signum == SIGUSR1) {
        printf("Child received signal!\n");
    }
}

int main() {
    //Creating empty set
    sigset_t block;
    sigemptyset(&block);
    //Adding SIGUSR1 to set
    sigaddset(&block, SIGUSR1);
    //Proc mask
    sigprocmask(SIG_BLOCK, &block, NULL);

    

    printf("Parent started...\n");
    sleep(3);
    printf("Parent about to signal child...\n");

    pid_t child = fork();

    if (child < 0) {
        perror("Error: Fork()");
        exit(1);
    } else if (child != 0) {
        sigset_t child_mask;
        sigemptyset(&child_mask);
        sigprocmask(SIG_SETMASK, &child_mask, NULL);

        signal(SIGUSR1, signal_handler_child);

        
        // Wait for Signal
        pause();

        //reseting 
        sigprocmask(SIG_BLOCK, &block, NULL);

        exit(0);
    } else { 
        kill(child, SIGUSR1);
        exit(0);
    }
}
