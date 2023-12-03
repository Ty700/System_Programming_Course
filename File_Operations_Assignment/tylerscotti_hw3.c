#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <grp.h>
#include <pwd.h>
#define PATH_MAX 4096

static char filenames[PATH_MAX][PATH_MAX] = {0};

static int filetypeletter(int mode){
    char c;

    if (S_ISREG(mode))
        c = '-';
    else if (S_ISDIR(mode))
        c = 'd';
    else if (S_ISBLK(mode))
        c = 'b';
    else if (S_ISCHR(mode))
        c = 'c';
#ifdef S_ISFIFO
    else if (S_ISFIFO(mode))
        c = 'p';
#endif 
#ifdef S_ISLNK
    else if (S_ISLNK(mode))
        c = 'l';
#endif
#ifdef S_ISSOCK
    else if (S_ISSOCK(mode))
        c = 's';
#endif
#ifdef S_ISDOOR
   
    else if (S_ISDOOR(mode))
        c = 'D';
#endif 
    else
    {
        c = '?';
    }
    return (c);
}

static char *lsperms(int mode){
    static const char *rwx[] = {"---", "--x", "-w-", "-wx",
                                "r--", "r-x", "rw-", "rwx"};
    static char bits[11];

    bits[0] = filetypeletter(mode);         
    strcpy(&bits[1], rwx[(mode >> 6) & 7]);
    strcpy(&bits[4], rwx[(mode >> 3) & 7]);
    strcpy(&bits[7], rwx[(mode & 7)]);
    if (mode & S_ISUID)
        bits[3] = (mode & S_IXUSR) ? 's' : 'S';
    if (mode & S_ISGID)
        bits[6] = (mode & S_IXGRP) ? 's' : 'l';
    if (mode & S_ISVTX)
        bits[9] = (mode & S_IXOTH) ? 't' : 'T';
    bits[10] = '\0';
    return (bits);
}

unsigned int listdir(const char *pathname){
    struct dirent *dir;
    DIR *d = opendir(pathname);
    unsigned int counter = 0;
    if (d)
    {
        while ((dir = readdir(d)) != NULL)
        {
            strcpy(filenames[counter++], dir->d_name);
        }
        closedir(d);
    }

    return counter;
}

const char *get_filename_ext(const char *filename){
    const char *dot = strrchr(filename, '.');
    if (!dot || dot == filename)
        return "";
    return dot;
}

void details(char *filename, struct stat buf){
    printf("Filename:     %s \n", filename);

    int mode = buf.st_mode;
    char *perms = lsperms(mode);
    printf("Permissions:  %s\n", perms);

    struct passwd *pw = getpwuid(buf.st_uid);
    printf("Owner:        %s\n", pw->pw_name);

    struct group *gr = getgrgid(buf.st_gid);
    printf("group:        %s\n\n", gr->gr_name);
}

int search(char *filename, char *keyword){
    FILE *fp;
    int line = 1;
    int result = 0;
    char buf[512];

    if ((fp = fopen(filename, "r")) == NULL) 
    {
        printf(" File opening error for %s ", filename);
    }

    while (fgets(buf, 512, fp) != NULL) 
    {
        if ((strstr(buf, keyword)) != NULL) 
        {
            result = 1;
        }
        line++;
    }
    return result;
}

int main(int argc, char *argv[]){

    char *operation = argv[1];
    const char *file_ext = argv[2];
    char *path = argv[3];
    unsigned int num_files_found = listdir(".");
    char validFilenames[] = {0};
    struct stat buf;
    int keywordfound = 0;
    
    if (chdir(path) == 0) { 
        chdir(path);
    }
    else {
        printf("Please ensure the directory path is correct.\n");
        exit(1);
    }

    for (int i = 0; i < num_files_found; i++)
    {
        stat(filenames[i], &buf);
        if (argc == 4 & strcmp(argv[1], "details") == 0) 
        {                                                
                if ((strcmp(get_filename_ext(filenames[i]), file_ext)) == 0)
                {
                    details(filenames[i], buf);
                }
        }

        else if (argc == 5 & strcmp(argv[1], "search") == 0) 
        {                                                  
            if (i == 0) 
            {
                printf("Keyword \"%s\" found in: ", argv[4]);
            }
            if (keywordfound == 0 & i == num_files_found - 1) 
            {
                printf("None");
            }
            if (i == num_files_found - 1) 
            {
                printf("\n");
            }
            if ((strcmp(get_filename_ext(filenames[i]), file_ext)) == 0) 
            {                                                           
                if (search(filenames[i], argv[4]) == 1)
                {
                    printf("%s ", filenames[i]);
                    keywordfound = 1;
                }
            }
            
        }

        else
        {
            printf("-------------------------\n");
            printf("Usage Error\n"); 
            printf("Details: ./tylerscotti_hw3 details [File Extension] [Target Directory Path]\n");
            printf("Search: ./tylerscotti_hw3 search [File Extension] [Target Directory Path] [Keyword]\n");
            printf("-------------------------\n");
            exit(1);
        }
    }
}