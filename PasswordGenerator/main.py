import random

numbers = '1234567890'
symbols = '~!@#$%^&*()_+=-`><?/\|][}{,.'
letters = 'qwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM'

def password_generator(letters_count):
  password = ''
  for i in range(letters_count // 3):
    password += random.choice(numbers)
    password += random.choice(symbols)
    password += random.choice(letters)

  random.shuffle(list(password))
  return password

password_generator(143)
