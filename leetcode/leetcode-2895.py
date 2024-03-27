class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        return max(time + task
               for (time, task) in zip(sorted(processorTime), sorted(tasks)[::-4]))