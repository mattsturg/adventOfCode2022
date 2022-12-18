# Some of my worst code. However, it works!

class Player:
    choice = ""

    def __init__(self, ind, let):
        if ind == 0:
            if let == 'A':
                self.choice = "Rock"
            elif let == 'B':
                self.choice = "Paper"
            else:
                self.choice = "Scissors"
        else:
            if let == 'X':
                self.choice = "Rock"
            elif let == 'Y':
                self.choice = "Paper"
            else:
                self.choice = "Scissors"

    def get_score(self, other_player):
        score = 0
        if self.choice == "Rock":
            if other_player.choice == "Rock":
                score += 3
            elif other_player.choice == "Scissors":
                score += 6
            score += 1
        elif self.choice == "Paper":
            if other_player.choice == "Paper":
                score += 3
            elif other_player.choice == "Rock":
                score += 6
            score += 2
        else:
            if other_player.choice == "Scissors":
                score += 3
            elif other_player.choice == "Paper":
                score += 6
            score += 3
        return score


class PlayerWl:
    choice = ""

    def __init__(self, ind, let):
        if ind == 0:
            if let == 'A':
                self.choice = "Rock"
            elif let == 'B':
                self.choice = "Paper"
            else:
                self.choice = "Scissors"
        else:
            if let == 'X':
                self.choice = "Rock"
            elif let == 'Y':
                self.choice = "Paper"
            else:
                self.choice = "Scissors"

    def get_other_score(self, outcome):
        score = 0
        if outcome == 'X':
            if self.choice == "Rock":
                score += 3
            elif self.choice == "Paper":
                score += 1
            else:
                score += 2
        elif outcome == 'Y':
            score += 3
            if self.choice == "Rock":
                score += 1
            elif self.choice == "Paper":
                score += 2
            else:
                score += 3
        else:
            score += 6
            if self.choice == "Rock":
                score += 2
            elif self.choice == "Paper":
                score += 3
            else:
                score += 1
        return score


def make_players(play_list):
    total_score = 0
    for game in play_list:
        game = game.split()
        them = Player(0, game[0])
        us = Player(1, game[1])
        total_score += us.get_score(them)
    return total_score


def make_players_wl(play_list):
    total_score = 0
    for game in play_list:
        game = game.split()
        them = PlayerWl(0, game[0])
        total_score += them.get_other_score(game[1])
    return total_score
