
# When Python file is run directly, then python will see name of the module as main.

def main():
    print("First Module's Name: {}".format(__name__))  # First Module's Name: __main__


if __name__ == '__main__':
    main()
else:
    print("imported")