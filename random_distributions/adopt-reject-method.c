#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "dSFMT.h"


double func(double x){
	double s =exp(-pow((x-3),2)/2)/(pow(2,0.5)+M_PI)+exp(-pow((x+3),2)/2)/(pow(2,0.5)+M_PI);
	return s;
}

int main(){
	double a,b;
	dsfmt_t dsfmt1;
	dsfmt_init_gen_rand(&dsfmt1, 1234);



	for (int i=0; i<100000;i++){
		a=2.5*dsfmt_genrand_close_open(&dsfmt1);
		b=10*(dsfmt_genrand_close_open(&dsfmt1)-0.5);
		
		if(a<func(b)){
			printf("%lf %lf\n",b,a);
		}
		//printf("%lf\n",a);
	}
}