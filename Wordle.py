from colorama import init, Fore, Style


def Wordle(Word):
    init()
    WordA = list(Word.lower())
    

    for z in range(1,5):
        #Var
        Inp = ""
        z = ""
        t = []

        #Ask the player
        while(len(Inp) != 5):
            Inp = input(f"{Fore.BLACK}Enter a 5 letter word: ")
            if len(Inp) !=5:
                print("Try Again (Hint has to be 5 letters)")
        Inp = list(Inp.lower())

        #Win
        if Inp == WordA:
            z = "".join(Inp)
            return (f"{Fore.GREEN} {z}!!").replace(" ", "")
        
        #Check for right Place
        for x in range(len(WordA)):
            t = Inp
            t.pop(int(x-1))
            if WordA[x] == Inp[x]:
                z = (f"{z}{Fore.GREEN} {Word[x]}")
            elif Inp[x] in WordA and Inp[x] not in t:
                z = f"{z}{Fore.YELLOW}{Inp[x]}"
            elif WordA[x] != Inp[x]:
                z = f"{z}{Fore.BLACK}{Inp[x]}"
        print(z.replace(" ", ""))


print(Wordle("House"))