def to_list(tup):
    st = []
    for i in range(len(tup)):
        st.append(tup[i])

    return st

def main():
    ds = (1, 2, 3)
    ds = to_list(ds)
    print(ds)

    ds = "hello"
    ds = to_list(ds)
    print(ds)

main()
