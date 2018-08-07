from sys import exit
from sys import argv

def start():
    print "Jubilee is leaving the mall with some sweet new threads and spies a Sentinel!!"
    print "Holy SMOKES!!"
    print "She could run, hide, or fight..."
    print "What should she do??"

    next = raw_input("> ")
    next_selection = next.lower().replace("!","")

    if next_selection == "run":
        nyc_streets()
    elif next_selection == "hide":
        good_call()
    elif next_selection == "fight":
        make_a_stand()
    else:
        start()

def nyc_streets():
    print "Jubilee makes a break for it and totally ditches that tin can!"
    print "She gets to Times Square only to discover an ARMY OF SENTINELS"
    print "What the CRAP?! "
    print "What should she do now??"

    next = raw_input("> ")
    next_selection = next.lower().replace("!","")

    if next_selection == "run":
        beast()
    elif next_selection == "hide":
        wolverine()
    elif next_selection == "fight":
        pep_rally()


def beast():
    print "Jubilee turns and burns hoping to make a call for help..."
    print "She heads down to the subway tunnels and runs into Beast!"
    print "Beast helps Jubilee escape and call for help!"
    print "Together, they save the day!"
    exit(0)

def wolverine():
    print "Jubilee ducks into an alley to hide and runs into Wolverine!"
    print "He'll take it from here- Jubilee hides safely in a dumpster..."
    exit(0)

def pep_rally():
    print "Jubilee summons her courage to make a stand when suddenly..."
    print "The X-Men arrive in the blackbird overhead!!"
    print "This business is HANDLED."
    exit(0)

def good_call():
    print "Good call- our hero is no match for a Sentinel."
    print "Jubilee runs back into the mall and uses her com to call Cyclops for help."
    exit(0)

def make_a_stand():
    print "Brave girl!"
    print "You've got a few basic attacks in that yellow trench..."
    print "You can fire off an energy_blast, a photo_flash, or use independence_day..."
    print "What's it gonna be??"

    next = raw_input("> ")
    next_selection = next.lower().replace("!","")

    if next_selection == "energy_blast":
        slowed()
    elif next_selection == "photo_flash":
        kiddin()
    elif next_selection == "independence_day":
        take_down()
    else:
        dead("Ya hesitated... Jubilee was squashed like a yellow bug.")

def dead(why):
    print why
    exit(0)

def slowed():
    print "Oh man! That sure slowed the big guy down!"
    print "You may not be able to finish this fight... run for help or fight on?"

    next = raw_input("> ")
    next_selection = next.lower().replace("!","")

    if "run" in next_selection:
        wolverine()
    elif "fight" in next_selection:
        make_a_stand()
    else:
        dead("No time to hesitate, girl. You're toast.")

def kiddin():
    print "Are ya kiddin me? Tryin' to Photo Flash a SENTINEL??"
    print "Sorry, kiddo, that's not gonna fly"
    dead("A Sentinel is not blinded by some mild light tricks")

def take_down():
    print "CHYEA BUDDY! This burst of firecracker fury takes down the Sentinel!"
    print "Way to save the day!"
    exit(0)

start()
