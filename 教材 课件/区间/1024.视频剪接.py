from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 对 clips 按起点升序排序
        clips.sort()
        st=0
        ed=time
        c=0
        i=0
        while i<len(clips):
            maxR=-1#重置！
            while i<len(clips) and clips[i][0]<=st:
                maxR=max(maxR,clips[i][1])
                i+=1#找左端点符合右端点最大的区间
            if maxR==-1:#一个也找不到 中间断了
                return-1
            st=maxR
            c+=1
            if maxR>=time:
                return c

        return -1
