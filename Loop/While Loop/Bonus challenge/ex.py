import random
guess = random.randint(1,20)
attemp = 1
while True:
  
  n = int(input("Enter the number: "))
  
  
  if n > guess:
    print("too high")

  elif n < guess:
    print("too low")
  else:
    print("You won")
    print(f"You won in {attemp} attemps")
    break
  attemp +=1
  
