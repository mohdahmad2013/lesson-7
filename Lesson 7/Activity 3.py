print("Enter the marks of 5 subjects")
sub1=int(input("Subject 1 :"))
sub2=int(input("Subject 2 :"))
sub3=int(input("Subject 3 :"))
sub4=int(input("Subject 4 :"))
sub5=int(input("Subject 5 :"))
total=sub1+sub2+sub3+sub4+sub5
average= total/5
if sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100:
    print("Your numbers should be 100 or lower")
elif average>=80 and average<=100:
    print("You got A")
elif average>=60 and average<=79:
    print("You got B")
elif average>=40 and average<=59:
    print("You got C")
elif average>=20 and average<=39:
   print("You got D")
else:
    print("YOU FAILED")