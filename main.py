import csv 

header = ['name' , 'rating']

def add_element(categorie,name,rating):
    data = [name, rating]
    with open(categorie+'.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

choice = int(input("what's new today\n\tanime : type 1\n\tfilms : type 2\n\tseries : type : 3"))
if choice == 1:
    name = input("enter the name : ")
    rating = float(input("enter your rating : "))
    add_element("anime",name,rating)
