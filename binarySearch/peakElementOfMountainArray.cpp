#include<iostream>

using namespace std;

/*


Given an array of length greater than "3" and guarantees mountain like

array = [1,2,8,6,2]   ---> 8 is the peak element

            8 
                6
    2               2
1

*/


int findPeak(int arr[], int length){
    int start =0;
    int end =  length-1;
    int mid = (start+end)/2;

    while(start<end){ // Here start < ends means there is still one element left in the array
        if(arr[mid] < arr[mid+1]){
            start = mid+1;
        }else{
            end= mid;
        }
        mid = (start+end)/2;

    }
    return start;

}

int main(){

    int arr[] = {1,2,5,9,12,18,7,2};
    int len = sizeof(arr)/ sizeof(arr[0]);

    cout<<findPeak(arr, len)<<endl;

    return 0;
}