#include<iostream>
using namespace std;


int binarySearch(int arr[], int s, int e, int item){
    int mid = (s+e)/2;
    if(s>e)
        return -1;
    if(arr[mid] == item){
        return mid;
    }else if(arr[mid] > item){
        binarySearch(arr, s, mid-1, item);
    }else{
        binarySearch(arr, mid+1, e, item);
    }

}


int main(){

    int arr[] = {1,3,5,7,8,9,13,15,19};
    int len = sizeof(arr)/sizeof(arr[0]);

    cout<<binarySearch(arr,0,len-1, 19)<<endl; 

    return 0;
}