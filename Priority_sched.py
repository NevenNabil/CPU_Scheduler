global N3
N3 = 0
global preemptive__2

global process
process = []
global OutputPriority
OutputPriority=[]
global time
time = 0.0
global avg_waiting_time_pri
avg_waiting_time_pri = 0.0

#sampling time

#sorting according to arrival time and priority
def simulate_pri():
    global N3
    n3 = N3
    global time
    time = 0.0
    total_waiting_time = 0.0
    global avg_waiting_time_pri
    global OutputPriority
    OutputPriority.clear()
    # print(process)

    min_burst = min(obj['burst time'] for obj in process)
    to = float(min_burst)* 0.1

    for i in range(0, int(n3)):
        for j in range(i+1, int(n3)):
            if(process[i]['arrival time']>process[j]['arrival time']):
                temp = process[i];
                process[i] = process[j];
                process[j] = temp;
            elif (process[i]['arrival time'] == process[j]['arrival time'] and process[i]['priority'] > process[j]['priority']):
                temp = process[i];
                process[i] = process[j];
                process[j] = temp;


    if int(preemptive__2) == 0:
        for i in range(int(n3)):
            OutputPriority.append({'process' :process[i]['process'], 'arrival' :process[i]['arrival time'],'length' :process[i]['burst time']})
            time = OutputPriority[-1]['length'] + (time if process[i]['arrival time'] <= time else process[i]['arrival time'])
            departure = time 
            total_waiting_time += departure - process[i]['arrival time'] - process[i]['burst time']
            print("test")

    else:
        current_process = process[0]
        burst_time = current_process['burst time']
        length = 0
        current_time=0

        while(1):
            print (burst_time)
            print(current_time)
            current_time += to
            burst_time -= to
            length += to

            #deleting the process when it is done and new current process
            if(burst_time <= 0):
                length = length + burst_time
                OutputPriority.append({'process': current_process['process'], 'arrival' : current_process['arrival time'], 'length': round(length,3)})
                time = OutputPriority[-1]['length'] + (time if current_process['arrival time'] <= time else current_process['arrival time'])
                departure = time 
                total_waiting_time += departure - current_process['arrival time'] - current_process['burst time']

                process.pop(0)
                n3 = n3-1
                if (n3 == 0):break

                #rearrange the priority according to current time and priority and arrival time
                for i in range(0, int(n3)):
                    for j in range(i + 1, int(n3)):
                        if (current_time >= process[j]['arrival time'] and process[i]['priority'] >process[j]['priority']):
                            temp = process[i];
                            process[i] = process[j];
                            process[j] = temp;
                current_process = process[0]
                burst_time = current_process['burst time']
                length = 0
            else:
                print("hello")
                # switch context and swapping current process if arrival time = current time and of higher priority
                for i in range(1,int(n3)):
                    if(current_time >= process[i]['arrival time'] and current_process['priority'] > process[i]['priority']):
                        pp = current_time - process[i]['arrival time']
                        current_time = process[i]['arrival time']
                        process[0]['burst time'] = burst_time + pp #pp is the impurities
                        OutputPriority.append({'process': current_process['process'], 'arrival' : current_process['arrival time'], 'length': round(length - pp,3)})
                        time = OutputPriority[-1]['length'] + (time if current_process['arrival time'] <= time else current_process['arrival time'])
                        departure = time 
                        total_waiting_time += departure - current_process['arrival time'] - current_process['burst time']

                        temp=current_process
                        current_process = process[i]
                        process[0]=current_process
                        process[i]=temp
                        burst_time = current_process['burst time']
                        length = 0

            if (n3 == 0): break



    avg_waiting_time_pri = round(total_waiting_time / N3, 3)
    print('output is',OutputPriority)
    print(avg_waiting_time_pri)



