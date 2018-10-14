#include <iostream>
using namespace std;

int sumSquare();
int squareSum();

int main(){
        cout << squareSum() - sumSquare();
        return 0;
}

int squareSum(){
        int sum = 0;
        for(int i=0; i<=10; i++){
                sum += i;
        }
return sum*sum;
}

int sumSquare(){
        int sum = 0;
        for(int i = 0; i<=10; i++){
                sum += i*i;
        }
return sum;
}
