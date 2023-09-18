
/*
* Is it the most efficent way?
* Prob not. But I have a migraine and just trying to survive right now
*/

#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define BUF_SIZE 1024

int main(int argc, char *argv[]){
    int inputFd, outputFd, outputFd2, openFlags;
    mode_t filePerms;
    size_t numRead;
    char buf[BUF_SIZE];

    if (argc != 4 || strcmp(argv[1], "--help") == 0){
        fprintf(stderr, "Usage: %s source_file destination_file1 destination_file2\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* Open input and output files */
    inputFd = open(argv[1], O_RDONLY); /* O_CREAT is not specified, mode can be omitted */
    if (inputFd == -1) {
        fprintf(stderr, "Opening Error!: [%s]\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    openFlags = O_CREAT | O_WRONLY | O_TRUNC;
    filePerms = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH; /* rw-rw-rw- */

    outputFd = open(argv[2], openFlags, filePerms);
    if (outputFd == -1){ /* If an error occurs, open returns -1 */
        fprintf(stderr, "Opening Error!: [%s]\n", argv[2]);

        exit(EXIT_FAILURE);
    }

    outputFd2 = open(argv[3], openFlags, filePerms);
    if (outputFd == -1){ /* If an error occurs, open returns -1 */
        fprintf(stderr, "Opening Error!: [%s]\n", argv[3]);

        exit(EXIT_FAILURE);
    }


    /* Transfer data until we encounter end of input or an error */
    while ((numRead = read(inputFd, buf, BUF_SIZE)) > 0)
        if (write(outputFd, buf, numRead) && write(outputFd2, buf, numRead) != numRead){
            fprintf(stderr, "Error: Couldn't write to whole buffer");
            exit(EXIT_FAILURE);
        }

        if (numRead == -1) {
            fprintf(stderr, "Read Error");
            exit(EXIT_FAILURE);
        }
        if (close(inputFd) == -1){
            fprintf(stderr, "Closing Input Error");
            exit(EXIT_FAILURE);
        }
        if (close(outputFd) == -1){
            fprintf(stderr, "Closing Output Error");
            exit(EXIT_FAILURE);
        }
        if (close(outputFd2) == -1){
            fprintf(stderr, "Closing Output Error");
            exit(EXIT_FAILURE);
        }
        exit(EXIT_SUCCESS);
}