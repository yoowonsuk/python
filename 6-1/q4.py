def main():
    st = []
    for i in range(1, 11):
        st.append(i)
        print(st)
    for i in range(1, 11):
        st.remove(i) # st.pop(0) also works
        print(st)

main()
