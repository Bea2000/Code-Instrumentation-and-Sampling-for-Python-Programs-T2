from profiler import *
import sys

if __name__ == '__main__':
    profiler = Profiler.profile("input_code/" + sys.argv[1] + ".py")
    profiler.calculate_report_data()
    profiler.print_fun_report()