#include<iostream>

using namespace std;

int findPivot(int arr[], int size){
    int start = 0, end=size-1;
    int mid = (start+end)/2;

    while(start<end){
        if(arr[mid]<arr[0])
            end = mid;
        else
        start = mid+1;

        mid = (start+end)/2;
    }
    return start;
}


int main(){

    int arr[] = {10,12, 15,1,2,3,5,7,9}; // find pivot -> 1 at index 3
    int size = sizeof(arr)/ sizeof(arr[0]);

    cout<< findPivot(arr, size) << endl;

    return 0;
}