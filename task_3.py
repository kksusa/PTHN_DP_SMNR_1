from random import randint
from time import sleep


def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if UPPER_LIMIT >= number > LOWER_LIMIT:
                return number
            else:
                print("Ð§Ð¸ÑÐ»Ð¾ Ð²Ð²ÐµÐ´ÐµÐ½Ð¾ Ð½ÐµÐ¿Ñ€Ð°Ð²Ð¸Ð»ÑŒÐ½Ð¾.")
        except:
            print("Ð§Ð¸ÑÐ»Ð¾ Ð²Ð²ÐµÐ´ÐµÐ½Ð¾ Ð½ÐµÐ¿Ñ€Ð°Ð²Ð¸Ð»ÑŒÐ½Ð¾.")


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
number = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Ð˜Ñ‚Ð°Ðº, Ñ Ð·Ð°Ð³Ð°Ð´Ð°Ð» Ñ‡Ð¸ÑÐ»Ð¾ Ð¾Ñ‚ {LOWER_LIMIT} Ð´Ð¾ {UPPER_LIMIT}...")
sleep(1)
print("ÐŸÐ¾Ð¿Ñ€Ð¾Ð±ÑƒÐ¹ ÐµÐ³Ð¾ Ð¾Ñ‚Ð³Ð°Ð´Ð°Ñ‚ÑŒ.")
sleep(1)
win = False
for i in range(10):
    user_number = CheckNumbers(f"ÐŸÐ¾Ð¿Ñ‹Ñ‚ÐºÐ° {i + 1}:")
    if number == user_number:
        print("Ð£Ñ€Ð°, Ñ‚Ñ‹ Ð¾Ñ‚Ð³Ð°Ð´Ð°Ð» ÐµÐ³Ð¾!")
        win = True
        break
    elif user_number < number:
        print("ÐœÐ¾Ñ‘ Ñ‡Ð¸ÑÐ»Ð¾ Ð±Ð¾Ð»ÑŒÑˆÐµ...")
    else:
        print("ÐœÐ¾Ñ‘ Ñ‡Ð¸ÑÐ»Ð¾ Ð¼ÐµÐ½ÑŒÑˆÐµ...")
if win == False:
    print("Ð§Ñ‚Ð¾ Ð¶, Ð½Ðµ Ð¿Ð¾Ð²ÐµÐ·Ð»Ð¾...\nÐŸÐ¾Ð¿Ñ€Ð¾Ð±ÑƒÐµÐ¼ Ð² ÑÐ»ÐµÐ´ÑƒÑŽÑŽÑ‰Ð¸Ð¹ Ñ€Ð°Ð·?")
