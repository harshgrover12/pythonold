f = open('C:\\Users\\GHarsh\\Desktop\\sync_time.txt', 'r')
print(f.name)
print(f.read())
print(f.mode)
f.close()

with open('C:\\Users\\GHarsh\\Desktop\\sync_time.txt', 'r') as f:
    print(f.closed)  # False
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.readlines())  # returns list of all the lines
    print(f.tell())
    f.seek(0)
    print(f.readline())  # returns first line in the file
    for line in f:
        print(line, end='')
    print(f.tell())
    f.seek(0)
print(f.closed)   # True

with open('C:\\Users\\GHarsh\\Desktop\\sync_time.txt', 'r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f.tell())  # 10
    # while len(f_content) > 0:
    #     print(f_content, end='*')
    #     f_content = f.read(size_to_read)


########   writing to file ############
with open('test.txt', 'w') as f:
    f.write('Test')  # if file doesn't exist, it will create it, if file is already there it will override the content
    f.write('Test')  # TestTest
    f.seek(0)
    f.write('Rest')  #RestTest--Test at start will be overridden by Rest

# copying content of a file to another
with open('test.txt') as rf:  # By default 'r' will be mode.
    with open('test_copy.txt', 'w') as wf:
        for lin in rf:
            wf.write(lin)

# working with binary files
with open('C:\\Users\\GHarsh\\Desktop\\python.PNG', 'rb') as rf:
    with open('python1.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)