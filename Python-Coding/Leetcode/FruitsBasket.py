'''You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''


'''
Solution:  

            Create a hashset to hold each occurrance of the trees. Increase the number as you see similar ones and decrease if you have seen it before.

            - Loop the trees for 2 times. 

            -Valid grouping is non zero tree number ( non zero fruits)
             - Keep two pointers left and right. 
            

'''
import collections
class solution: 
    def FruitsIntoBaskets( self, fruits: list[int])->int :
        counter = collections.defaultdict(int) 
        l , total ,res = 0,0,0

        for r in range(len(fruits)) :
            counter[fruits[r]] += 1   #increase the count if same fruit is found 
            total +=1 
        while len(counter) >2 :
            f=fruits[l]
            counter[f] -=1
            total -= 1
            l +=1
            if not counter[f
                counter.pop(f)
        res = max(res,total)
        return res
sol = solution()

result =sol.FruitsIntoBaskets([0,1,2,2])
print(result)

