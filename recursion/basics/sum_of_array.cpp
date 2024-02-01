#include<iostream>

using namespace std;

// Sum of an array using recursion

int getSum(int arr[], int size){
    if(size<=0){
        return 0;
    }
    if(size == 1){
        return arr[0];
    }else{
        int sum = arr[0] + getSum(arr+1, size-1);
        return sum;
    }
}

int main(){

    int arr[] = {1,2,3,4,5, 5};
    int size = sizeof(arr)/sizeof(arr[0]);

    cout<<getSum(arr, size)<<endl;

    return 0;
}