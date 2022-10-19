def filework(filename , opentype):
    if opentype == 'w':
        f = open(filename, 'w')
        filecontent = input('content~')
        f.write(filecontent)
        f.close()
    if opentype == 'r':
        f = open(filename, 'r')
        print(f.read())
def wait(timewait, waittext):
    import time
    print(waittext + str(timewait))
    time.sleep(timewait)
def close(closelog):
    import sys
    sys.exit('programm closed, reason: ' + closelog)

class cmd:
    def log(text):
        print(text)
    def close(closelog):
        import sys
        sys.exit('programm closed, reason: ' + closelog)
console = cmd

class f:
    def read(filename):
        fileopen = open(filename, 'r')
        console.log(fileopen.read())
        fileopen.close()
    def edit(filename, content):
        fileopen = open(filename, 'w')
        fileopen.write(content)
        fileopen.close()

filee = f






