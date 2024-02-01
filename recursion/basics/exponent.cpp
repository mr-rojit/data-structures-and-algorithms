#include<iostream>
using namespace std;

int positiveNumberExponent(int base, int power){
    if(base == 0)
        return 0;
    
    if(power==0){
        return 1;
    }
    return base * positiveNumberExponent(base, power-1);

}


int main(){

    cout<<positiveNumberExponent(0,5)<<endl;

    return 0;
}