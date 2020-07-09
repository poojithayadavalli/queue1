 def leastInterval(s, n):
      taskMap = {}
      # Simply make hashmap which is used for storing frequencies of tasks
      for task in s:
          taskMap[task] = taskMap.get(task, 0) + 1
      # Sort it to find the task which occurs Maximum
      maxList = sorted(taskMap.values(), reverse=True)
        
      maxNum = maxList[0]
        
      i, maxTaskCounter = 0, 0
      # Now find how many tasks are there which occur maximum number of times after we founded maxFrequency above
      while i < len(maxList) and maxList[i] == maxNum:
          maxTaskCounter += 1
          i += 1
      # The formula that we derived after taking different cases as aboove
      intervals = (maxNum - 1) * (n + 1) + maxTaskCounter
      # Finally the formula doesn'y hold for some cases like  (ABCABCDEFG) so we take the max of len(tasks) to get our final answer
      return max(intervals, len(s))
     
tasks=input().split(",")
n=int(input())
print(leastIntervals(tasks,n))
