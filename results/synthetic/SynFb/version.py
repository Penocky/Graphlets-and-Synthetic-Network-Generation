import os
def formatter(files, n):
    if len(str(n)) == 1:
        print("\n " + str(n) + ":", end="  ")
    else:
        print("\n" + str(n) + ":", end="  ")

    xcord = 1

    k = [3, 4, 5]   # values of graphlets

    k3 = [2, 3]
    k4 = [3, 6, 7, 8, 9, 10]
    k5 = [4, 10, 11, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    for i in k:
        regex = "-k"+str(i)+".txt"
        filename = [x for x in files if regex in x][0]
        #print(filename)
        samples = 200000
        store = {}

        consider = []
        if i == 3:
            consider = k3
        elif i == 4:
            consider = k4
        elif i == 5:
            consider = k5

        mfile = open(filename, 'r')
        #print("file opened")
        for line in mfile.readlines():
            line = line.strip()
            if len(line) < 1:
                continue
            a, b = tuple(map(int, line.split()))
            if b in consider:
                store[b] = a

        #print(store)
        for typ in consider:
            #print("%.3f" % ((store[typ]/samples) * 100), end="/")
            print("(" + str(xcord) + ",%.2f)" % ((store[typ]/samples) * 100), end="")
            xcord += 1


    print()
    print()
    print()



files = [f for f in os.listdir('.') if os.path.isfile(f)]
n9 = [x for x in files if "syn-9-" in x]
n10 = [x for x in files if "syn-10-" in x]
n11 = [x for x in files if "syn-11-" in x]
n12 = [x for x in files if "syn-12-" in x]

formatter(n9, 9)
formatter(n10, 10)
formatter(n11, 11)
formatter(n12, 12)
print()
