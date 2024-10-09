from functools import reduce

class FunctionRecord:
    def __init__(self, funName):
        self.functionName = funName
        self.frequency = 0
        self.callers = []
        self.start = []
        self.finish = []
        self.avgTime = 0
        self.maxTime = 0
        self.minTime = 0
        self.args = []
        self.return_values = []
        self.cache_candidate = 1

    def getExecutionTime(self, index):
        return (self.finish[index] - self.start[index])
    
    def setCacheCandidate(self):
        # verificar que todos los argumentos sean iguales
        for i in range(1, len(self.args)):
            if self.args[i] != self.args[i-1]:
                self.cache_candidate = 0
                break
        # verificar que todos los valores de retorno sean iguales
        for i in range(1, len(self.return_values)):
            if self.return_values[i] != self.return_values[i-1]:
                self.cache_candidate = 0
                break

    def setRecordData(self):
        self.setAvgTime()
        self.setMaxTime()
        self.setMinTime()
        self.setCacheCandidate()

    def setAvgTime(self):
        self.avgTime = round(self.getAvgTime(), 3)

    def setMaxTime(self):
        self.maxTime = round(self.getMaxTime(), 3)

    def setMinTime(self):
        self.minTime = round(self.getMinTime(), 3)

    def getAvgTime(self):
        length = len(self.start)
        print(f"FunctionName: {self.functionName}")
        sum = reduce(lambda x, y: x + y, map(lambda x: self.getExecutionTime(x), range(length)))
        average = sum / length
        return average

    def getMaxTime(self):
        length = len(self.start)
        return max(map(lambda x: self.getExecutionTime(x), range(length)))

    def getMinTime(self):
        length = len(self.start)
        return min(map(lambda x: self.getExecutionTime(x), range(length)))

    def print_report(self):
        print("{:<30} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(self.functionName, self.frequency, self.avgTime, self.maxTime, self.minTime, self.cache_candidate, str(self.callers)))
