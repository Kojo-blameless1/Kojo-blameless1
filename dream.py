
import random
print(F"HELLO WELCOME TO BLAMELESS  GAMES. \n"
      '\n'
      F'Win somthing Today.. GOOD LUCK \n'
      f'Games Availabe: Dice , guess and lotto \n'
      )
have_fun = "Do you love this game?"
warning = "Letter(s) are not accepted please!! tips guess from 1 - 5"
help_desk = "Incase you need help type [a]🔽 or click on Enter(ke) to QUIT!"

play = input('What Game Do You want to Play. ').lower()
if play == 'dice':
    play_limit = 0

    while play_limit <= 3:
        roll = input('Do you want to roll . yes or no ? ').lower()
        if roll == 'yes':
            attempt = 0
            
            
            dice_1 = random.randint(1, 7)
            dice_2 = random.randint(1, 7)

            print(f'First Dice: {dice_1}\n'
            f'Second Dice: {dice_2}')

            sum = dice_1 +dice_2
            print(f'The sum is {sum}')
        
            if sum >= 8:

                print(f'The sum of the 2 Dice is {sum}\n'
                f'Congratulations you won an order'
                )
                order_choice = ['rice','Pizza' , 'drink']

                orders = input('what will you like to order: , PIZZA, RICE, DRINK : ').lower()
                name = input('Whats your name ? ')
                location = input('We might need your adress for Delivery. whats your adress: ').capitalize()
                
    
                while orders in order_choice:  

                    if orders == 'Pizza':                    
                        pizza_option = 'Vegetable ' 'or ' 'Animal '
                        pizza_choice = input(f'Which form Of pizza do you want {pizza_option}').capitalize()
                        print(f'Hello {name}\n'
                            f"You ordered for Pizza with {pizza_choice} source. \n"
                            f'It will be Delivered {location} in an Hour time. ')
                        break

                    elif orders == 'rice':
                        rice_option = 'Jollof, ' 'Fried  ' 'or ' 'Plain '
                        rice_choice = input(f"which form of Rice do you want {rice_option} ").capitalize()

                        print(f'Hello {name}\n'
                            f"You ordered for {rice_choice} Rice \n"
                            f'It will be Delivered at {location} in an Hour time. ')
                        break

                    elif orders == 'drink':
                        drink_option = 'Hennessy, ' 'cocacola, ''orijin' 
                        drink_choice = input(f"which form of drink do you want {drink_option} ").capitalize()

                        print(f'Hello {name}\n'
                            f"Thanks you ordered for {drink_choice} \n"
                            f'It will be Delivered at {location} in an Hour time. ')
                        break
                    else:
                        break

                        
                
                else:
                    print(f"Hello {name}  We don't have your order in our options")
                    
                    
            else:
                print(f'The sum of the 2 Dice is {sum} you did not win anything')
            
            #again = input('Do you want to play Again : yes or no. ')
            attempt = attempt + 1
            break
        else:
            print('wish to see you play again👏') 
        play_limit = play_limit + 1 
    print(help_desk)
    i_need_help = input("> ")
    if i_need_help == "a":
        print(
            '''
            ------- Help------
Input -- This program only accept int no❌ float and no ❌ strings!

Limits -- You have only Five(3) chances to  roll the Dice. !💯 

contact -- For more details contact the developer (KOJO BLAMELESS) @donkorenoch2002@gmail.com👍✔
                

''')
        print("----------Use small letters----------")
        print(have_fun)
        have_fun = input("Yes or No > ")
        if have_fun == "yes":
            print("Thanks for loving this game, we hope to see you playing always💖")
        elif have_fun == "no":
            print("We're sorry to hear this, we will make sure you enjoy it next time!✔🌹")

    elif i_need_help == "":
        print("GAME OVER!🛑, RUN PROGRAM AGAIN")
        print("----------Use small letters----------")
        print(have_fun)
        have_fun = input("Yes or No > ")
        if have_fun == "yes":
            print("Thanks for loving this game, we hope to see you playing always💖")
        elif have_fun == "no":
            print("We're sorry to hear this, we will make sure you enjoy it next time!✔🌹")

        

        print(f'No of Attempt: {attempt}')
    else:
        print('Thank play Again next Time. ')      
    
    #print('THANKS FOR PLAYING SEE YOU NEXT TIME. ')

