import os

def GetSongFileName(path):
    # Lấy ra tên file (bao gồm phần mở rộng)
    return os.path.basename(path)

def GetSongName(path):
    # Lấy ra tên file (không bao gồm phần mở rộng)
    return os.path.splitext(os.path.basename(path))[0]

# Ví dụ sử dụng
if __name__ == "__main__":
    file_path = r"d:\music\muabui.mp3"
    print(GetSongFileName(file_path))  
    print(GetSongName(file_path))      