#include<iostream>

using namespace std;

// Check if an array is sorted using recursion

bool checkSorted(int arr[], int size){
    if(size == 0 || size ==1)
        return true;

    if (arr[0]> arr[1])
        return false;
    else
        return checkSorted(arr+1, size-1);
    
}

int main(){

    int arr[] = {1,2,3,4,5,6};
    int size = sizeof(arr)/sizeof(arr[0]);

    cout<<checkSorted(arr, size)<<endl;

    return 0;
}