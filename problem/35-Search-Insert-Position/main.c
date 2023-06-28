//Check the answer and write it...

int searchInsert(int* nums, int numsSize, int target){
    int i = 0, j = numsSize-1;
    int mid = -1;

    if(nums == NULL || numsSize == 0){
        return 0;
    }

    while(i <= j){
        mid = (i + j) / 2;

        if(nums[mid] == target){
            return mid;
        } else if(nums[mid] > target){
            j = mid - 1;
        } else if(nums[mid] < target){
            i = mid + 1;
        }
    }

    return i;
}
