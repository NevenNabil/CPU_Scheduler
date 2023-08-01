from queue import PriorityQueue
import queue

def init():
    global n4
    n4 = 0
    global q
    q = 0.0
    global totalBurstTime_RR
    totalBurstTime_RR = 0.0

class Process:
    def __init__(self, pid, arrival = 0, burst = 0):
        self.pid = int(pid)
        self.arrival = float(arrival)
        self.burst = float(burst)
        self.remaining = float(burst)
        self.departure = 0.0

    def __lt__(self, other):
        return self.arrival < other.arrival

    def waitingTime(self):
        return self.departure - self.arrival - self.burst


inputQueue_RR = PriorityQueue()
readyQ = []
outputQueue_RR = queue.Queue()
totalWaitingTime_RR = 0.0

def simulate_rr():
    global q
    global totalBurstTime_RR
    totalBurstTime_RR = 0.0
    totalWaitingTime_RR = 0.0

    #clear last outputs
    while not outputQueue_RR.empty():
        try:
            outputQueue_RR.get(False)
        except Empty:
            continue
        outputQueue_RR.task_done()    

    time = 0.0
    procs = []
        
    #output
    while (1):
        while not (inputQueue_RR.empty()):
            procs.append(inputQueue_RR.get())
            if (time >= procs[-1].arrival):
                readyQ.append(procs[-1])
                procs.pop(-1)

        if procs:
            for i in range(len(procs)):
                inputQueue_RR.put(procs[-(i+1)])
        procs = []

        if readyQ:   
            #slice 
            s = q if readyQ[0].remaining >= q else readyQ[0].remaining #slice
            s_pid = readyQ[0].pid
            s_arrival = readyQ[0].arrival
            time += s
            outputQueue_RR.put({'pid': s_pid, 'slice': s, 'arrival': s_arrival})
            
            #process to the end of the ready_queue or terminate
            readyQ[0].remaining -= s
            if (readyQ[0].remaining == 0):
                readyQ[0].departure = time
                print (time)
                totalWaitingTime_RR += readyQ[0].waitingTime()
                readyQ.pop(0)
            else:
                temp = readyQ[0]
                readyQ.append(temp)
                readyQ.pop(0)

        else:
            if not (inputQueue_RR.empty()):
                fp = inputQueue_RR.get()
                time = fp.arrival
                inputQueue_RR.put(fp)
            else: break  

    totalBurstTime_RR = time

    #print
    for n in list(outputQueue_RR.queue):
        print(n)
    global avgWaitingTime_RR
    avgWaitingTime_RR = round(totalWaitingTime_RR / int(n4), 3)
    print(avgWaitingTime_RR)



















    



