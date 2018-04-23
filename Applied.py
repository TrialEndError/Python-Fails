#Applied#
import random
print("\nWelcome to number guessing game...\n")
asd=random.randint(0,50)
ass=random.randint(0,100)
#You should'nt be looking in here...#
add=random.randint(0,500)
exe=["easy","medium","hard"]
print("These are the possible difficulties you can choose from:\n",exe,"\n")
aaa=input("Select Difficulty!\nType it in!\n ")
if aaa in exe[0]:
   print("Okay!")
   while True:
      ent=int(input("Enter your guess!\nNumber:"))
      if ent<asd:
         print("Sorry bud your guess was too small.\nTry again...\n")
      elif ent>asd:
         print("Try a little lower bro...\n")

      else:
         print("nice guess bro...\nIt was correct!")
         break
      

if aaa in exe[1]:
   print("Okay!")
   while True:
      ent=int(input("Enter your guess!\nNumber:"))
      if ent<ass:
         print("Sorry bud your guess was too small.\nTry again...\n")
      elif ent>ass:
         print("Try a little lower bro...\n")

      else:
         print("nice guess bro...\nIt was correct!")
         break
      

if aaa in exe[2]:
   print("Oh Wow, I also enjoy living life on the harderside.\n(*-*)\n")
   while True:
      ent=int(input("Enter your guess!\nNumber:"))
      if ent<add:
         print("Sorry bud your guess was too small.\nTry again...\n")
      elif ent>add:
         print("Try a little lower bro...\n")

      else:
         print("nice guess bro...\nIt was correct!")
         break

      
