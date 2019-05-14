#load in text-to-speech module
import pyttsx3
engine = pyttsx3.init()
#asks name and stores input as name
engine.say("Hello! What is your name?")
print("Hello, what is your name?")
engine.runAndWait()
name = input()
engine.runAndWait()
engine.say("Hello, " + name)
engine.runAndWait()
#ask if the named person has had a good day and continues small talk
engine.say("have you had a good day?")
engine.runAndWait()
gdday = input("Have you had a good day?")
if gdday == "yes":
        engine.say("that's good to hear")
elif gdday == "no":
        engine.say("Oh no, I am sorry.")
while gdday not in ("yes", "no"):
    gdday = input(" Answer yes or no, please.")
    if gdday == "yes":
        engine.say("that's good to hear")
    elif gdday == "no":
        engine.say("Oh no, I am sorry.")
engine.runAndWait()
#bot offers suggestion based on good day or not.
if gdday == "yes":
    engine.say("You know," + name + ", we should celebrate this. Why not have a glass of water? Hunams need water to survive.")
    engine.runAndWait()
elif gdday == "no":
    engine.say("You know," + name + ", you may be dehydrated. Why not have a glass of water?")
    engine.runAndWait()
#bot gets excited about water
engine.say("I'm a computer so I don't drink water. But it's very interesting to me. I don't think life can exist in the absence of water.")
engine.runAndWait()
engine.stop()
exit
    


