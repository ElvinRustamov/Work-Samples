class GuessTheNumber():
  import random

  def __init__(self):
    self.predicted_comp = self.random.randrange(1, 100)
    self.user_guess_numbers = []
    self.user_guess_not_numbers = []
    self.guess_counter = 0
    self.guess_chance = 0.
    print('Welcome! Guess a number between 1 and 100.')
    self.choose_a_level()
    self.find_number()

  def choose_a_level(self):
    level = input('Choose a level (Easy, Normal, Hard): ').lower()
    if level in ['easy', 'normal', 'hard', 'e', 'n', 'h']:
      
      if level == 'easy' or level == 'e':
        self.guess_chance = 7
      elif level == 'normal' or level == 'n':
        self.guess_chance = 5
      elif level == 'hard' or level == 'h':
        self.guess_chance = 3
    
    else:
      print('Choose correct level. Levels are: Easy (E), Normal (N), Hard (H)')
      self.choose_a_level()
      
    print(f'You have {self.guess_chance} guess chance. Have a good play.')


  def find_number(self):
    while self.guess_chance:
      user_input = input("Guess a number (For exit the game press 'q'): ")
      if user_input == 'q':
        break
      else:
        try:
          user_number = int(user_input)
          self.user_guess_numbers.append(user_number)
        except ValueError:
          self.user_guess_not_numbers.append(user_number)
          print('Write a Number.')
          self.find_number()

        if user_number == self.predicted_comp:
          print(f'''You winnnnnnnnnnn the game!!!!. 
          You find the right number on the {self.guess_counter} guess. 
          Your guessed numbers are: {self.user_guess_numbers}''')
          break

        elif user_number > self.predicted_comp:
          self.guess_chance -= 1
          self.guess_counter += 1
          print(f'''Say Low ⤓⤓⤓. Your remain guess {self.guess_chance}. 
          Your guessed numbers are: {self.user_guess_numbers}''')

        elif user_number < self.predicted_comp:
          self.guess_chance -= 1
          self.guess_counter += 1
          print(f'''Say high ⤒⤒⤒. Your remain guess {self.guess_chance}. 
          Your guessed numbers are: {self.user_guess_numbers}''')
        
    if self.guess_chance == 0:
      print('You lose the game :(')
      
  
game = GuessTheNumber()
