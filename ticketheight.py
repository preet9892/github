minimum_height = 160
height = int(input("how tall are you"))
age = int(input("what is your age"))

if minimum_height > height:
    print("not tall enough")
else:
    if age ==20 or age >20:
        print("Ticket id $50")
    elif age<21:
        print("Ticket is $60")
    elif age < 22:
        print ("Ticket is $70")

photo = input("Do you want a photo? yes or no")
if photo =="yes":
    print("That will be another$100")
else:
    print("proceed")