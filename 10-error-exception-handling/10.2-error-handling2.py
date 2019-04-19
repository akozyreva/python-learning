def ask_for_int():
    # we create while, which runs until user will enter a correct number
    while True:
        try:
            result = int(input("Please provide a number: "))
        except Exception:
            print("Woops! That's not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except")
            print("I will always run in the end")


ask_for_int()
