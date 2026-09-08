# 这题需要用到最小堆，最小堆是import heapq，使用的时候是先建立一个list，然后做heapq.heapqpop(list)或者heaqp.heapqpush(list, element)
# 观察选定的一组的workers的共同点，就是wage/quality=ratio是一样，paymen是ratio*sum(quality)，显然我们需要去找一组worker使得1、ratio小，2、sum(quality)小
# 对于ratio我们首先需要计算得到，那可以直接将ratio按递增排列（显然sum(quality)是不能排列的），然后我们以不断考察下一worker的quality，如果超过k，那么已选定的workers中
# 最大的那个退出，而想要做到每次都能得到quality最大的那个，需要用到最小堆（要得到最大的乘负号即可），所以最后会得到满足ratio尽量小并且sum(quality)尽量小的一组workers
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = []
        for i in range(len(quality)):
            workers.append((wage[i]/quality[i], quality[i]))
        workers.sort()

        queue = []
        quality_sum = 0
        ans = float("inf")
        for ratio, q in workers:
            heapq.heappush(queue, -q)
            quality_sum += q
        
            if len(queue) > k:
                remove = heapq.heappop(queue)
                quality_sum += remove
            
            if len(queue) == k:
                ans = min(ans, quality_sum * ratio)
        
        return ans



m = Solution()
print(m.mincostToHireWorkers([10,20,5],[70,50,30],2))
