#include <stdio.h>

// f(n) = sum(f 0 to n-1) % 13
int f(int n) {
    if (n==0) return 1;
    if (n==1) return 1;
    int sum = 1;
    for (int i = 0; i < n - 1;i++)
        sum = (2 * sum) % 13;
    return sum;
}

int main(){
    char ans[] = "rgjgmbuyhbfcx";
    for (int i = 0; i < 13; i++)
        ans[i] ^= f(13 + i * i * i);
    puts(ans);
}
