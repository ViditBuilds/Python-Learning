
# Shopping Mall Billing System

def calculate_bill(price , quantity) : 
    bill = price * quantity 
    return bill 

def apply_discount(bill):
    if bill>10000 : 
        discount = bill*15/1000 

    elif bill>5000 : 
        discount = bill * 10/100 

    else : 
        discount = 0 

    return 0 ; 

def display_bill( name , price ,bill ,quantity , discount ): 
    final_amount = bill - discount  
    print("\n-------final Bill -------- ")  
    print("product:", name ) 
    print("price:", price )
    print("bill:", bill ) 
    print("quantity:" , quantity)  
    print("discount: " , discount)   

    


name =input("Enter Your Name : ")
price = float(input("Enter Product Price:"))
quantity = float(input("Enter Your quantity:")) 

bill = calculate_bill(price , quantity )
discount = apply_discount(bill)
display = display_bill(name , price , bill , quantity , discount )  











