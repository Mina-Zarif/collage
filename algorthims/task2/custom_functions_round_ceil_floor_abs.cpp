#include <iostream>

using namespace std;

// Function to calculate the absolute value of a number
double customAbs(double number) {
    return (number < 0) ? -number : number;
}

// Function to round a number to the nearest integer
double customRound(double number) {
    double decimalNumber = number - (int)(number);
    if(decimalNumber >= 0.5)  return (int)number + 1;    
    else if(decimalNumber <= -0.5)  return (int) number - 1;
    return (int)number;
   
}

// Function to find the ceiling of a number
double customCeil(double number) {
    double decimalNumber = (number - (int)(number));
    return (decimalNumber <= 0) ? (int) number : (int)number + 1;
}

// Function to find the floor of a number
double customFloor(double number) {
    double decimalNumber = (number - (int)(number));
    return (decimalNumber >= 0) ? (int)number  : (int) number - 1;
}



int main() {


    double number = 12.28;
    cout << "Number: " << number  << endl;

    // Custom round function
    double rounded = customRound(number);
    cout << "Custom Rounded: " << rounded << endl;

    // // Custom ceiling function
    double ceiling = customCeil(number);
    cout << "Custom Ceiling: " << ceiling << endl;

    // // Custom floor function
    double flooring = customFloor(number);
    cout << "Custom Floor: " << flooring << endl;

    // // Custom absolute value function
    double absolute = customAbs(number);
    cout << "Custom Absolute Value: " << absolute << endl;

    return 0;
}
