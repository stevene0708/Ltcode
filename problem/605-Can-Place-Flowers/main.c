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