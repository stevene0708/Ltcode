int arrayPairSum(int* nums, int numsSize){
    int temp=0;
    int sum=0;

    for(int i=0; i<numsSize-1; i++) {
        for(int j=0; j<numsSize-i-1; j++){
            if(nums[j] > nums[j+1]) {
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        }
    }

    for(int i=0; i<numsSize; i++) {
        printf("%d", nums[i]);
        if(i%2==0) { 
            sum+=nums[i];
        }
    }

    return sum;
}

// 使用bubble sort太慢，會time limited
// 暫時先這樣放著