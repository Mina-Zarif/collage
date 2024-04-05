#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// R1 ==> number of rows in Matrix-1
// C1 ==> number of columns in Matrix-1
// R2 ==> number of rows in Matrix-2
// C2 ==> number of columns in Matrix-2

const int R1 = 2,C1 = 2, R2 = 2,C2 = 3;
void mulMat(int mat1[R1][C1], int mat2[R2][C2])
{
    int rslt[R1][C2];
 
    cout << "Multiplication of given two matrices is:\n";
 
    for (int i = 0; i < R1; i++) {   
        for (int j = 0; j < C2; j++) {
            rslt[i][j] = 0;   /// put init value = zero.

            for (int k = 0; k < R2; k++) {
                rslt[i][j] += mat1[i][k] * mat2[k][j];
            }
 
            cout << rslt[i][j] << "\t";
        }
        cout << "\n";
    }
}
 
int main()
{
  
    int mat1[R1][C1];
    int mat2[R2][C2];
    // int mat1[R1][C1] = { { 1, 1 }, { 2, 2 } };
    // int mat2[R2][C2] = { { 1, 1, 1 }, { 2, 2, 2 } };
    // expected output : 3    3    3    
    //                   6    6    6   
 
 
     for (int i = 0; i < R1; i++) {
        for (int j = 0; j < C1; j++) {
            mat1[i][j] = rand() % 10;  // Fill with random values
        }
    }

    for (int i = 0; i < R2; i++) {
        for (int j = 0; j < C2; j++) {
            mat2[i][j] = rand() % 10;  // Fill with random values
        }
    }


    if (C1 != R2) {
        cout << "The number of columns in Matrix-1 must "
                "be equal to the number of rows in "
                "Matrix-2\n";

        exit(EXIT_FAILURE);
    }
 
    
        cout << "Matrix A:" << endl;
       for (int i = 0; i < R1; i++) {
               for (int j = 0; j < C1; j++) {
                cout << mat1[i][j] << " ";
            }
            cout << endl;
        }

        cout << "Matrix B:" << endl;
        for (int i = 0; i < R2; i++) {
            for (int j = 0; j < C2; j++) {
                cout << mat2[i][j] << " ";
            }
            cout << endl;
        }
        
    mulMat(mat1, mat2);
}