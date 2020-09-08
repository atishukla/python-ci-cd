from another_mod import _private_sub
from another_mod import main

def calling():
    print(_private_sub())
    print(main())


if __name__ == '__main__':
    calling()