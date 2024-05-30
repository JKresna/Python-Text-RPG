# Class untuk membuat object player

class Player:

    def __init__(player):
        player.name = ""
        player.hp = 0
        player.mp = 0
        player.__job = ""
        player.status_effects = []
        player.location = "start"
        player.game_over = False

    # Getter & Setter untuk Job player
    @property
    def job(self):
        None

    @job.getter
    def job(player):
        return player.__job

    @job.setter
    def job(player, job):
        
        match job.lower():
            case "warrior":
                player.hp = 180
                player.mp = 70
            case "assasin":
                player.hp = 140
                player.mp = 150
            case "archer":
                player.hp = 150
                player.mp = 130
            case "mage":
                player.hp = 120
                player.mp = 180
            case _:
                raise Exception("Please choose between Warrior, Mage, Archer, or Assasin.")

        player.__job = job.lower()
