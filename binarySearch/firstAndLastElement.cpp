#include<iostream>
using namespace std;


/*

Question:

find first and last occurrence of given element in an array

Eg:

input array : [1,2,4,4,4,4,7,9], key = 4
output = [2, 5]  -> cause first and last index of 4 is 2 and 5

*/


int firstIndex(int arr[], int key, int length){
    int start = 0, end = length-1;
    int ans = -1;

    while(start<=end){
        int mid = (start+end)/2;
        if(arr[mid] == key){
            ans = mid;
            end = mid-1;
        }else if(arr[mid] > key){
            end = mid-1;
        }else if (arr[mid] < key){
            start = start+1;
        }
    }
    return ans;
}

int lastIndex(int arr[], int key, int length){
    int start = 0, end = length-1;
    int ans = -1;

    while(start<=end){
        int mid = (start+end)/2;
        if(arr[mid] == key){
            ans = mid;
            start = mid+1;
        }else if(arr[mid] > key){
            end = mid-1;
        }else if (arr[mid] < key){
            start = start+1;
        }
    }
    return ans;
}




int main(){

    int arr[] = {1,2,4,4,4,4,7,9};
    int length = sizeof(arr)/ sizeof(int);

    int firstInd = firstIndex(arr, 4, length); 
    int lastInd = lastIndex(arr, 4, length); 

    cout<<firstInd<<", "<<lastInd<<endl;
    return 0;

}