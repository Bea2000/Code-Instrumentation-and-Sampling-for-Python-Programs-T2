from __future__ import print_function
import threading
from time import sleep, time
import traceback
from sys import _current_frames
from functools import reduce

class Function:
    def __init__(self, name):
        self.name = name
        self.calls = 0
        self.children = {}
        self.parent = None


class Sampler:
    def __init__(self, tid) -> None:
        self.tid = tid
        self.t = threading.Thread(target=self.sample, args=())
        self.active = True
        self.stack = []
        self.tree = None
        
    def start(self):
        self.active = True
        self.t.start()
    
    def stop(self):
        self.active = False
        
    def checkTrace(self):
        for thread_id, frames in _current_frames().items():
            if thread_id == self.tid:
                frames = traceback.walk_stack(frames)
                stack = []
                for frame, _ in frames: 
                    code = frame.f_code.co_name
                    stack.append(code)
                stack.reverse()
                self.stack.append(stack)
                print(stack)  # Esta linea imprime el stack despues de invertirlo la pueden comentar o descomentar si quieren

    def sample(self):
        while self.active:
            self.checkTrace()
            sleep(1)

    def printReport(self):
        self.calculateTree()
        i = 1
        indent = "  "*i
        print(f"root ({len(self.stack)} seconds )")
        actual_node = self.tree
        print(f"{indent}{actual_node.name} ({len(self.stack)} seconds )")
        self.print_tree(actual_node, i+1)

    def print_tree(self, actual_node, i):
        indent = "  "*i
        if actual_node.children != {}:
            for child in actual_node.children.values():
                print(f"{indent}{child.name} ({child.calls} seconds )")
                self.print_tree(child, i+1)



    def calculateTree(self):
        # recorrer primera fila
        actual_node = Function(self.stack[0][0])
        actual_node.calls += 1
        self.tree = actual_node
        for i in range(1, len(self.stack[0])):
            actual_node.children[self.stack[0][i]] = Function(self.stack[0][i])  
            actual_node = actual_node.children[self.stack[0][i]]
            actual_node.calls += 1
        
        # recorrer filas
        for i in range(1,len(self.stack)):
            actual_node = self.tree
            len_stack = len(self.stack[i])
            for c in range(len_stack):
                if len_stack > c+1:
                    next = self.stack[i][c+1]
                    if next not in actual_node.children:
                        actual_node.children[next] = Function(next)
                        actual_node.children[next].parent = actual_node
                    actual_node = actual_node.children[next]
                    actual_node.calls += 1
                else:
                    break