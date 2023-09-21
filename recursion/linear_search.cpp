#include<iostream>

using namespace std;

// Linear search using recursion

int linearSearch(int arr[], int size, int item, int index){
    if(index >= size){
        return -1;
    }
    if(arr[index] == item){
        return index;
    }else{
        return linearSearch(arr, size, item, index+1);
    }
    
    
}

int main(){

    int arr[] = {1,2,3,4,5,15,11};
    int size = sizeof(arr)/sizeof(arr[0]);
    int item = 22;

    int index = linearSearch(arr, size, item, 0);
    if(index == -1){
        cout<<item<<" does not exists"<<endl;
    }else{
        cout<<item<<" is found at index "<<index<<endl;
    }

    return 0;
}