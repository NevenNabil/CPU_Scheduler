from queue import PriorityQueue
import queue

def init():
    global n1
    n1 = 0

class Process:
    def __init__(self, pid, arrival = 0, burst = 0):
        self.pid = int(pid)
        self.arrival = float(arrival)
        self.burst = float(burst)
        self.departure = 0.0

    def __lt__(self, other):
        return self.arrival < other.arrival

    def waitingTime(self):
        return self.departure - self.arrival - self.burst


inputQueue = PriorityQueue()
outputQueue = queue.Queue()
totalWaitingTime = 0.0

def simulate_fcfs():
    #clear last inputs
    while not outputQueue.empty():
        try:
            outputQueue.get(False)
        except Empty:
            continue
        inputQueue.task_done()    

    time = 0.0
    global totalWaitingTime
    totalWaitingTime = 0.0
        
    #output
    while not inputQueue.empty():
            p = inputQueue.get()
            time = p.burst + (time if p.arrival <= time else p.arrival)
            p.departure = time
            totalWaitingTime += p.waitingTime()
            outputQueue.put({'pid': p.pid, 'burst': p.burst, 'arrival': p.arrival})

    global totalBurstTime
    totalBurstTime = time

    #print
    for n in list(outputQueue.queue):
        print(n)
    global avgWaitingTime
    avgWaitingTime = round(totalWaitingTime / int(n1), 3)
    print(avgWaitingTime)



















    



