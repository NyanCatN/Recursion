def reverse(inputpath, outputpath):
    
    with open(inputpath, "r") as f:
        contents = f.read()
    
    with open(outputpath, "w") as f:
        f.write(contents[::-1])

def copy(inputpath, outputpath):
    with open(inputpath, "r") as f:
        contents = f.read()

    with open(outputpath, "w") as f:
        f.write(contents)

def deplicate_contents(inputpath, n):
    contents = ""
    with open(inputpath, "r") as f:
        cont = f.read()

    with open(inputpath, "w") as f:
        for i in range(n):
            f.write(contents + cont)

def replace_string(inputpath, needle, newstring):
    with open(inputpath, "r") as f:
        contents = f.read()
    
    contents = contents.replace(needle, newstring)

    with open(inputpath, "w") as f:
        f.write(contents)


inputpath = "test.txt"
replace_string(inputpath, "H", "G")