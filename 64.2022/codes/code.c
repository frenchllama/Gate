#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double genSample(){

    double u = (double)rand() / RAND_MAX;
    
    if(u<0.5){
        return(-2+2*sqrt(2*u));
    }

    return (2*u-1);
}

int main(){

	int simlen = 10000000;

	double *X = malloc(simlen*sizeof(double));

	srand(time(NULL));

    for(int i=0; i<simlen; i++){
        X[i] = genSample();
    }

    FILE *fptr = fopen("vals.txt","w");

    if(fptr == NULL){
      printf("Error!");   
      exit(1);             
    }

    for(int i=0; i<simlen; i++){
        fprintf(fptr, "%lf\n", X[i]);
    }

    fclose(fptr);
}