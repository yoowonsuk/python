def birth_only(st):
    return st[:6]
    
    # ret = st.split('-')
    # return ret[0]

def main():
    p1 = "070609-2011xxx"
    p1 = birth_only(p1)
    print(p1)

    p2 = "090716-1012xxx"
    print(birth_only(p2))

main()
