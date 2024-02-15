damagedealt = 0
minotaurhp = 15
demonhp = 10
zombiehp = 5
playerhp = 20
con = 0
import time
import random
damagelist = [1, 2, 3, 4, 5, 6]
damage = random.choice(damagelist)
print("Welcome to... TEXT ADVENTURE!")
time.sleep(1)
print("\nHere you can choose anything to help you battle through a mighty dungeon.")
time.sleep(1)
playerName = input("\nWhat do you want your name to be adventurer?\n ")
time.sleep(1)
if playerName == "henry":
  print("cheats activated")
  playerhp = 1000
time.sleep(1)
print("\nWelcome " + playerName + ".")
time.sleep(1)
while True:
  playerWeapon = input("\nWhat weapon do you want?\no----(::::::::::>" + "\n1) Short Sword" + "\n2) Long Sword" + "\n3) Great Sword\n")
  if playerWeapon == "1":
    playerWeapon = "Short Sword"
    break
  elif playerWeapon == "2":
    playerWeapon = "Long Sword"
    break
  elif playerWeapon == "3" or playerWeapon == "Great Sword":
    playerWeapon = "Great Sword"
    break
  else: print("Thats not a weapon silly")

time.sleep(1)
    
while True:
  story = input("Where do you want to go?" + "\n1) Dragons lair\n" + "2) Spiders den\n")
  if story == "1":
    place = "Dragons Lair"
    break
  elif story == "2":
    place = "Spiders Nest"
    break
  else: print("Thats not a place silly")
if place == "Spiders Nest":
  print("\nAs you approach the massive entrance to the Spiders nest you hear a barely audible whisper saying: Coming sooooon ooooooh\n")
  place == "Dragons Lair"
time.sleep(2)
print("Ok so your name is " + playerName + ". You want to wield a " + playerWeapon + " and explore the " + "Dragons Lair" + ".")
print("Time to start!")


time.sleep(2)

print("\nYou walk down a large set of damp stone stairs coming into a large room.")
time.sleep(2)
print("\nAgainst one wall you see a large book shelf with a old wooden chest stitting aginst it.")
time.sleep(2)
investigatebookshelf = input("\nDo you want to check the chest?" + "\nY/N\n")
if investigatebookshelf == "y" or investigatebookshelf == "Y":
    time.sleep(2)  
    print("\nOk you pull out a old dusty book with strange writing on it.")
time.sleep(2)
if investigatebookshelf == "n" or investigatebookshelf == "N":
  print("\nOk continuing..")
time.sleep(2)
print("\nYou contiune around the room and see two doors. the one on the right has a lion carved onto it. the one on the right has a metal bird handle.")
time.sleep(3)
Whichdoorfirst = input("\nwhich door do you want to enter?" + "\n1) Left" + "\n2) Right\n")
if Whichdoorfirst == "1":
  time.sleep(2)
  print("\nOk you head into the left door and are attacked by a zombie!")
  firstenemy = "Zombie"
  print("[¬º-°]¬")
if Whichdoorfirst == "2":
  time.sleep(2)
  print("\nOk you head into the right room and are attacked by a Demon")
  firstenemy = "Demon"
  print("(꒪ཀ꒪)")
time.sleep(2)
print("\nThe " + firstenemy + " looks like it wants to fight!")
time.sleep(2)
firstfightprompt = input("\nDo you want to fight the " + firstenemy + "?" + "\nY/N\n")
time.sleep(2)
if firstfightprompt == "n" or firstfightprompt == "N":
  print("Oh no you couldnt get away!")
  firstfightprompt = "y"
if firstfightprompt == "y" or firstfightprompt == "Y":
  time.sleep(2)
  print("Ok you chose to fight the " + firstenemy)
time.sleep(2)
damagelist = [1, 2, 3, 4, 5]
damage = random.choice(damagelist)
time.sleep(2)
if firstenemy == "Zombie":
  while zombiehp > 0 and playerhp > 0:
    if firstfightprompt == "y" or firstfightprompt == "Y":
      damagelist = [1, 2, 3, 4, 5]
      damage = random.choice(damagelist)
      
      print("You hit the " + firstenemy + " for " + str(damage) + " damage\n")
      zombiehp = zombiehp - damage
      damagedealt = damagedealt + damage
      playerdamage = random.choice(damagelist)
      time.sleep(1)
      print("Oh no the enemy " + firstenemy + " hit you for " + str(playerdamage) + " damage!\n")
      playerhp = playerhp - playerdamage
      if zombiehp <= 0:
        time.sleep(1) 
        print("you killed the zombie!\n")
        con = 1
        getinfected = (1, 5)
        didugetinfected = random.choice(getinfected)
        if didugetinfected > 2:
          time.sleep(2)
          print("you got infected by the zombie!")
          playerhp - 5
          time.sleep(2)
          print("\n-5 health")
        if playerhp <= 0:
          print("you died!")
      
          
      
     
