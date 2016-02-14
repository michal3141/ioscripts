import sys, os
from multiprocessing import Process, Queue

# Command for running the simulation
JAVA_HOME = '/project/plab/tools/java/x86-GNU_Linux_64bit/jdk1.8.0_60/bin/java'
cmd = JAVA_HOME + ' -cp examples-assembly-1.0.jar pl.edu.agh.scalamas.examples.EmasApp | tail -1 >> out/%s_%s_%s'

# Defines the mesh for alpha-delta parameter space
DIVS_COUNT = 20
alphas = [x/float(DIVS_COUNT) for x in xrange(DIVS_COUNT+1)]
deltas = [x/float(DIVS_COUNT) for x in xrange(DIVS_COUNT)]

# Number of iterations in evolution
ITERS_COUNT = 10000
# Number of runs for particular alpha-delta parameters
RUNS_COUNT = 20 #30
# Number of processes that are running
NUM_OF_PROCESSES = 2

def process(q):
    while q.qsize > 0:
        try:
            alpha, delta = q.get(False)
        except:
            break
        a = str(alpha)
        b = str(delta)

        # Only setting environment....
        
        os.environ["ALPHA"] = a
        os.environ["DELTA"] = b

        print 'Executing for alpha=%s delta=%s iters=%s' % (a, b, ITERS_COUNT)
        os.system(cmd % (a, b, ITERS_COUNT))

if __name__ == '__main__':
    q = Queue()
    for alpha in alphas:
        for delta in deltas:
            for _ in xrange(RUNS_COUNT):
                q.put((alpha, delta))
    
    processes = [Process(target=process, args=(q,)) for _ in xrange(NUM_OF_PROCESSES)] 
    for p in processes:
        p.start()
    for p in processes:
        p.join()
