#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
    int D = 5;
    int N = 1000;
    int i, j, k;
    double X[D][N];
    double beta[N], Y[N];
    double theta;
    double r;

    for (i = 0; i<N; i++){
        //beta[i] =(double) rand();
        beta[i] = 1;

        for(j=0; j<D; j++){
            //X[j][i] = rand();     
            X[j][i] = 1;
        }
    }
    //theta = rand();
    theta = 1;

    for (i = 0; i<N; i++){
        for(j=0; j<N; j++){
            r=0;
            for(k=0;k<D; k++){
                r += pow((X[k][j] - X[k][i]),2);
            }
            r = sqrt(r);
            Y[i] += beta[j] * exp(-pow(r * theta,2));
        }
    }
    printf("%f ", Y[0]);

    return 0;
}
