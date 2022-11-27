int main(void){
    unsigned int code;
    printf("Maître, quel est votre code à 4 chiffres ?");scanf("%u",&code);
    if(code == 2611){
        printf("Vous pouvez donner ce code à un administrateur du FlagMalo, il vous donnera votre flag :)");
    }else{
        printf("Raté, faites un effort...");
    }
    return 0;
}
main();
