def main():
    num = int(input("Input Integer: "))

    if num < 0:
        print("it's smaller than 0")
    elif 0 <= num < 10:
        print("it's between 0 and 10, including 0")
    elif 10 <= num < 20:        
        print("it's between 10 and 20, including 10")
    else:
        print("bigger than 20")

main()
            
