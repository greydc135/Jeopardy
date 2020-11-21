# This is the User class
# It will be able to hold a list of questions that can expand as needed.
# It can also hold player name and number of points.
class User:
    email = ""
    #nickname?
    #points = 0
    questions = []
    
    def addQuestion(self):
        newQuestion = input('Enter a question: ')
        newAnswer = input('Enter the answer to that question: ')
        self.questions.append( Question(newQuestion, newAnswer) )

#class Admin(User):
    # is a User, will hold more information like game customization

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    #points = None

# main function to be the skeleton of what we need to do for interacting with the database
# as well as be a general flow of what each user will go through
def main():
    # simulate clicking "Join Game"
    # input email to "log in" and create a User
    newUser = User()
    newUser.email = input('Input email to log in: ')
    print()

    # here would be where they could input a nickname

    # now is when they are asked what game to join, inputting the email of the Admin they wish to join
    joinGame = input('Please input the email of the person whose game you want to join: ')
    print("Joining game...")
    print()
    # then, check and see if it is an available server and have 3 responses:
    # Joining game...
    # Sorry, that game is full!
    # Sorry, we couldn't find a game under that email!

    # next, depending on server specifications, prompt the user for the questions and their answers
    # we'll pretend, for now, that there are 3 questions needed for this game
    x = 0
    while (x < 3):
        newUser.addQuestion()
        x += 1

main()