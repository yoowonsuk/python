def to_list(t):
    st = []
    for i in t:
        st.append(i)
    return st

def main():
    ds = (1, 2, 3)
    ds = to_list(ds)
    print(ds)

    ds = "hello"
    ds = to_list(ds)
    print(ds)

main()
