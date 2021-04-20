from mymath import add_numbers
from person import Person

name = "kamil"
name1 = 'Jamila'
name2 = 'kora'
name3 = 'korea'

def ola(name: str):
    print(name.upper())

def alex_method(name):
    p = Person(name)
    print(p)

if __name__ == '__main__':
    # todo : fix bug here
    # todo : 고쳐서 사용
    print("Ola")
    print("Ola")
    stuname = "Ahmed"
    print("%s" % stuname)
    print(add_numbers(4, 3))
    alex_method("ali")

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
