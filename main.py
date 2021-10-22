from generators import pigeonProblem
from View import ViewConsole

def main():

    pigeonProblem.generate_file(3)
    VC = ViewConsole()
    test = True
    while test:
        test = VC.action()

if __name__ == '__main__':
    main()

