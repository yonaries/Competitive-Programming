function insertionSort1(n: number, arr: number[]): void {
    let key, j;
    for(let i = 1; i < n; i++) {
        key = arr[i];
        j = i-1;
        
        while(j>=0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
            console.log(arr.join(' ')); 
        }
        arr[j+1] = key;
    }
    console.log(arr.join(' ')); 
}
