bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i=0;

    while(i < flowerbedSize) {

        if(flowerbed[i] == 1) {
            i=i+2; 
        } else if(i+1 < flowerbedSize && flowerbed[i+1] == 1){
            i=i+3;
        }
        else if(flowerbed[i] == 0) {
            n=n-1;
            i=i+2;
        }

    }

    if(n<=0) {
        return 1;
    } else {
        return 0;
    }
} 

// 解題:
//      在每一個點當下，可以做三種判斷
//          1. 如果已經種了，就直接判斷i+2的位置
//			2. 如果i+1位置有種，直接判斷i+3的位置
//			3. 如果沒有種，n-1再判斷i+2的位置