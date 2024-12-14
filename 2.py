project = int(input("enter the project score"))
internal = int(input("enter the internal score"))
external = int(input("enter the external score"))
if project >= 50 and internal >= 50 and external >= 50:
        p = (70 / 100)*project
        i = (10/100)*internal
        e = (20/100)*external
        total = p+i+e
        print(total)
        if total > 90:
            print("grade A")
        elif total > 80:
            print("grade B")
        else:
            print("grade c")
elif internal < 50 and external < 50:
    print("you failed in both")
elif internal < 50:
    print("you failed in internal")
elif external < 50:
    print("you failed in external")

else:
    print("you failed in project")