import os
import time
import requests

print("Текущая деректория:", os.getcwd())
print("Все папки и файлы:", os.listdir())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


requests.get("https://ironchampion.ru", verify=False)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
