melon_cost = 1.00
def customer_payment():
    ''' creating a function to calculate the customers payments from a file '''
    file = open("customer-orders.txt")
    for line in file:
        line.rstrip()
        word = line.split('|')

        cust_num = int(word[0])
        cust_name = str(word[1])
        cust_melon = int(word[2])
        cust_paid = float(word[3])

        cust_expected = cust_melon * melon_cost
        if cust_expected != cust_paid:
            print(f"{cust_name} paid ${cust_paid:.2f},",
              f"expected ${cust_expected:.2f}"

              )
    file.close()
customer_payment()
