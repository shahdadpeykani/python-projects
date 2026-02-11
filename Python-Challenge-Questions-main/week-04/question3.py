
ticket_type = input("Please enter the ticket type: ").lower()

total = 0

if ticket_type == "front" or ticket_type == "middle" or ticket_type == "back":

    numb = int(input(f"How many {ticket_type} row tickets do you want?"))

    if ticket_type == "front":
        total = numb * 600
    elif ticket_type == "middle":
        total = numb * 400
    elif ticket_type == "back":
        total = numb * 150

    print(f"Total cost is {total} TL.")

else:
    print("Invalid ticket type!")
