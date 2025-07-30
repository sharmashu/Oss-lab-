#include <iostream>
using namespace std;

int main() {
    int number, reversedNumber = 0;

    cout << "Enter a three-digit number: ";
    cin >> number;

    if (number >= 100 && number <= 999) {
        while (number != 0) {
            int digit = number % 10;
            reversedNumber = reversedNumber * 10 + digit;
            number /= 10;
        }
        cout << "Reversed number: " << reversedNumber << endl;
    } else {
        cout << "Please enter a valid three-digit number." << endl;
    }