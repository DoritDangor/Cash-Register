import array
import sys
import product as p
import customer as c


TAX = 1.2
c_list = []
p_list = []


# initialize the system with data
def init_sys():
    init = 1
    while init != 9:
        init = int(input("-------\nTo enter customer details, press 1\nTo enter product details, press 2\n"
                         "For the customers list, press 3\nFor the products list, press 4\nTo continue, press 9\n"
                         "To exit, press 0:\n"))
        if init == 1:
            c_name = input("Enter a Customer Name: ")
            c_id = int(input("Enter a Customer Id: "))
            c_balance = int(input("Enter a Customer Balance: "))
            c_gender = int(input("Enter a Customer Gender: 0 for male, 1 for female: "))
            c_list.append(c.Customer(c_name, c_id, c_balance, c.Gender(c_gender)))
        if init == 2:
            p_company = input("Enter a Product Company: ")
            p_name = input("Enter a Product Name: ")
            p_bar_code = int(input("Enter a Product Barcode: "))
            p_price = int(input("Enter a Product Price: "))
            p_type = int(input("Enter a Product Type: 0 for regular, 1 for israeli: "))
            p_list.append(p.Product(p_company, p_name, p_bar_code, p_price, p.Type(p_type)))
        if init == 3:
            print("-------\n{:<10} {:<10} {:<10} {:<10}".format('Id', 'Name', 'Gender', 'Balance'))
            for item in c_list:
                print("{:<10} {:<10} {:<10} {:<10}".format(item.id, item.name, item.gender.name, item.balance))
        if init == 4:
            print("-------\n{:<10} {:<10} {:<10} {:<10} {:<10}".format('Name', 'Company', 'Barcode', 'Price', 'Type'))
            for item in p_list:
                print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(item.name, item.company, item.bar_code, item.price,
                                                                  item.type.name))
        if init == 0:  # exit
            sys.exit()


# starting a new bill
def new_b():
    new_bill = 1
    while new_bill != 0:
        new_bill = int(input("\nFor a new bill press:\n1 - Normal\n2 - Tax\n3 - Worker\n"
                             "To update system data, press 9\nTo Exit, press 0\n"))
        if new_bill == 0:  # exit
            sys.exit()
        if new_bill == 9:
            init_sys()
        cus_id = int(input("Enter a Customer Id: "))
        total_bill = 0
        bar_code = 1
        pro_arr = array.array('i')
        credit = 0
        min = float('inf')

        # Calculation of products
        while bar_code != 0:
            bar_code = int(input("\nTo finish the bill, press 0\nTo cancel the bill, press 9\n"
                                 "To continue enter a barcode:\n"))
            if bar_code == 9:
                print("The bill has been cancelled!")
                break
            for product in p_list:
                if bar_code == product.bar_code:
                    if new_bill == 1 or new_bill == 3:  # normal or worker bill
                        total_bill += product.price
                    if new_bill == 2:  # bill with tax
                        total_bill += product.price * TAX
                    pro_arr.append(bar_code)  # adding to current products list
                    if product.type.value == 0:  # regular product
                        credit += product.price * 0.1
                    if product.type.value == 1:  # israeli product
                        credit += product.price * 0.2
            print("-------\nYour Bill: ")
            print("{:<10} {:<10} {:<10}".format('Barcode', 'Name', 'Price'))
            for i in range(len(pro_arr)):
                for product in p_list:
                    if pro_arr[i] == product.bar_code:
                        print("{:<10} {:<10} {:<10}".format(product.bar_code, product.name, product.price))
                        if product.price < min:
                            min = product.price
            print("-------\nTotal: ", round(total_bill, 2), "\nCredit: ", credit)

        if new_bill == 3:  # worker bill
            total_bill = total_bill - min
            print("-------\nTotal after worker discount: ", round(total_bill, 2), "\nCredit: ", credit)

        # Calculation of total bill and updating customer balance
        for customer in c_list:
            if cus_id == customer.id:
                if customer.balance > 100 and total_bill * 10 <= customer.balance:
                    customer.balance = customer.balance - total_bill * 10 + credit
                    print("-------\nCurrent Customer:\nName: ", customer.name,
                          "\t\tBalance: ", round(customer.balance, 2), "\n")
                else:
                    print("****\nThere is not enough money for the customer. The bill has been cancelled!\n****")
        init_sys()


init_sys()
new_b()
