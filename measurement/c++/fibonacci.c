#include <iostream>
#include <vector>
#include <cstdlib> // For atoi function

class BigInteger {
public:
    BigInteger(int n) {
        while (n > 0) {
            digits.push_back(n % base);
            n /= base;
        }
    }

    void add(const BigInteger& other) {
        int carry = 0;
        for (size_t i = 0; i < std::max(digits.size(), other.digits.size()) || carry; i++) {
            if (i == digits.size())
                digits.push_back(0);

            int sum = digits[i] + carry;
            if (i < other.digits.size())
                sum += other.digits[i];

            digits[i] = sum % base;
            carry = sum / base;
        }
    }

    std::string toString() const {
        std::string result;
        if (digits.empty())
            return "0";

        for (int i = digits.size() - 1; i >= 0; i--)
            result += std::to_string(digits[i]);

        return result;
    }

private:
    static const int base = 1000000000; // Each element of digits can hold 9 digits (base 10^9)
    std::vector<int> digits;
};

BigInteger fibonacci(int n) {
    if (n <= 0) {
        std::cout << "Invalid input. Please provide a positive integer." << std::endl;
        exit(1);
    } else if (n == 1) {
        return BigInteger(0);
    } else if (n == 2) {
        return BigInteger(1);
    } else {
        BigInteger prev = BigInteger(0);
        BigInteger current = BigInteger(1);
        for (int i = 3; i <= n; i++) {
            BigInteger next = current;
            next.add(prev);
            prev = current;
            current = next;
        }
        return current;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " <positive_integer>" << std::endl;
        return 1;
    }

    int num = std::atoi(argv[1]);
    BigInteger result = fibonacci(num);
    std::cout << "The Fibonacci number at position " << num << " is: " << result.toString() << std::endl;

    return 0;
}
