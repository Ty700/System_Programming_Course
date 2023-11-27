#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

#define FILENAME "test.txt"

int main() {

    const char* fileName = FILENAME;
    const char* writeCommand = "echo 'Hello World' > test.txt";

    printf("Using popen to echo 'Hello World' to a file\n");

    FILE* pipePointer = popen(writeCommand, "r");

    if (!pipePointer) {
        printf("Error: Can't open pipe.\n");
        return EXIT_FAILURE;
    }
    
    pclose(pipePointer);

    printf("Using popen to cat test.txt\n");
    const char* cat_command = "cat test.txt";
    pipePointer = popen(cat_command, "r");

    if (!pipePointer) {
        printf("Error: Can't open pipe.\n");
        return EXIT_FAILURE;
    }

    char* buffer = (char *)malloc(100 * sizeof(char)); //Hard coding 100 D:

    printf("%s contains: ", fileName);
    
    while (fgets(buffer, sizeof(buffer), pipePointer) != NULL) {
        printf("%s", buffer);
    }
    pclose(pipePointer);

    return EXIT_SUCCESS;
}