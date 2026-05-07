'''
                Leet code Problem : 11

                You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1



'''



'''
       Brute force : Have two loops one for left and another for right 

       Calculate the area of the square for holding the water from left and right my multiplying each point with other O(n2)


       Better approach : 

       Use two pointer method, find the max of each pointer.

       If the left is larger , decrease the right pointer position by 1 and vise versa.

       This approach is O(n)

'''



class solution:
    def Container_water(self, height:list[int])->int :
        area = 0
        res = 0
        left = 0
        right = len(height) -1

        while (left<right) :
            area = (right-left)  * min(height[left],height[right])
            res = max(res,area)


            if(height[left]<height[right]):
                left +=1

            else :
                right -=1

        return res
sol = solution()

result = sol.Container_water([1,8,6,2,5,4,8,3,7])

print(result)

