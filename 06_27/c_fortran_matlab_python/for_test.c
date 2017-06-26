#include <stdio.h>
void main(){
    int i, j, mul;
    for(i=0;i<100000;i++){
        for(j=0;j<10000;j++){
            if(i==99999 && j==9999){
                printf("C: looping is over!!\n");
            }
        }
    }
}
