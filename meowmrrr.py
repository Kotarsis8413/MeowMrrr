def log(text):
    print(text)
def filework(filename , opentype):
    if opentype == 'w':
        f = open(filename, 'w')
        filecontent = input('content~')
        f.write(filecontent)
        f.close()
    if opentype == 'r':
        f = open(filename, 'r')
        print(f.read())
def wait(timewait):
    import time
    print('please wait ' + str(timewait) + ' second')
    time.sleep(timewait)
def close(closelog):
    import sys
    sys.exit('programm closed, reason: ' + closelog)

