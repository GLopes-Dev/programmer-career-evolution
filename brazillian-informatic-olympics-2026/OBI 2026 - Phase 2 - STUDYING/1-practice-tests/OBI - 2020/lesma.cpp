#include <iostream>

using namespace std;

int main() {
    int A;
    int S;
    int D;
    int dias = 0;
    int total = 0;
    cin >> A >> S >> D;
    while (true) {
        dias += 1;
        total += S;
        if (total >= A) {
            break;
        }
        total -= D;
    }
    cout << dias << endl;

    return 0;
}