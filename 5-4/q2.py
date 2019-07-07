def show_reverse(st):
    for i in range(len(st)):
        print(st[len(st)-1-i], end = ' ')

show_reverse([1, 2, 3, 4, 5])
show_reverse("ABCDEFG")
