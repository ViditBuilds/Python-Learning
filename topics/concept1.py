# we used to study in this is funtion 

def student_info(name , age , Mark1 , Mark2, Mark3 , Mark4, Mark5   ):   


    total = ( Mark1+Mark2+Mark3+Mark4+Mark5 )
    average = (Mark1+Mark2+Mark3+Mark4+Mark5)/5
    print("name:" , name )
    print("age:" , age  )
    print(" Mark1:" , Mark1) 
    print(" Mark2:" , Mark2) 
    print(" Mark3:" , Mark3) 
    print(" Mark4:" , Mark4) 
    print(" Mark5:" , Mark5)  
    print("total:" , total)
    print(" average:" , average) 

student_info("vidit " , 19 , 91 , 78 , 85 , 89 ,60 )


# method 2  

def std_info(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return average

name = input("Enter Your Name: ")
roll_no = int(input("Roll no.: ")) 

m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

result = std_info(m1, m2, m3, m4, m5)

print("Student Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", m1 + m2 + m3 + m4 + m5)
print("Average Marks:", result)