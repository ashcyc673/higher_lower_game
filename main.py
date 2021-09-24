from game_data import data
import random
import art


for_loop_country = [country["country"] for country in data]
for_loop_name = [name["name"] for name in data]
for_loop_follower = [follower["follower_count"] for follower in data]
for_loop_desc = [desc["description"] for desc in data]

print(art.logo)

is_continue = True
score = 0

while is_continue:
  random_pick = random.randint(1,len(data) - 1)
  random_pick2 = random.randint(1,len(data) - 1)
  whole_value = data[random_pick]
  whole_value2 = data[random_pick2]

  if random_pick == random_pick2:
    random_pick = random.randint(1,len(data) - 1)
  
  # print(whole_value)
  print("")
  print(f"Compare A: {for_loop_name[random_pick]}, a {for_loop_desc[random_pick]}, from {for_loop_country[random_pick]}")

  print(art.vs)

  # print(whole_value2)
  print("")
  print(f"Against B: {for_loop_name[random_pick2]}, a {for_loop_desc[random_pick2]}, from {for_loop_country[random_pick2]}")
  print("")

  choice_a = for_loop_follower[random_pick]
  choice_b = for_loop_follower[random_pick2]
  compare = input("Who has more follower? Type 'A' or 'B': ")
  print("")

  if compare == "A" or compare == "a":
    compare = for_loop_follower[random_pick]
  else:
    compare = for_loop_follower[random_pick2]

  if choice_a > choice_b:
    highest = choice_a
    lower = choice_b
  else:
    highest = choice_b
    lower = choice_b
  
  if compare == highest:
    score += 1
    print("")
    print(f"*****Hooray! Correct*****")
    print(f"     Current Score: {score}")
    print("")
  else:
    print(f"You guess wrong :'(, final score: {score}")
    print("")
    is_continue = False

    
