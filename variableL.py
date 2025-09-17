def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4))  
print(sum_numbers(5))            
print(sum_numbers())    


def find_max(*args):
    if not args:   
        return None
    maximum = args[0]
    for num in args[1:]:
        if num > maximum:
            maximum = num
    return maximum


print(find_max(1, 5, 3, 9, 2))   
print(find_max(-10, -3, -25))    
print(find_max(7))               
print(find_max())           


def multiply(*args):
    if not args:   
        return None
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(2, 3, 4))   
print(multiply(5))         
print(multiply())          
print(multiply(1, -2, 3))     

def count_even_odd(*args):
    even_count = 0
    odd_count = 0
    
    for num in args:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count


print(count_even_odd(1, 2, 3, 4, 5, 6))  
print(count_even_odd(2, 4, 6, 8))        
print(count_even_odd(1, 3, 5, 7))        
print(count_even_odd())                  



def concat_strings(*args):
    return " ".join(args)


print(concat_strings("Hello", "world"))          
print(concat_strings("Python", "is", "fun"))     
print(concat_strings())      


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


student_info(name="malli", age=20, grade="A")
print("---")
student_info(name="naga", grade="B")


def car_details(**kwargs):
    print("Car Details:")
    print("------------")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


car_details(brand="KTM", model="corolla", color="Red", price="$80,000")
print()
car_details(brand="HERO", model="Corolla", color="Blue")



def shopping_bill(**kwargs):
    total = sum(kwargs.values())
    return total


print("Total Bill:", shopping_bill(materials=2000, jeans=1000, drees=1500))   
print("Total Bill:", shopping_bill(shirts=200, sarees=2500))              
print("Total Bill:", shopping_bill())        


def order_pizza(size, *toppings, **details):
    print(f" Pizza Order")
    print(f"Size: {size}")
    
    if toppings:
        print("Toppings:")
        for t in toppings:
            print(f" - {t}")
    else:
        print("No extra toppings")
    
    if details:
        print("Details:")
        for key, value in details.items():
            print(f" - {key.capitalize()}: {value}")
    print(" Order Confirmed ")

order_pizza("Large", "Mushrooms", "Olives", crust="Thin", takeaway=True, extra_cheese=True)
print()
order_pizza("Medium")



def student_report(name, *marks, **details):
    print(" Student Report")
    print("-----------------")
    print(f"Name: {name}")
    
    
    if marks:
        print("Marks:", ", ".join(map(str, marks)))
        print(f"Total Marks: {sum(marks)}")
        print(f"Average Marks: {sum(marks)/len(marks):.2f}")
    else:
        print("No marks provided")
        student_report("Malleswari", 85, 90, 78, age=20, grade="A", subject="Math")
student_report("Malli", 70, 65, 80, subject="Science")
student_report("Naga", 65, 60, 85, subject="computers")



def student_report(name, *marks, **details):
    print(" Student Report")
    print("-----------------")
    print(f"Name: {name}")
    if details:
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    
    if marks:
        print("Marks:", ", ".join(map(str, marks)))
        total = sum(marks)
        avg = total / len(marks)
        print(f"Total Marks: {total}")
        print(f"Average Marks: {avg:.2f}")
    else:
        print("No marks provided")
    
    print("✅ Report Generated!\n")


student_report("Malli", 85, 90, 78, age=20, grade="A", subject="Math")
