import time
filename = input("type file: ")
if (filename[len(filename)-4:len(filename)] != ".bad") and (filename[len(filename)-5:len(filename)] != ".bad/"):
    print("Warning: Filename not a .bad!")
thing = open(filename,"r")
variables = {"ifvar": 0}
linenum = 0
nextif = -1
for line in thing:
    variables["ifvar"] = nextif
    linenum += 1
    if line[:6] == "print ":
        if line[6:7] == "_":
            print(line[7:(len(line)-2)])
        else:
            if line[6:len(line)-1] not in variables:
                print("Error in line "+str(linenum)+": Undefined variable")
                quit()
            else:
                print(variables[line[6:len(line)-1]])
    elif line[:5] == "wait ":
        time.sleep(int(line[5:len(line)])/100)    
    elif line[:6] == "input(":
        if not line.find("?"):
            print("Error in line "+str(linenum)+": Missing ?")
            quit()
        inp = line[6:(len(line)-2)]
        inputstr = inp.split("?")[0]
        variables[inp.split("?")[1]] = input(inputstr + " ")
    elif line[:3] == "if ":
        if not (line.find("==")):
            print("Error in line "+str(linenum)+": Missing comparison")
            quit()
        check = line[3:len(line)-1]
        ifstr = check.split("==")[0]
        if ifstr in variables:
            ifstr = variables[ifstr]
        ofstr = check.split("==")[1]
        if ofstr in variables:
            ofstr = variables[ofstr]
        if ifstr == ofstr:
            nextif = 1
        else:
            nextif = 0
    elif line[:7] == "setvar(":
        if not line.find("?"):
            print("Error in line "+str(linenum)+": Missing ?")
            quit()
        var = line[6:(len(line)-2)]
        varstr = var.split("?")[0]
        variables[varstr] = var.split("?")[1]
    elif line[:2] == "//":
        pass
    else:
        print("Error in line ",str(linenum),": Unrunnable code")
        quit()