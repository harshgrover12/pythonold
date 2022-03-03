from NameEqualToMain import first_module
# on running this file, there will be no print from imported file as check is
# added there to see if file name is __main__
print("Second Module's Name: {}".format(__name__))  # imported...Second Module's Name: __main__
