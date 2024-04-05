#include <iostream>
#include <vector>

using namespace std;
 
bool isPrime(int n)
{
    // O(n)

    // Corner case
    if (n <= 1)
        return false;
 
    // Check from 2 to n-1
    for (int i = 2; i <= n / 2; i++)
        if (n % i == 0)
            return false;
 
    return true;
}

bool SieveOfEratosthenes(int n) 
{ 

    // O(n*log(log(n)))

   bool isPrime = false;

    vector<bool> prime(n + 1,true);
  
    for (int p = 2; p * p <= n; p++) { 
        // If prime[p] is not changed, then it is a prime 
        if (prime[p] == true) { 

            for (int i = p * p; i <= n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    // Print all prime numbers 
    for (int p = 2; p <= n; p++) {
        if (prime[p]) { 
            // cout << p << " ";  
            if(p == n)
            {
                isPrime = true;
            }
        }
    }
    return isPrime;
            
} 

int main()
{
    isPrime(11) ? cout << " true\n" : cout << " false\n";
    isPrime(15) ? cout << " true\n" : cout << " false\n";
    return 0;
}