
# if we try to open a file which doesn't exist, then it will go to exception block and print message

try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception  # This will go to line 12

except FileNotFoundError:  # not generic exception but specifically FileNotFound
    print('Sorry! file does not exist')
except Exception:
    print('something went wrong')
except Exception as e:
    print(e)
else:  # if try block doesnt throw exception
    print(f.read())  #RestTest, as file exist and flow doesn't go to exception block
    f.close()
finally:  # this block runs no matter what happens
    print('Executing finally....')
