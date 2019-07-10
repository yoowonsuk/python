class Friend:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def get_name(self):
        return name

    def get_phone(self):
        return num

    def set_phone(self, num):
        self.num = num

    def show_info(self):
        print("name: " + self.name, end = ' ')
        print("number: " + self.num)
