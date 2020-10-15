def GetInput():
	return input("\nRock, paper, or scissors? \n").strip().lower()

def Rock():
	print("""\n
     _______
 ---'   ____)
|      (_____)
|      (_____)
|      (____)
 ---.__(___)
		\n""")
	return "rock"


def Paper():
	print("""\n
      _______
 ---'    ____)____
|           ______)
|          _______)
|         _______)
 ---.__________)
		""")
	return "paper"

def Scissors():
	print("""\n
     _______
 ---'   ____)____
|          ______)
|          ______)
|      (____)
---.__(___)
		\n""")
	return "scissors"

input(""" Welcome To Reda's Totally Beatable Rock, Paper, Scissors (press enter to start)
     _______         _______              _______
 ---'   ____)    ---'    ____)____    ---'   ____)____
|      (_____)  |           ______)  |          ______)
|      (_____)  |          _______)  |          ______)
|      (____)   |         _______)   |      (____)
 ---.__(___)     ---.__________)      ---.__(___)
""")

while True:
	successful = False
	while not successful:
		playerInput = GetInput()

		computerInput = None
		successful = True
		if playerInput == "rock":
			Rock()
			computerInput = Paper()
		elif playerInput == "paper":
			Paper()
			computerInput = Scissors()
		elif playerInput == "scissors":
			Scissors()
			computerInput = Rock()
		else:
			successful = False
			continue

		print("Computer chose " + computerInput + ". You lose!")
