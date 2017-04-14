from tkinter import *
from getallsymbole import ElementList

characters = re.compile(r'[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]')


def ichsuche(allel, inpud):
    loesung = []
    hit = False
    while inpud != "":
        for element in allel[::-1]:
            if element == inpud[:len(element)].title():
                loesung.append(element)
                inpud = inpud[len(element):]
                hit = True
                break
            else:
                continue
        if hit != True:
            loesung.append(inpud[0])
            inpud = inpud[1:]
        hit = False
    return loesung

                # if inpud == "":
                #     return loesung
                # for i in kurz:
                #     i = i.lower()
                #     ilen = len(i)
                #     if inpud[:ilen] == i:
                #         loesung.append(i)
                #         print(inpud[ilen:])
                #         hier = ichsuche(kurz, inpud[ilen:], loesung)
                #         if hier != "nothing found":
                #             return hier
                #         loesung = loesung[:len(loesung) - 1]
                # print("nothing found")
                #
                # return "nothing found"


def take_care_of_inpud(inpud) -> str:
    inpud = inpud.lower()  # halving number of replacements (äöü)
    inpud = re.sub('ä', 'ae', inpud)
    inpud = re.sub('ö', 'oe', inpud)
    inpud = re.sub('ü', 'ue', inpud)
    inpud = re.sub(characters, '', inpud)  # remove everything that is not a letter, after umlauts are replaced
    return inpud


def letthefunbegin(allel, inpud):
    inpud = take_care_of_inpud(inpud.get())
    print(inpud)
    loesung = ichsuche(allel, inpud)
    print(loesung)
    if not isinstance(loesung, str):
        loesung = ElementList(*[allel[l] for l in [l.title() for l in loesung]])  # get element by its short from dict
    showloesung(loesung)


def showloesung(loesung):
    print(loesung)

    master = Tk()
    master.wm_title("CHEMIE IST COOL")

    cheight = 100
    cwidth = len(loesung) * 26 if (len(loesung) * 26) > 120 else 120
    canvas = Canvas(master, height=cheight, width=cwidth, bg="white")

    tempwidth = 0
    if isinstance(loesung, str):
        canvas.create_text(cwidth / 2, cheight / 2, text="nothing found", font=("Century Gothic", 11))
    else:  # make method for ElementList from the code below
        for l in loesung.values():
            print(l)
            tempwidth += 24
            # alles schwarz
            canvas.create_rectangle(tempwidth - 12, 40, tempwidth + 12, 60, fill=l.color)
            # schrift
            canvas.create_text(tempwidth, cheight / 2, text=l.short, font=("Century Gothic", 11))

    # button mit showNumbers... Wenn an dann sollen die Zahlen des Elements unter der Box erscheinen

    # button mit showFullNames...
    canvas.pack()
    master.focus_force()  # to give the new window focus

    # master.mainloop() ???
