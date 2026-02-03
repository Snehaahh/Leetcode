def countResponseTimeRegressions(responseTimes):
    count = 0
    for i in range(1,len(responseTimes)):
        sum = 0
        avg = 0
        for n in range(i-1,-1,-1):
            sum += responseTimes[n]
        avg = sum / i
        if responseTimes[i] > avg:
            count += 1
            
    return count
