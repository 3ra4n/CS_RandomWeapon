
def Money(player):
    if player.team == "Terrorist":
        return 800
    elif player.team == "Counter-Terrorist":
        return 800
    else:
        return 0
    
Player = type("Player", (object,), {})  # Simple Player class for demonstration

def Player(name, team):
    player = Player()
    player.name = name
    player.team = team
    player.money = Money(player)
    return player