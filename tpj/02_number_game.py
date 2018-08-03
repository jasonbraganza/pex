import random

print('------------------------------------------')
print('             Number Game!')
print('------------------------------------------')

the_num = random.randint(1, 100)

get_num = -1

while get_num != the_num:
    get_num = int(input("Enter a number between 1 and 100: "))

    if get_num == the_num:
        print(f"You guessed {get_num}. Yay! You win!")
        break
    elif get_num < the_num:
        print(f"You guessed {get_num}. That’s low!")
        continue
    elif get_num > the_num:
        print(f"You guessed {get_num}. That’s high!")
        continue
