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
    int start = 0, end = length-1;

    while(start<=end){
        int mid = (start+end)/2;

        if(arr[mid] > arr[mid-1] && arr[mid] > arr[mid+1]){
            return mid;
        }else if( arr[mid]<arr[mid+1] ){
            start = mid+1;
        }else if(arr[mid]>arr[mid+1]){
            end =  mid;
        }
    }

}

int main(){

    // Not working for now

    int arr[] = {1,2, 15,9,8,6,2};
    int arr1[] = {1,21,15,9,5,6,1,0};
    int arr2[] = {1,2,5,9,12,18,26,2};

    int peakIndex = findPeak(arr, 7);
    int peakIndex1 = findPeak(arr, 8);
    int peakIndex2 = findPeak(arr, 8);

    cout<< "the peak index is "<<peakIndex <<endl;
    cout<< "the peak index is "<<peakIndex1 <<endl;
    cout<< "the peak index is "<<peakIndex2 <<endl;


    return 0;
}