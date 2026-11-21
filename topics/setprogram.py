# Set programming code in python : 
nums = [ 1,2,3,4,5,6]
print("type ; " , type(nums)) 
# print("empty set: " , set()) # this is empty set in this code 
 
#  *************************** Adding Method - 1 :  **************************
nums.append(12)
print(nums)

# but append is not the tuple so dont compare it with update 


#  *************************** Adding Method - 2  :  **************************
print("type:" , type(nums))
print(nums)

#  *************************** Adding Method - 3 by using update  :  **************************

nums.update(28,29,30)
print("update:" , type(nums))
print(nums)