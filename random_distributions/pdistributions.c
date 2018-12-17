//確率分布に従う値を出力

#include <stdio.h>
#include <stdlib.h>
#include "dSFMT.h"
#include <math.h>
#define N 50000

double exponential(double a);
double power(double a);
double cauchy(double a);
double laplace(double a);

int main()
{
  double a;
  dsfmt_t dsfmt1;
  dsfmt_init_gen_rand(&dsfmt1, 1234);
  
  for(int i=0;i<N;i++){
    a=dsfmt_genrand_close_open(&dsfmt1);
    //printf("%lf\n",exponential(a));
    //printf("%lf\n",power(a));
    //printf("%lf\n",cauchy(a));
    printf("%lf\n",laplace(a));
  }
}

//exponential distribution
double exponential(double a){ 
  double lambda = 1;
  double exp_pdf;

  exp_pdf = -1/lambda*log(a);
  return exp_pdf;
}

//power distribution
double power(double a){
  double pow_pdf;
  double alpha=2; 
  pow_pdf = pow(a,-1/alpha);
  return pow_pdf;
}

//cauchy distribution
double cauchy(double a){
  double cauchy_pdf;
    cauchy_pdf = tan((a-0.5)*M_PI);
    return cauchy_pdf;
} 

//laplace distribution
double laplace(double a){
  double laplace_pdf;
  if (a>0.5){
    laplace_pdf=-log(2-2*a);
  }
  else {
    laplace_pdf=log(2*a);
  }
  return laplace_pdf;
}




