#include<iostream>
using namespace std;


/*
iterative Binary Search function to search an array of integers.
Return element's index of found else return -1
*/

int iterativeBinarySearch(int arr[], int length, int key){
    int start = 0;
    int end = length;


    while(start<=end){
        int mid = (start+end)/2;
        if(arr[mid] == key){
            return mid;
        }
        if(key > arr[mid]){
            start = mid+1;
        }else{
            end = mid-1;
        }

    }
    return -1;
}


int main(){

    int arr[] = {1,4,6,17,88,93,167};

    int ans = iterativeBinarySearch(arr, 7, 6); //  Passing 6 as the key to search

    if (ans < 0){
        cout<<"The item you are searching for doesnot exists"<<endl;
    }else{
        cout<<"The item is found at index "<<ans<<endl;
    }


    return 0;

}