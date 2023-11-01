import threading

#glist
glist = []
for _ in range(500):
    glist.append(_)

alist = [0] * 5

def accumulate(startingIndex):
    global alist
    acc = 0
    start = glist[startingIndex * 100]
    end = glist[start + 99]

    for num in range(start, end + 1):
        acc += num
    
    alist[startingIndex] = acc

    threadID = threading.get_native_id()

    print(f"Accumulated value in thread [{threadID} -> {startingIndex}] is {acc}")

def startOrJoinThreads(listOfThreads, start):
    if(start):
        for thread in listOfThreads:
            thread.start()
    else:
        for thread in listOfThreads:
            thread.join()

def calTotal(alist):
    total = 0
    for num in alist:
        total += num
    return total

def main():

    listOfThreads = [_] * 5

    listOfThreads[0] = threading.Thread(target=accumulate, args=((0),))
    listOfThreads[1] = threading.Thread(target=accumulate, args=((1),))
    listOfThreads[2] = threading.Thread(target=accumulate, args=((2),))
    listOfThreads[3] = threading.Thread(target=accumulate, args=((3),))
    listOfThreads[4] = threading.Thread(target=accumulate, args=((4),))

    startOrJoinThreads(listOfThreads, 1)
    startOrJoinThreads(listOfThreads, 0)

    print(f"Total: {calTotal(alist)}")

if __name__ == "__main__":
    main()