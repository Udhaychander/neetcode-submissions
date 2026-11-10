class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_count = 0 
        for count in task_counts.values():
            if count == max_frequency:
                max_count += 1
        minimum_cycles = (max_frequency - 1) * (n+1) + max_count
        return max(len(tasks), minimum_cycles)
 
