class Participant:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__choice = ""

    def choose(self):
        self.__choice = input(
            "{name}, select rock, paper, scissor, lizard or Spock: ".format(
                name=self.__name
            )
        )
        print("{name} selects {choice}".format(name=self.__name, choice=self.__choice))

    def toNumericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, "lizard": 3, "spock": 4}
        return switcher[self.__choice]

    def incrementPoint(self):
        self.__points += 1

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def get_choice(self):
        return self.__choice


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(
            "Round resulted in a {result}".format(result=self.getResultAsString(result))
        )

        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]

    def awardPoints(self):
        print("implement")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        GameRound(self.participant, self.secondParticipant)
        self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n:")
        if answer == "y":
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                "Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(
                    p1name=self.participant.get_name(),
                    p1points=self.participant.get_points(),
                    p2name=self.secondParticipant.get_name(),
                    p2points=self.secondParticipant.get_points(),
                )
            )
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.get_points() > self.secondParticipant.get_points():
            resultString = "Winner is {name}".format(name=self.participant.get_name())
        elif self.participant.get_points() < self.secondParticipant.get_points():
            resultString = "Winner is {name}".format(
                name=self.secondParticipant.get_name()
            )
        print(resultString)


game = Game()
game.start()