elif play == 'guess':
    start = 'yes'
    while start == 'yes':
        number = random.randint(1,5)
        guess = None
        guess_count = 0
        guess_limit = 3
        start_game = ""

        
        print(warning)
        while guess_count < guess_limit:
            guess = float(input("Guess the secret number : "))
            guess_count += 1

            if guess == number:
                print('Congratulation on guessing the correct number\n'
                    'you are a genius!✔💋❤\n'
                    '\n'
                    'YOU HAVE WON AN ORDER😍' )

                orders = input('what will you like to order: , PIZZA, RICE, DRINK : ').lower()
                name = input('Whats your name ? ')
                location = input('We might need your adress for Delivery. whats your adress: ').capitalize()
                order_choice = ['rice','Pizza' , 'drink']
                    
        
                while orders in order_choice:  

                    if orders == 'Pizza':                    
                        pizza_option = 'Vegetable ' 'or ' 'Animal '
                        pizza_choice = input(f'Which form Of pizza do you want {pizza_option}').capitalize()
                        print(f'Hello {name}\n'
                            f"You ordered for Pizza with {pizza_choice} source. \n"
                            f'It will be Delivered {location} in an Hour time. ')
                        break

                    elif orders == 'rice':
                        rice_option = 'Jollof, ' 'Fried  ' 'or ' 'Plain '
                        rice_choice = input(f"which form of Rice do you want {rice_option} ").capitalize()

                        print(f'Hello {name}\n'
                                f"You ordered for {rice_choice} Rice \n"
                                f'It will be Delivered at {location} in an Hour time. ')
                        break

                    elif orders == 'drink':
                        drink_option = 'Hennessy, ' 'cocacola, ''orijin' 
                        drink_choice = input(f"which form of drink do you want {drink_option} ").capitalize()

                        print(f'Hello {name}\n'
                                f"Thanks you ordered for {drink_choice} \n"
                                f'It will be Delivered at {location} in an Hour time. ')
                        break
                    else:
                        break

                                
                        
                else:
                    print(f"Hello {name}  We don't have your order in our options")
                            

                print(have_fun)
                print("----------Use small letters----------")
                have_fun = input("Yes or No > ")

                if have_fun == "yes":
                    print("Thanks for loving this game, we hope to see you playing always💖")
                elif have_fun == "no":

                    print("We're sorry to hear this, we will make sure you enjoy it next time!✔🌹")
                break
            elif guess_count == guess_limit:
                print("Sorry you've use all your chances😂, run the program again💥")

                print(help_desk)
                i_need_help = input("> ")
                if i_need_help == "a":
                    print(
                        '''
                        ------- Help------
        Input -- This program only accept int and float no ❌ strings!

        Limits -- You have only three chances to Guess the secret number!💯 

        contact -- For more details contact the developer (KoJo Blameless) @donkorenoch2002@gmail.com
                        

        ''')
                    print("----------Use small letters----------")
                    print(have_fun)
                    have_fun = input("Yes or No > ")

                    if have_fun == "yes":
                        print("Thanks for loving this game, we hope to see you playing always💖")

                    elif have_fun == "no":
                        print("We're sorry to hear this, we will make sure you enjoy it next time!✔🌹")

                elif i_need_help == "":
                    print("GAME OVER!🛑, RUN PROGRAM AGAIN")
                    print("----------Use small letters----------")
                    print(have_fun)
                    have_fun = input("Yes or No > ")

                    if have_fun == "yes":
                        print("Thanks for loving this game, we hope to see you playing always💖")
                    elif have_fun == "no":
                        print("We're sorry to hear this, we will make sure you enjoy it next time!✔🌹")
                    break
                break
            else:
                print("Sorry you have to guess again (:")
                continue

        else:
            print('Your selected Game is not in the Option. ')

        start_game = input("do you want to start the Game. ")
elif play == 'lotto':
    lotto = input('Do you want to play. yes or no ? ').lower()
    if lotto == 'yes':
        print(f'\n'
            f'Tips for The Lottory Game👍 \n'
            f'Guess from 1-10\n'
            f'No❌ floating Number , No ❌strings, only integers✔')

        list = []
        for num in range(1,6):
            Number = random.randint(1,10)
            list.append(Number)

        player_choice = int(input('Enter a Number from 1-10: '))
        if player_choice in list:
            print(f'congratulations You Have won the Lottery ✔😁\n '
            f'The numbers  are {list}\n'
            f'You have won an order')
            order_choice = ['rice','Pizza' , 'drink']

            orders = input('what will you like to order: , PIZZA, RICE, DRINK : ').lower()
            name = input('Whats your name ? ')
            location = input('We might need your adress for Delivery. whats your adress: ').capitalize()


            while orders in order_choice:  

                if orders == 'Pizza':                    
                    pizza_option = 'Vegetable ' 'or ' 'Animal '
                    pizza_choice = input(f'Which form Of pizza do you want {pizza_option}').capitalize()
                    print(f'Hello {name}\n'
                        f"You ordered for Pizza with {pizza_choice} source. \n"
                        f'It will be Delivered {location} in an Hour time. ')
                    continue
                

                elif orders == 'rice':
                    rice_option = 'Jollof, ' 'Fried  ' 'or ' 'Plain '
                    rice_choice = input(f"which form of Rice do you want {rice_option} ").capitalize()

                    print(f'Hello {name}\n'
                        f"You ordered for {rice_choice} Rice \n"
                        f'It will be Delivered at {location} in an Hour time. ')
                    continue
                    

                elif orders == 'drink':
                    drink_option = 'Hennessy, ' 'cocacola, ''orijin' 
                    drink_choice = input(f"which form of drink do you want {drink_option} ").capitalize()

                    print(f'Hello {name}\n'
                        f"Thanks you ordered for {drink_choice} \n"
                        f'It will be Delivered at {location} in an Hour time. ')
                    continue
                    
                else:
                    continue
            else:
                print(f"Hello {name}  We don't have your order in our options")
                
        else:
            print(f'Sorry you Didnt Win This set\n'
                f'The Numbers are {list}\n')

    
    else:
        print('We Hope To see you play another Time.😢')

        

else:
    print('The Game you selected is not in the Available Games😢.')