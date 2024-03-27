#1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["Beverages"] = {"Soda":4.99, "juice":7.99}
print(restaurant_menu)
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)
del restaurant_menu ["Starters"] ["Bruschetta"]
print(restaurant_menu)

#2 Task1
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def room_booking(key,name):
        if key in hotel_rooms:
            if hotel_rooms[key]["status"] == "available":
                hotel_rooms[key]["status"] == "booked"
                hotel_rooms[key]["customer"] == name
                print(f"Room {key} reserved by {name}")
            else:
                print(f"Room {key} is already booked")
        else:
           print("invalid input ")


def checking_out(key):
    if key in hotel_rooms:
            if hotel_rooms[key]["status"] == "booked":
               name = hotel_rooms[key]["customer"]
               hotel_rooms[key]["status"] = "available"
               hotel_rooms[key]["customer"] = ""
               print(f"{name} has checked out of room {key}")
            else:
               print(f"the room {key} is not booked")
    else:
         print(f"Room is not valid")

def display_status():
        print("Room Status:")
        for room_number, room_info in hotel_rooms.items():
            print(f"Room {room_number}: {room_info['status']} by {room_info['customer']}")

display_status()
room_booking("101" , "Sarah")
room_booking("102" , "john")
checking_out("101")
display_status()

#task2
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def search_product(product):
    matching_products = []
    for product_type, product_info in products.items():
        if product in product_info["name"]:
            matching_products.append((product_type, product_info))
    return matching_products
search_name = "Shirt"
matching = search_product(search_name)
if matching:
     print(f"Matching products for {search_name}")
     for product_type, product_info in matching:
          print(f"Product ID: {product_type}, Name: {product_info['name']}, Category: {product_info['category']}, Price: ${product_info['price']}")
else:
     print(f"No matching results")

#3 
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_ticket(ticket_num, customer_name, problem):
    if ticket_num not in service_tickets:
        service_tickets[ticket_num] = {"Customer": customer_name, "Issue": problem, "Status": "open"}
        print(f"{ticket_num} is opened for {customer_name}: {problem}")
    else:
        print("Ticket is already in the system")

def update_status(ticket_num, new_status):
    if ticket_num in service_tickets:
        service_tickets[ticket_num]["Status"] = new_status
        print(f"{ticket_num} updated to {new_status}")
    else:
        print("Ticket does not exist")

def display_tickets(status=None):
    if status:
        print(f"Tickets with status '{status}':")
        for ticket_type, ticket_info in service_tickets.items():
            if ticket_info["Status"] == status:
                print(f"{ticket_type}, {ticket_info['Customer']},{ticket_info['Issue']},{ticket_info['Status']}")
    else:
        print("All tickets:")
        for ticket_type, ticket_info in service_tickets.items():
            print(f"{ticket_type}, {ticket_info['Customer']}, {ticket_info['Issue']}, {ticket_info['Status']}")
open_new_ticket("Ticket003", "Raymond", "Coding error")
update_status("Ticket001", "closed")
display_tickets()