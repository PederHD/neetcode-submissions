class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = dict()
        my_dict = dict()
        bucket[1]=[]
        biggest_bucket = 1
        for i,num in enumerate(nums):
            if num in my_dict:
                temp = my_dict[num]
                my_dict[num]+=1
                bucket[temp].remove(num)
                temp = temp+1
                if temp in bucket:
                    bucket[temp].append(num)
                else:
                    bucket[temp] =[num]
                if temp>biggest_bucket:
                    biggest_bucket = temp
            else: 
                my_dict[num]=1
                bucket[1].append(num)
                
        output = []
        while len(output)<k:
            temp_item = bucket[biggest_bucket]
            output.extend(temp_item)
            biggest_bucket -=1

        return output


            

            

        
               