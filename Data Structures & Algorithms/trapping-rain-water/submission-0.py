class Solution:
    def trap(self, height: List[int]) -> int:
        def l_g(height,k):
            l_g_map = []
            l_g_ele = 0
            for i in height:
                l_g_map.append(l_g_ele)
                l_g_ele = max(l_g_ele, i)
            return l_g_map[k]
        def r_g(height, k):
            r_g_map = [0] * len(height)
            r_g_ele = 0
            for i in range(len(height)-1,-1,-1):
                r_g_map[i] = r_g_ele
                r_g_ele = max(r_g_ele, height[i])
            return r_g_map[k]

        t_t_water = 0
        for i in range(len(height)):
            t_t_water += max(0,max(0,min(l_g(height, i), r_g(height, i))) - height[i])
        
        return t_t_water