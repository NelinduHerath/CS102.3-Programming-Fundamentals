attempts_left:int=3
correct_password: str="admin"

while attempts_left >=1:
    input_password: str=input("Enter password")
    if input_password==correct_password:
        print("Access Grantted.")
    else:
        print("Incorrect password")
        attempts_left-=1
        if attempts_left==0:
            print("no more attempts left!")
            break
        else:
            print(f"only{attempts_left} attempts left")
