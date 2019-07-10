class Friend:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.num

    def set_phone(self, num):
        self.num = num

    def show_info(self):
        print("name: " + self.name, end = ' ')
        print("number: " + self.num)

def main():
    f1 = Friend('yoon', '010-111-222')
    f2 = Friend('lee', '010-333-444')
    f3 = Friend('jang', '010-555-666')
    f4 = Friend('yoon', '010-777-888')

    lst = [f1, f2, f3, f4]
    for i in lst:
        print(i.get_name(), i.get_phone())
main()

