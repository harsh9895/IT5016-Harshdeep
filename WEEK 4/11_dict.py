def main():
    contacts = {"Jill": 3456, "James": 7654, "Syed": 6754}
    contacts["Mark"] = 7654
    contacts["Jerry"] = 7004
    
    contacts["James"] = 3456
    name1 = "Jill"
    name2 = "James"
    print(name1, "is at extension:", contacts[name1])
    if contacts[name1] == contacts[name2]:
        print(name2, "has same extension")
    print(contacts)

main()