def ticket_calculator(age, isStudent=False):
    if isStudent and age > 5:
        return 15.00
    elif age <=5:
        return 0.00
    elif age <= 18 or age >65:
        return 20.00
    else:
        return 30.00
    
# test case 1
#print(ticket_calculator(7, False))
    
# test case 2 
print(ticket_calculator(67, True))