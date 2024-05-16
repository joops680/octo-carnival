# asking user there age
age = int(input("What is your age? "))
if age < 18:
    # checking if your older enough or a minor
    print("You are a minor.")
else:
    print("You just became an adult.")