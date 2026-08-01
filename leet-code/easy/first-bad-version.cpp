using namespace std;

class Solution {
public:
    int firstBadVersion(int n) {
        long long left = 1, right = n, answer = 0;
        while (left <= right) {
            long long middle = (left + right) /2;
            if (isBadVersion(middle)) {
                answer = middle;
                right = middle - 1;
            }
            else {
                left = middle + 1;
            }
        }
        return answer;
    }
};