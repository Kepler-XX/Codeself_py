import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()  # 获得选择好的文件夹
file_path = filedialog.askopenfilename()  # 获得选择好的文件

print(f'{folder_path}')
print(f'{file_path}')
