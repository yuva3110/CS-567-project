class Pharmacy:
    def __init__(self):
        self.inventory = {}
        self.sales = {}
        self.customers = {}
        self.expiration_dates = {}
        self.discounts = {}
        self.batch_numbers = {}

    def add_item(self, item_name, quantity, price, expiration_date=None, discount=None, batch_number=None):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

        self.sales[item_name] = 0

        if expiration_date:
            self.expiration_dates[item_name] = expiration_date

        if discount:
            self.discounts[item_name] = discount

        if batch_number:
            self.batch_numbers[item_name] = batch_number

    def sell_item(self, item_name, quantity, customer=None):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                self.sales[item_name] += quantity
                if customer:
                    if customer in self.customers:
                        if item_name in self.customers[customer]:
                            self.customers[customer][item_name] += quantity
                        else:
                            self.customers[customer][item_name] = quantity
                    else:
                        self.customers[customer] = {item_name: quantity}
                return True
            else:
                return False
        else:
            return False

    def add_customer(self, customer_name, contact_details):
        self.customers[customer_name] = contact_details

    def add_discount(self, item_name, discount):
        self.discounts[item_name] = discount

    def add_batch_number(self, item_name, batch_number):
        self.batch_numbers[item_name] = batch_number

    def get_inventory(self):
        return self.inventory

    def get_sales(self):
        return self.sales

    def get_customers(self):
        return self.customers

    def get_expiration_dates(self):
        return self.expiration_dates

    def get_discounts(self):
        return self.discounts

    def get_batch_numbers(self):
        return self.batch_numbers
