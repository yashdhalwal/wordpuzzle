# JSON is a syntax for storing and exchanging data.
# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Python Random module is an in-built module of Python which is used to generate random numbers. 
import random
# No echo input ( passwords aren't shown )
import getpass

def play():
	print("\n==========QUIZ START==========")
	score = 0
	with open("assets/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(10):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')
  
def quizQuestions():
    print('\n==========ADD QUESTIONS==========\n')
    ques = input("Enter the question that you want to add:\n")
    opt = []
    print("Enter the 4 options with character initials (A, B, C, D)")
    for _ in range(4):
        opt.append(input())
        ans = input("Enter the answer:\n")
    with open("assets/questions.json", 'r+') as f:
        questions = json.load(f)
        dic = {"question": ques, "options": opt, "answer": ans}
        questions.append(dic)
        f.seek(0)
        json.dump(questions, f)
        f.truncate()
        print("Question successfully added.")
        

     
choice = 1
while choice != 4:
		print('\n=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. EXIT')
		
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
