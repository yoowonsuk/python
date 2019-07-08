def main():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    print(st)

    st.pop(-1)
    st.pop(-1)
    st.pop(-1) # inserting, we should allow for the index changed
    print(st)

main()

