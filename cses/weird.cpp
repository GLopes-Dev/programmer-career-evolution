#include <iostream>
#include <list>

int main() {
    long long n;
    std::cin >> n;
    std::list<long long> numbers;
    while (n != 1) {
        numbers.push_back(n);

        if (n % 2 == 0) {
            n = n / 2;
        }
        else {
            n = n * 3 + 1;
        }
    }
    numbers.push_back(1);
    for (long long num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}