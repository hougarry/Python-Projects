print("welcome to my computer quiz!")

playing = input("Do you want to play?")

text = "Tim Is Great!"

print(text.lower())
if playing.lower() !="yes":
    quit()


print("okay, let's play:")
score = 0

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    score = score + 1
else:
    print('Incorrect!')

print('You got' + str(score) + 'questions correct')
print('You got' + str((score/4)* 100) + "%")

answer = input("what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
else:
    print('Incorrect!')

answer = input('what does RAM stand for?')
if answer.lower() == 'random access memory':
    print('Correct!')
else:
    print('Incorrect!')

answer = input('what does PSU stand for')
if answer.lower() == 'power supply unit':
    print('Correct!')
else:
    print('Incorrect!')


          
