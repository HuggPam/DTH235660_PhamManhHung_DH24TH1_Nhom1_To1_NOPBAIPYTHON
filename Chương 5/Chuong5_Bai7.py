def OptimizeNounString(s):
    # Loại bỏ khoảng trắng dư thừa và chuẩn hóa từng từ
    words = s.strip().split()
    optimized = ' '.join(word.capitalize() for word in words)
    return optimized

# Ví dụ sử dụng
if __name__ == "__main__":
    input_str = " PHạm hỮu Huy "
    print(OptimizeNounString(input_str))  