if firstenemy == "Demon":
  while demonhp > 0 and playerhp > 0:
    if firstfightprompt == "y" or firstfightprompt == "Y":
      damagelist = [1, 2, 3, 4, 5]
      damage = random.choice(damagelist)
      time.sleep(1)
      print("You hit the " + firstenemy + " for " + str(damage) + " damage\n")
      demonhp = demonhp - damage
      damagedealt = damagedealt + damage
      playerdamage = random.choice(damagelist)
      time.sleep(1)
      print("Oh no the enemy " + firstenemy + " hit you for " + str(playerdamage) + " damage!\n")
      playerhp = playerhp - playerdamage
      time.sleep(1)
      if demonhp <= 0:
        print("you killed the demon!\n")
        con = 1
      if playerhp <= 0:
        print("You Died!")
        quit()
if con == 1:
  time.sleep(2)
  healthlist = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
  health = random.choice(healthlist)
  coinlist = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  coins = random.choice(coinlist)
  time.sleep(2)
  checkbehindfirst = input("\nDo you want to check behind the " + firstenemy + "?" + "\nY/N\n")
  if checkbehindfirst == "Y" or checkbehindfirst == "y":
    time.sleep(2)
    print("\nBehind the " + firstenemy + " you find " + "a health potion" + " it healed " + str(health) + " health points!" " you also found " + str(coins) + " gold coins in a bag!")
    playerhp = playerhp + health
  time.sleep(2)
  print("\nYou walk out of the room back into the hallway and see a large stone button has appeared.")
  if checkbehindfirst == "N" or checkbehindfirst == "n":
    time.sleep(2)
    print("\nOk continuing")
  
  time.sleep(2)
 
  firstbuttonpress = input("\nDo you want to press the button? \n1) Y \n2) N\n")
  
time.sleep(2)
if firstbuttonpress == "n" or firstbuttonpress == "Y" or firstbuttonpress == "2":
  print("\nYou see a wood chest but as you walk up to it you are completely swollowed by it.")
  time.sleep(2)
  print("\nGame Over")
  quit()

if firstbuttonpress == "y" or firstbuttonpress == "Y" or firstbuttonpress == "1":
     time.sleep(2)
     print("\nYou hear a loud scraping sound coming from the wall across from you.")
     time.sleep(2)
     print("\nAcross from you two large doorways in the wall appear!")
     time.sleep(2)
whichdoorway = input("\nwhich door do you want to enter? \n1) Left \n2) Right\n")
if whichdoorway == "2" or whichdoorway == "Right" or whichdoorway == "right":
  time.sleep(2)
  print("You head into the right door but as you walk down the long but after making it only about halfway though you hear a scraping sound and the ground beneath you opens up and you fall into a massive pit of spikes")
  time.sleep(2)
  print("Game Over")
  time.sleep(2)
  quit()
if whichdoorway == "1" or whichdoorway == "Left" or whichdoorway == "left":
  print("As you turn the corner a Giant Orc lunges at you!")
  secondenemy = "Giant Orc"
time.sleep(2)
print("\nThe " + secondenemy + " looks like it wants to fight!")
time.sleep(2)
secondfightprompt = input("\nDo you want to fight the " + secondenemy + "?" + "\nY/N\n")
time.sleep(2)
if secondfightprompt == "n" or secondfightprompt == "N":
  print("Oh no you couldnt get away!")
  firstfightprompt = "y"
if secondfightprompt == "y" or secondfightprompt == "Y":
  time.sleep(2)
  print("Ok you chose to fight the " + secondenemy)
time.sleep(2)
damagelist = [1, 2, 3, 4, 5]
damage = random.choice(damagelist)
time.sleep(2)
spiderhp = 15
while spiderhp > 0 and playerhp > 0:
    if secondfightprompt == "y" or secondfightprompt == "Y":
      damagelist = [1, 2, 3, 4, 5]
      damage = random.choice(damagelist)
      time.sleep(1)
      print("You hit the " + secondenemy + " for " + str(damage) + " damage\n")
      spiderhp = spiderhp - damage
      damagedealt = damagedealt + damage
      playerdamage = random.choice(damagelist)
      time.sleep(1)
      print("Oh no the enemy " + secondenemy + " hit you for " + str(playerdamage) + " damage!\n")
      playerhp = playerhp - playerdamage
      time.sleep(1)
      if spiderhp <= 0:
        print("you killed the Giant Orc!\n")
        con = 1
      if playerhp <= 0:
        print("You Died!")
        quit()
if con == 1:
  time.sleep(2)
  healthlist = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
  health = random.choice(healthlist)
  coinlist = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  coins = random.choice(coinlist)
  time.sleep(2)
  checkbehindsecond = input("\nDo you want to check behind the " + secondenemy + "?" + "\nY/N\n")
  if checkbehindsecond == "Y" or checkbehindsecond == "y":
    time.sleep(2)
    print("\nBehind the " + secondenemy + " you find " + "a health potion" + " it healed " + str(health) + " health points!" " you also found " + str(coins) + " gold coins in a bag!")
    playerhp = playerhp + health
  time.sleep(2)
  print("As you look behind the orc you see a large stone archway has appeared and as you head through you see the blinding light of freedom!")
  time.sleep(2)
  print("You win!!!")
  quit()
  if checkbehindsecond == "N" or checkbehindsecond == "n":
    time.sleep(2)
    print("As you turn to head back to the main room a large stone archway appears next to you and as you head through you see the blinding light of freedom!")
    time.sleep(2)
  print("You win!!!")
  quit()
  
