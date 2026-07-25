#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int n;
    vector<int> numbers;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int valor;
        cin >> valor;
        numbers.push_back(valor);
    }
    sort(numbers.begin(), numbers.end());
    for (int num : numbers) {
        cout << num << " ";
    }
    
    return 0;
}