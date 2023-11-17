#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

//this function generates a sample belonging to the uniform distribution between 0 and 1 and then returns the inverse CDF of u
double genSample(){

    double u = (double)rand() / RAND_MAX;
    
    if(u<0.5){
        return(-2+2*sqrt(2*u));
    }

    return (2*u-1);
}

int main(){
    //I wanted to test the speed difference between c and python for this particular code
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

    //large simlen to increase accuracy of simulation
	int simlen = 10000000;

    //creating an array to hold the samles of the random variable
	double *X = malloc(simlen*sizeof(double));

	srand(time(NULL));

    //inputting values into the array
    for(int i=0; i<simlen; i++){
        X[i] = genSample();
    }

    //opening a text file to store all the generated samples
    FILE *fptr = fopen("vals.txt","w");

    if(fptr == NULL){
      printf("Error!");   
      exit(1);             
    }

    //writing all the samples into the txt file
    for(int i=0; i<simlen; i++){
        fprintf(fptr, "%lf\n", X[i]);
    }

    //closing the txt file to ensure no errors occur later
    fclose(fptr);

    //printing the time it took to run the code
    end_time = clock();

    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Time taken: %f seconds\n", cpu_time_used);
}