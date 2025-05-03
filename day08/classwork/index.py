cannons = int(input('Please enter the amount of cannons on your ship: '))
amount_of_people = int(input('Enter the amount of people on your ship: '))
ship_damage = int(input('Enter the current damage level of the ship (0-100): '))

# Check if cannons >= 10
can_go_to_battle_cannons = cannons >= 10

# Check if amount_of_people >= 20
can_go_to_battle_people = amount_of_people >= 20

# Check if ship damage is less than 50
can_go_to_battle_damage = ship_damage < 10
# Calculate if the ship can go into battle based on all conditions
can_go_to_battle = (can_go_to_battle_cannons and can_go_to_battle_people and can_go_to_battle_damage)

# Output the result using True/False
print('You can go into battle.' * can_go_to_battle)
print('You cannot go into battle.' * (not can_go_to_battle))