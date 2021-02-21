#region Importations
import os, sys, math, requests, json, random
from datetime import datetime
cur = "Assistant"
#endregion

#region Time and date
now = datetime.now()
today = datetime.today()
hour = now.strftime("%H")
dia = [5, 6, 7, 8, 9, 10, 11]
tarde = [12, 13, 14, 15, 16, 17, 18]
noite = [19, 20, 21, 22, 23]
madrugada = [0, 1, 2, 3, 4]
time = now.strftime("%Hh%M")
date = today.strftime("%A, day %d of %message, in year %Y")
t = ""
if int(hour) in dia:
    t = "morning"
    print("Good morning Arthur!")
elif int(hour) in tarde:
    t = "afternoon"
    print("Godd afternoon!")
elif int(hour) in noite:
    t = "night"
    print("What a beautiful night, isn't it?")
elif int(hour) in madrugada:
    t = "midnight"
    print("I think it's late for a bath. Anyway, welcome!")
print(f"Now it's: {time},\n{date}.")
#endregion

#region Main
def main():
    command = input("Please, insert a command\n")
    def try_again():
        comm = input("Looks that job is done. Anything more?\n")
        if comm == "yes":
            main()
        else:
            print(f"That's ok! Have a wonderful {t}!")
            exit

    # File command
    if command == "file":
        dir_name = input("File name: ")
        dir_dir = input("Folder: ")
        if dir_dir == "current":
            os.system(f"sh ./test.sh ~/{cur} {dir_name}")
            dir_dir = cur

        os.system(f"sh ./test.sh ~/{dir_dir} {dir_name}")

        message = input("Want to write on it? ")
        if message == "yes":
            m = input("Insert the mono-line content: ")
            os.system(f"sh ./test.sh ~/{cur} writeon.sh")

            f_ = open("writeon.sh", "w")
            f_.write(f"cd {dir_dir}\n")
            f_.write(f"echo '{m}' >> '{dir_name}'")

            os.system(f"sh ./writeon.sh")
            os.remove("writeon.sh")
        elif message == "no":
            exit

        excl = input("Exclude it? ")
        if excl == "sim":
            f = open(f'~/{dir_dir}/{dir_name}')
            print(f.read())
            os.remove(f'~{dir_dir}/{dir_name}')
        elif excl == "no":
            try_again()

    # Folder command
    elif command == "folder":
        f_name = input("Insert the folder name: ")
        f_dir = input("Insert the folder diretory: ")
        if f_dir == "current":
            f_dir = cur
        os.system(f"sh ./folder.sh ~/{f_dir} {f_name}")
        try_again()

    # Workdspace command
    elif command == "workspace":
        w_name = input("Insert the workspace name: ")

        w_dir = input("Insert the workspace diretory: ")
        if w_dir == "current":
            w_dir = cur

        w_lang = input("Insert the workspace language: ")

        def make(type, lang):
            if w_lang == f"{type}":
                os.system(f"sh ./workspace.sh ~/{w_dir} {w_name} {lang}")

        make("web", "index.html style.css script.js")
        make("html", "index.html")
        make("python", "main.py")
        make("kotlin", "main.kotlin")
        make("cpp", "main.cpp")
        make("c", "main.c")
        make("ts", "main.ts")

        # u = open("workspace.sh", "r")
        # print(u.read())
        try_again()

    # Periodic decimate command
    elif command == "dizcalc":
        diz = input("Insert the periodic decimate: ")
        n = diz.split(",")

        def get_number_of_elements(list):
            count = 0
            for element in list:
                count += 1
            return count

        if (get_number_of_elements(n) == 2):
            integer = int(n[0])
            decimate = int(n[1])

            digits = int(math.log10(decimate)) + 1
            numerator = decimate

            num = ""
            for x in range(digits):
                num += "9"
            denominator = num

            numerator += (integer * int(denominator))
        elif (get_number_of_elements(n) == 3):
            integer = n[0]
            irregular = n[1]
            decimate = n[2]

            n_digits = int(len(decimate))
            d_digits = int(len(irregular))

            num = ""
            num1 = ""
            for x in range(n_digits):
                num += "9"
            for x in range(d_digits):
                num1 += "0"
            denominator = num + num1

            n_ = irregular + decimate
            numerator = (int(n_) - int(irregular))

        print(f"{numerator}/{denominator}")
        try_again()

    # Casual talking
    elif command == "lets talk":
        print("What's up? ")
        com = input("")
        
        if com == "get me some inspiration":   
            url_insp = "https://zenquotes.io/api/random"
            url_anime = "https://animechanapi.xyz/api/quotes/random"
            c = random.randrange(1, 3)
            if c == 1:
                response = requests.get(url_anime)
                data = json.loads(response.text)
                print("Here's a good one from the anime " + data['data'][0]['anime'] + ":")
                print(data['data'][0]['quote'] + " By " + data['data'][0]['character'] + ".")
            elif c == 2:
                response = requests.get(url_insp)
                data = json.loads(response.text)
                print("Thats a great quote by " + data[0]['a'] + ":")
                print(data[0]['q'])
        
        try_again()
        
    # Unknown command
    else:
        print("Sorry, This command is unknown fo me!\nLet's try again?")
        inp = input()
        if inp == "yes":
            main()
        else:
            exit
main()
#endregion