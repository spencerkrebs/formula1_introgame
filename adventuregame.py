import time
import random

outcomes_ferrari = ['Charles Leclerc\'s Ferrari is too fast and you '
                    'can\'t keep up.',
                    'The young Charles Leclerc made a rookie mistake and '
                    'forgot to activate his DRS!']
outcomes_redbull = ['Red Bull\'s new Honda upgrades are paying off, and you '
                    'can\'t keep up.',
                    'Max Verstappen spun out trying to warm up his tires '
                    'in the middle of the race!']


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause('You are racing in the Formula 1 Grand Prix.\n')
    print_pause('You have just entered the longest straightaway of the '
                'track.\n')
    print_pause('In front of you are two cars:\n')
    print_pause('Charles Leclerc in the Ferrari\n')
    print_pause('and Max Verstappen in the Red Bull Honda.')
    print_pause('Which car do you want to draft?')


def player_choice():
        decision = input("Enter 1 to follow Charles Leclerc in the Ferrari.\n"
                         "Enter 2 to follow Max Verstappen in the Red Bull "
                         "Honda.\n")
        if decision == '1':
            result = random.choice(outcomes_ferrari)
            if result == outcomes_ferrari[0]:
                print_pause(result)
                print_pause('You have lost the race. GAME OVER.')
                play_again()
            elif result == outcomes_ferrari[1]:
                print_pause(result)
                print_pause('You overtook Leclerc and won the Grand Prix!')
                play_again()
        elif decision == '2':
            result = random.choice(outcomes_redbull)
            if result == outcomes_redbull[0]:
                print_pause(result)
                print_pause('You have lost the race. GAME OVER.')
                play_again()
            elif result == outcomes_redbull[1]:
                print_pause(result)
                print_pause('You overtook Verstappen and won the Grand Prix!')
                play_again()
        else:
            print_pause('Sorry, the input is invalid. Please try again,'
                        'but hurry! You are losing time!')
            play_again()

def play_again():
        response = input('Would you like to play again? '
                         'Enter \'yes\' or \'no\':\n').lower()
        if 'no' in response:
            print_pause('Ok, goodbye!')
        elif 'yes' in response:
            print_pause('Vroom! Vroom! Vroom! Let\'s play again!')
            race()
        else:
            print_pause("Invalid Input")


def race():
    intro()
    player_choice()


race()
