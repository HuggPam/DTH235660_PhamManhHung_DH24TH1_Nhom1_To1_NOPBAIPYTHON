def analyze_string(s):
    vowels = "aeiouAEIOU"
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_special = 0
    count_space = 0
    count_vowel = 0
    count_consonant = 0

    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
        if c.isdigit():
            count_digit += 1
        if not c.isalnum() and not c.isspace():
            count_special += 1
        if c.isspace():
            count_space += 1
        if c.isalpha():
            if c in vowels:
                count_vowel += 1
            else:
                count_consonant += 1

    print("Số chữ IN HOA:", count_upper)
    print("Số chữ in thường:", count_lower)
    print("Số chữ là chữ số:", count_digit)
    print("Số chữ là ký tự đặc biệt:", count_special)
    print("Số chữ là khoảng trắng:", count_space)
    print("Số chữ là Nguyên Âm:", count_vowel)
    print("Số chữ là Phụ âm:", count_consonant)

if __name__ == "__main__":
    s = input("Nhập vào một chuỗi: ")
    analyze_string(s)