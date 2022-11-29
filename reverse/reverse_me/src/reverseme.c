#include <stdio.h>
#include <string.h>

#define FLAG "}19das5131a_gni1sr3v3r_0T_em0cleW{FTCMF"


void revstr(char *password)  
{  
    int i, len, temp;  
    len = strlen(password);
      
    for (i = 0; i < len/2; i++)  
    {  
        temp = password[i];  
        password[i] = password[len - i - 1];  
        password[len - i - 1] = temp;  
    }  
}


int main() 
{
    char user_input[40];

    puts("Password ?");
    fgets(user_input, 40, stdin);
    
    revstr(user_input);
    
    if(strcmp(user_input, FLAG)) 
    {
        puts("No...");
    } else {
        puts("Well done !");
    }

    return 0;
}
