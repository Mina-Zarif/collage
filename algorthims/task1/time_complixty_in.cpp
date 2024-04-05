#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main() {

    high_resolution_clock::time_point start_time = high_resolution_clock::now();
    ///// your algorithm 
    high_resolution_clock::time_point end_time = high_resolution_clock::now();
    duration execution_time = duration_cast<microseconds>(end_time - start_time);
    cout << "Execution Time: " << execution_time.count() << " microseconds" << endl;
    
    return 0;
}