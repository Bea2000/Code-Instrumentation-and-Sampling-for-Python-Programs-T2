import time
from function_record import *
from abstract_profiler import AbstractProfiler


class Profiler(AbstractProfiler):

    def __init__(self):
        self.records = {}
        self.callers = {}
        self.last_called = []
    
    # search a record by name
    def get_record(self, functionName):
        if functionName not in self.records:
            self.records[functionName] = FunctionRecord(functionName)
        return self.records[functionName]

    # metodo se llama cada vez que se ejecuta una funcion    
    def fun_call_start(self, functionName, args):
        record = self.get_record(functionName) #record de foo
        record.frequency += 1
        record.start.append(time.time())
        record.args.append(args)
        # revisamos de donde viene
        if len(self.last_called) != 0:
            last_called = self.last_called[-1]
            if last_called not in record.callers:
                record.callers.append(last_called)
        # agregamos a la lista de llamadas
        self.last_called.append(functionName)

    def fun_call_end(self, functionName, returnValue):
        record = self.get_record(functionName)
        record.finish.append(time.time()) 
        record.return_values.append(returnValue)      
        self.last_called.pop()
    
    def calculate_report_data(self):
        for record in self.records.values():
            record.setRecordData()

    # print report
    def print_fun_report(self):
        print("{:<30} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('fun', 'freq', 'avg', 'max', 'min',
                                                                        'cache', 'callers'))
        for record in self.records.values():
            record.print_report()


