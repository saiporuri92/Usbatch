import time
print("welcome")
try:
    print("try")
    time.sleep(10)
except Exception as err:
    print(err)
except:
    print("except")
finally:
    print("finally")
print("thanks")