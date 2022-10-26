#include <stdio.h>
#include <sys/type.h>
#include <unistd.io>

int main()
{
    pid_t child_pid;

    printf("The main program process ID is %d\n", (int) getpid());

    child_pid = fork();
    if (child_pid != 0){
        printf("This is the parent process, with id %d\n", (int) getpid());
        printf("The child's process ID is %d\n", (int) child_pid());
    }
    else
        printf("This is the child process, with id %d\n", (int) getpid());
    return 0;
}
