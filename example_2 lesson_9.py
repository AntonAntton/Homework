import os

my_path = 'D:\\Hillel'


def file_crawl(path, level=1):
    print("Level =", level, "Content:", os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print("Down", path + '\\' + i)
            file_crawl(path + '\\' + i, level + 1)
            print('back to', path)


file_crawl(my_path)