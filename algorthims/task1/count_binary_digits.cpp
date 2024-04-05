#include <iostream>
#include <cmath> 
#include <chrono>

using namespace std;
using namespace std::chrono;

// Function to count the number of binary digits for a given number
int countBinaryDigits(int number) {

    return (int)log2(number)+1; 

    // int count = 0;
    // while (number > 0) {
    //     number >>= 1;  // number /= 2;
    //     count++;
    // }
    // return count;
}

int main() {

    // Input number for which you want to count binary digits
    int number = 10;

    high_resolution_clock::time_point start_time = high_resolution_clock::now();
    int binary_digits_count = countBinaryDigits(number);
    high_resolution_clock::time_point end_time = high_resolution_clock::now();
    auto execution_time = duration_cast<microseconds>(end_time - start_time);

    cout << "Number: " << number << endl;
    cout << "Number of Binary Digits: " << binary_digits_count << endl;


    return 0;
}
