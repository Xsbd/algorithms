# python3
import math

class PriorityQueue:		# min-heap based Priority Queue
    def __init__(self):
        self._data = []
        self._priority = []

    def ReadData(self, n, data, priority):
        self._data = data
        self._priority = priority
        assert n == len(self._data)
        assert n == len(self._priority)
        PriorityQueue.SortQueue(self)

    def SortQueue(self):
        for i in range(math.ceil(len(self._priority)/2)-1, -1, -1):
            PriorityQueue.ShiftDown(self,i)

    def ShiftDown(self,i):
        minIndex = i
        l = 2*i+1
        if l< len(self._priority) and (self._priority[l] < self._priority[minIndex] or (self._priority[l] == self._priority[minIndex] and self._data[l] < self._data[minIndex])):
            minIndex = l
        r = 2*i+2
        if r< len(self._priority) and (self._priority[r] < self._priority[minIndex] or (self._priority[r] == self._priority[minIndex] and self._data[r] < self._data[minIndex])):
            minIndex = r
        if i != minIndex:
            self._priority[i], self._priority[minIndex] = self._priority[minIndex], self._priority[i]
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            PriorityQueue.ShiftDown(self,l)
            if r< len(self._priority):
                PriorityQueue.ShiftDown(self,r)

    def ShiftUp(self, i):
        parent_id = math.ceil(i/2)-1
        while i!=0:
            if (self._priority[i] < self._priority[parent_id]) or (self._priority[i] == self._priority[parent_id] and 
self._data[i] < self._data[parent_id]):
                self._priority[i], self._priority[parent_id] = self._priority[parent_id], self._priority[i]
                self._data[i], self._data[parent_id] = self._data[parent_id], self._data[i]
            i, parent_id = parent_id, math.ceil(parent_id/2)-1

    def NextJob(self, process_time):
        ret1, ret2  = self._data[0], self._priority[0]
        self._priority[0] += process_time
        if self._priority[0] < self._priority[math.ceil(len(self._priority)/2)-1]:
            PriorityQueue.ShiftDown(self,0)
        else:
            self._data[0], self._data[-1] = self._data[-1], self._data[0]
            self._priority[0], self._priority[-1] = self._priority[-1], self._priority[0]
            self._data.pop(-1)
            self._priority.pop(-1)
            PriorityQueue.ShiftDown(self,0)
            PriorityQueue.Insert(self, ret1, ret2 + process_time)
        return ret1,ret2

    def Insert(self, key, priority):
        self._data.append(key)
        self._priority.append(priority)
        PriorityQueue.ShiftUp(self, len(self._priority)-1)

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.assigned_workers)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        # self.assigned_workers = [None] * len(self.jobs)
        # self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]
        threads = PriorityQueue()
        if self.num_workers > len(self.jobs):
            self.assigned_workers = [i for i in range(len(self.jobs))]
            self.start_times = [0 for i in range(len(self.jobs))]
            return
        else:
            threads.ReadData(self.num_workers, [i for i in range(self.num_workers)], [self.jobs[i] for i in range(self.num_workers)])
            self.assigned_workers, self.start_times = [i for i in range(self.num_workers)], [0 for i in range(self.num_workers)]
            del self.jobs[:self.num_workers]
        while self.jobs:
#            print(threads._data, threads._priority)
            process_time = self.jobs.pop(0)
            thread, end_time = threads.NextJob(process_time)
            self.assigned_workers.append(thread)
            self.start_times.append(end_time)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
