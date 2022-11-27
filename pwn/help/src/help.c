#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <setjmp.h>
#include <stdlib.h>

static int win() 
{
	char flag[40];
	
	FILE *fd = fopen("flag.txt", "r");
	fgets(flag, 40, fd);
	printf("Here is your flag ! %s", flag);
	
	exit(0);
}

static void handler(int sig,  siginfo_t *osef, void *osef2)
{
	win();
}

int set_handler()
{
	struct sigaction sa;

  	memset(&sa, 0, sizeof(sigaction));
  	sigemptyset(&sa.sa_mask);

  	sa.sa_flags     = SA_NODEFER;
  	sa.sa_sigaction = handler;

  	sigaction(SIGSEGV, &sa, NULL);

	return 0;
}

int main()
{
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
	
	set_handler();

	char buf[0x1000];
       	
	printf("What would you scream if you needed help ?");
	scanf("%s", &buf);
	
	return 0;	
}
