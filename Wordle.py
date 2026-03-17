from colorama import init, Fore, Style
from collections import Counter


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
        
        #Duplicates
        counts = Counter(Inp)
        duplicates = [char for char, count in counts.items() if count > 1]
        if duplicates == ([char for char, count in (Counter(WordA)).items() if count >1]):
            print("test")

        #Makes Input of player into a list
        Inp = list(Inp.lower())

        #Win
        if Inp == WordA:
            z = "".join(Inp)
            return (f"{Fore.GREEN} {z}!!").replace(" ", "")
        
        #Check for right Place
        for x in range(len(WordA)):
            #t.pop(int(x-1))
            if WordA[x] == Inp[x]:
                z = (f"{z}{Fore.GREEN} {Word[x]}")
            elif Inp[x] in WordA:
                if duplicates == ([char for char, count in (Counter(WordA)).items() if count >1]):
                    z = f"{z}{Fore.YELLOW}{Inp[x]}"
                elif list(Inp[x]) != duplicates:
                    z = f"{z}{Fore.YELLOW}{Inp[x]}"
                else:
                    z = f"{z}{Fore.BLACK}{Inp[x]}"
            elif WordA[x] != Inp[x]:
                z = f"{z}{Fore.BLACK}{Inp[x]}"
        print(z.replace(" ", ""))


print(Wordle("hello"))
