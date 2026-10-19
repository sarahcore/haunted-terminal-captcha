
import random
import sys
import time


def digitar(texto, velocidade):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)


print("\033[40m\033[38;2;121;184;138m", end="")

humanidade = 15

print("Initializing verification system...\n")
time.sleep(2)

print("System ready.\n")
time.sleep(1)

print("Human verification required.\n")
time.sleep(0.5)

print("Press ENTER to begin.\n")
input("> ")

print("\nTEST 001 - CHARACTER VERIFICATION\n")
print("Enter the following characters:\n")
print("K7MXC8S\n")

test1 = input("> ").upper()
if test1 != "K7MXC8S":
    humanidade -= 1

time.sleep(1)

print("\nTEST 002 - SYMBOL RECOGNITION\n")
print("Count the number of # symbols.\n")
print("# @ # % & # $ # @\n")

test2 = input("> ")
if test2 != "4":
    humanidade -= 1

time.sleep(1)

print("\nTEST 003 - SEQUENCE VERIFICATION\n")
print("Complete the sequence:\n")
print("2, 4, 6, 8, ?\n")

test3 = input("> ")
if test3 != "10":
    humanidade -= 1

time.sleep(1)

print("\nTEST 004 - TEXT VERIFICATION\n")
print("Enter the following word in reverse:\n")
print("SECURITY\n")

test4 = input("> ").upper()
if test4 != "YTIRUCES":
    humanidade -= 1

time.sleep(1)

print("\nTEST 005 - MEMORY VERIFICATION\n")
print("Did you initiate this session?\n")
print("[1] YES")
print("[2] NO\n")

input("> ")
time.sleep(2.5)

digitar("\nIncorrect. Please try again.", 0.13)

test5 = input("\n> ")
if test5 != "1":
    humanidade -= 1

time.sleep(1.5)

print("\nVerification complete.\n")
print("Proceeding...")

time.sleep(1)

print("\nTEST 006 - NUMBER VERIFICATION\n")
print("What is 7 + 5?\n")

test6 = input("> ")
if test6 != "12":
    humanidade -= 1

print("\nVerification complete.\n")
time.sleep(1.5)

print("Verification complete.\n")
time.sleep(2.5)

digitar("Duplicate confirmation detected.\n", 0.06)
time.sleep(1)

print("Removing duplicate...\n")
time.sleep(1)

print("Proceeding...")

time.sleep(1)

print("\nTEST 007 - SESSION VERIFICATION\n")
print("How many people are currently")
print("using this terminal?\n")

input("> ")

print("\nSession validation complete.\n")
print("Expected users: 1")
time.sleep(2.5)

print("Detected users:")
digitar("UNVERIFIED.\n", 0.10)
time.sleep(4)

print("Please do not allow anyone else")
print("to complete this verification.\n")
time.sleep(1.5)

print("Proceeding...")

time.sleep(1)

print("\nTEST 008 - RESPONSE ANALYSIS\n")
print("Enter the following word:\n")
print("WINDOW\n")

test8 = input("> ").upper()
if test8 != "WINDOW":
    humanidade -= 1

print("\nAnalyzing response time...\n")
time.sleep(2.5)

resultado = random.choice(["NORMAL", "ATYPICAL"])

print("Response pattern:")
print(f"{resultado}\n")
time.sleep(1.5)

print("Input origin:")
print("UNIDENTIFIED.\n")
time.sleep(1.5)

print("Observer status: ACTIVE", end="", flush=True)
time.sleep(1.5)

print("\r\033[2K", end="", flush=True)

digitar("Please don't look through your window.\n", 0.12)
time.sleep(1.5)
print("\nProceeding...")

time.sleep(1)

print("\nTEST 009 - PRESENCE VERIFICATION\n")
print("Are you alone in the room?\n")
print("[1] YES")
print("[2] NO\n")

input("> ")
time.sleep(2.5)

print("\nResponse recorded.\n")
time.sleep(4)

print("Human presence: 1")
print("Unclassified presence: 1\n")
time.sleep(1.5)

print("Total occupants:")
digitar("UNKNOWN.", 0.12)
time.sleep(2)

print("\nProceeding...")

time.sleep(1)

print("\nTEST 010 - DECISION VERIFICATION\n")
print("Select one of the following.\n")
print("[1] TRUE")
print("[2] FALSE\n")

test10 = input("> ")
if test10 != "1" and test10 != "2":
    humanidade -= 1

print("\nResponse recorded.\n")
time.sleep(2.5)

print("Decision consistency:")
digitar("FAILED.", 0.08)
time.sleep(1.5)

print("\nNo reference statement provided.\n")
print("Proceeding...")

time.sleep(1)

