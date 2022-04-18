def small_number(nums):
    i=0
    minimum=nums[i]
    while i<len(nums):
        if nums[i]<minimum:
            minimum=nums[i]
        i=i+1
    return(minimum)
print(small_number([8,6,4,8,4,50,20,7]))