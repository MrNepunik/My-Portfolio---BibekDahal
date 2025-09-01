def kbc():
    print("Welcome to KBC")
    print("You will be asked 10 questions")
    print("You can exit at any time by pressing 0")
    print("You will be given 4 options for each question\n")

    # Q1
    print("Q1: Which is the capital city of Nepal?")
    options = ["1. Kathmandu", "2. Pokhara", "3. Biratnagar", "4. Chitwan"]
    print(options)
    ans = int(input("Choose the correct answer: "))
    if ans == 1:
        print("Correct! You have won Rs.1000\n")
    else:
        print("Incorrect. You have won nothing.\nThanks for playing.")
        return

    # Q2
    print("Q2: What is the height of Mt. Everest?")
    options = ["1. 7789", "2. 8845", "3. 8848", "4. 8849"]
    print(options)
    ans = int(input("Choose the correct answer: "))
    if ans == 3:
        print("Correct! You have won Rs.10,000\n")
    else:
        print("Incorrect. You have won nothing.\nThanks for playing.")
        return

    # Q3
    print("Q3: Which planet is known as the Red Planet?")
    options = ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"]
    print(options)
    ans = int(input("Choose the correct answer: "))
    if ans == 2:
        print("Correct! You have won Rs.20,000\n")
    else:
        print("Incorrect. You have won Rs.1000\nThanks for playing.")
        return

    # Q4
    print("Q4: Which is the National Song of Nepal?")
    options = ["1. Rato ra Chandra Surya", "2. Sayau Thunga Ful ka hami", "3. Shereeman Gambir", "4. Yo Nepali Shir Uchali"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 1:
        print("Correct! You have won Rs.50,000\n")
    elif ans == 0:
        print("You have won Rs.20,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.10,000\nThanks for playing.")
        return

    # Q5
    print("Q5: Which is the largest gorge of Nepal?")
    options = ["1. Budi Gandaki", "2. Kali Gandaki", "3. Koshi", "4. Karnali"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 2:
        print("Correct! You have won Rs.100,000\n")
    elif ans == 0:
        print("You have won Rs.50,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.20,000\nThanks for playing.")
        return

    # Q6
    print("Q6: Which is the second highest peak of the world?")
    options = ["1. Saipal", "2. Annapurna", "3. Kanchanjunga", "4. Mt. K2"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 4:
        print("Correct! You have won Rs.200,000\n")
    elif ans == 0:
        print("You have won Rs.100,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.50,000\nThanks for playing.")
        return

    # Q7
    print("Q7: Who was the Prime Minister of Nepal during World War 2?")
    options = ["1. Mohan Shumsher", "2. Chandra Shumsher", "3. Juddha Shumsher", "4. Padma Shumsher"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 2:
        print("Correct! You have won Rs.400,000\n")
    elif ans == 0:
        print("You have won Rs.200,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.100,000\nThanks for playing.")
        return

    # Q8
    print("Q8: Ncell was previously known by which name?")
    options = ["1. Mero Mobile", "2. New-Cell", "3. Nepal-Cell", "4. Mero Phone"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 1:
        print("Correct! You have won Rs.750,000\n")
    elif ans == 0:
        print("You have won Rs.400,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.200,000\nThanks for playing.")
        return

    # Q9
    print("Q9: Which is the big country that was formed after the separation of the Soviet Union?")
    options = ["1. Finland", "2. Belgium", "3. Bolivia", "4. Ukraine"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 4:
        print("Correct! You have won Rs.1,000,000\n")
    elif ans == 0:
        print("You have won Rs.400,000\nThanks for playing.")
        return
    else:
        print("Incorrect. You have won Rs.200,000\nThanks for playing.")
        return

    # Q10
    print("Q10: In which year did Nepal get membership of the United Nations (UN)?")
    options = ["1. 2008 BS", "2. 2056 BS", "3. 2068 BS", "4. 2065 BS"]
    print(options)
    ans = int(input("Choose the correct answer [To exit press 0]: "))
    if ans == 2:
        print("Correct! 🎉 You have won the grand prize of Rs.2,000,000!")
    elif ans == 0:
        print("You have won Rs.400,000\nThanks for playing.")
    else:
        print("Incorrect. You have won Rs.200,000\nThanks for playing.")

# Start the game
kbc()
# End of the game 
# Thank you for palying KBC 