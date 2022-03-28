# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import literals as msg
import functions as f
import libreria

def main():
    ans = 0
    x = libreria.validate(msg.MENU, 1, 2)
    match x:
        case 1:
            file = input(msg.MSG0)
            f.crear(file, msg.EXT2)
        case _:
            file = input(msg.MSG0)
            f_name = f.crear(file, msg.EXT2)
            head = f.verificar(f_name)
            if head == 1:
                ans = libreria.validate(msg.MSG1, 0, 1)
            if ans == 1:
                f.introduir(f_name, head, 'w')
                f.introduir1(f_name, head, 'a')
                f.introduir2(f_name, head, 'a')
            else:
                f.introduir(f_name, head, 'a')
                f.introduir1(f_name, head, 'a')
                f.introduir2(f_name, head, 'a')
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
