#try 
#except
#raise
#finally

try:
    print("In try block")
    print("All going well!!!")
    raise ValueError("Raising value error")
except ValueError as ve:
    print(ve)
    raise KeyboardInterrupt
except:
    print("some exception raised!!")
finally:
    print("what had to happen has already happened!!!")