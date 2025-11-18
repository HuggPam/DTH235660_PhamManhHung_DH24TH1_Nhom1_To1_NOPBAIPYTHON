import re

def NegativeNumberInStrings(s):
    # Tìm tất cả số nguyên âm, không tính dấu '--'
    negatives = re.findall(r'(?<!-)-\d+', s)
    for num in negatives:
        print(num)

# Ví dụ sử dụng
if __name__ == "__main__":
    test_str = "abc-5xyz-12k9l--p"
    NegativeNumberInStrings(test_str)