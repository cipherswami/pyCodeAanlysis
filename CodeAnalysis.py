import math
import time
import pstats
import psutil
import cProfile
import memory_profiler

# Code Profiling
def Profile():
    return cProfile.Profile()

def get_stats(pr):
    return pstats.Stats(pr).print_stats()

def get_ncalls(profile):
    return pstats.Stats(profile).total_calls

def get_exectime(profile):
    return pstats.Stats(profile).total_tt*1000

# Memory Profiling
def get_ram(func, *args, **kargs):
    return max(memory_profiler.memory_usage((func, args, kargs)))

def get_cpu(profile):
    ncalls = get_ncalls(profile)
    exectime = get_exectime(profile)/1000
    return ncalls*exectime

# Time Analysis
def timeNow():
    return time.process_time()

def delta_time(start_time, end_time):
    return (end_time - start_time)*1000

# Resources stats
def cpu_stats():
    return psutil.cpu_percent()

def ram_stats():
    return (psutil.virtual_memory().total - psutil.virtual_memory().available)*100 / psutil.virtual_memory().total

# Entropy function
def entropy(data):
    base = 2
    if len(data) <= 1:
        return 0
    myData = {}
    for d in data:
      if d not in myData:
        myData[d] = 0
      myData[d] += 1
    entropy = 0
    probs = [float(c) / len(data) for c in myData.values()]
    for p in probs:
        if p > 0.:
            entropy -= p * math.log(p, base)
    return entropy
