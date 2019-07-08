def main():
    st = input("input integer: ")

    if st.isdigit():
        print(int(st) ** 2)
    else:
        print("It's not integer")

main()

