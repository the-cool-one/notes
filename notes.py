Amount=int(input("Please Enter Amount to Withdraw"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("The amount of 100 rupee notes is",note_1)
print("The amount of 50 rupee notes is",note_1)
print("The amount of 10 rupee notes is",note_3)