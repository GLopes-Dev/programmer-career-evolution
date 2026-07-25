#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    cin >> n;
    long long total = (n * (n + 1)) / 2;
    for (int i = 0; i < n - 1; i++) {
        int valor;
        cin >> valor;
        total -= valor;
    }
    cout << total << endl;
    return 0;
}