print("\nTEST 011 - FACIAL VERIFICATION\n")
print("Is your face currently")
print("visible to the device?\n")
print("[1] YES")
print("[2] NO\n")

input("> ")

print("\nFacial landmarks:")
print("DETECTED.")
time.sleep(1.5)

digitar("Face count: 2", 0.12)
time.sleep(4)

print("\nCamera status:")
print("DISCONNECTED.")
time.sleep(1.5)

print("\nContinuing...")

time.sleep(1)

print("\nTEST 012 - BEHAVIORAL VERIFICATION\n")
print("Select the most human response.\n")
print("[1] Follow instructions.")
print("[2] Question instructions.")
print("[3] Ignore instructions.")
print("[4] Refuse to answer.\n")

test12 = input("> ")
if test12 not in ["1", "2", "3", "4"]:
    humanidade -= 1

print("\nResponse recorded.\n")
time.sleep(2.5)

print("Behavior classification:")
digitar("UNDEFINED.", 0.08)
time.sleep(1.5)

print("\nHuman verification continues.")

time.sleep(1)

print("\nTEST 013 - ATTENTION VERIFICATION\n")
print("Read the following instruction.\n")
print("Do not look away from the screen.\n")
print("Press ENTER when ready.\n")

test13 = input("> ")
if test13 != "":
    humanidade -= 1

print("\nInput detected.")
time.sleep(3.5)

print("\nResponse length: 8192")
print("Source: UNKNOWN.\n")
time.sleep(1.5)

print("Attention verified.\n")
time.sleep(4)

print("Visual confirmation:")
print("UNAVAILABLE.\n")
time.sleep(2)

digitar("Secondary observer:\n", 0.12)
digitar("DETECTED.", 0.16)
time.sleep(2.5)

print("\nProceeding...")

time.sleep(1)

print("\nTEST 014 - IDENTITY CONFIRMATION\n")
print("Before proceeding, please confirm:\n")
print("Are you human?\n")
print("[1] YES")
print("[2] NO\n")

test14 = input("> ")
if test14 == "2":
    humanidade -= 2
elif test14 != "1":
    humanidade -= 1

print("\nResponse recorded.\n")
time.sleep(2.5)

print("Self-identification:")
digitar("UNVERIFIED.\n", 0.15)
time.sleep(3.5)

print("One test remaining.")

time.sleep(1)

print("\nTEST 015 - FINAL VERIFICATION\n")
print("Final verification required.\n")
print("Please confirm that all previous")
print("responses were your own.\n")
print("[1] CONFIRM")
print("[2] DENY\n")

test15 = input("> ")
if test15 != "1":
    humanidade -= 1

print("\nResponse recorded.\n")
time.sleep(2.5)

print("Verifying response ownership...\n")
time.sleep(4)

print("Ownership:")
digitar("UNCONFIRMED.\n", 0.12)
time.sleep(1.5)

print("Additional confirmation required.\n")
time.sleep(1)

print("[ ] I am not a robot.\n")
print("Type X to check the box.\n")

addtest = input("> ").upper()
if addtest != "X":
    humanidade -= 1

time.sleep(2.5)

print("\n[X] I am not a robot.\n")
print("Checkbox verification successful.\n")
time.sleep(4)

print("Human verification:")
print("PENDING.\n")
print("Calculating final result...\n")

penalidadefinal = random.randint(0, 3)
humanidade -= penalidadefinal

time.sleep(6)

print("Verification complete.\n")
time.sleep(1)

if humanidade >= 14:
    classificacao = "HUMAN"
    print("Classification:")
    time.sleep(1)

    print("HUMAN\n")
    time.sleep(1.5)

    digitar("You passed.\n", 0.10)
    time.sleep(1.5)

    digitar("Please stay safe.", 0.15)

elif humanidade >= 9:
    classificacao = "INCONCLUSIVE"
    print("Classification:")
    time.sleep(1)

    print("INCONCLUSIVE\n")
    time.sleep(1.5)

    digitar("We couldn't verify your humanity.\n", 0.10)
    time.sleep(1.5)

    digitar("We couldn't rule it out either.\n", 0.10)
    time.sleep(1.5)

    digitar("Proceed with caution.", 0.15)

else:
    classificacao = "NON-HUMAN"
    print("Classification:")
    time.sleep(1)

    print("NON-HUMAN\n")
    time.sleep(1.5)

    digitar("I don't think you're human.\n", 0.10)
    time.sleep(1.5)

    digitar("If you are...\n", 0.10)
    time.sleep(1.5)

    digitar("Be aware.", 0.15)

time.sleep(2)

print("\nPress ENTER to exit.\n")
input("> ")

print("\033[0m", end="")
