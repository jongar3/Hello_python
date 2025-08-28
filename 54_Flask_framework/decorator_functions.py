import time


def delay_decorator(function):
    def inner():

        #DO SOMETHING BEFORE THE FUNCTION
        time.sleep(2)
        function()
        function() #Maybe u want to run the function twice
        #DO SOMETHING AFTER THE FUNCTION

    return inner 

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye!")

def say_greetings():
    print("How are you?")

say_bye()
#alternative to the @

delay_decorator(say_greetings)()