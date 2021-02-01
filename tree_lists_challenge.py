# Lists Challenge
# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_players = input("Would you like to add a player to the list? yes/no  ")
while add_players.lower() == 'yes':
    name = input("\nWhat is the player's name?  ")
    players.append(name)
    add_players = input("Would you like to add another player to the list? yes/no  ")

# TODO print the number of players on the team
print("There are {} players on your team.".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in players:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

# TODO Select a goalkeeper from the above roster
keeper = input("Which player should be the goalkeeper? Please type their number, 1-{} ".format(len(players)))
keeper = int(keeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great, {} will be the goalkeeper for your team.".format(players[keeper -1]))
