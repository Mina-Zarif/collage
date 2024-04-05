#include <iostream>
using namespace std;

// Function to swap two numbers using call by reference
void swapNumbers(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int num1 = 10;
    int num2 = 20;

     cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    // Call the swapNumbers function to swap the values of num1 and num2
    swapNumbers(num1, num2);

   cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    return 0;
}