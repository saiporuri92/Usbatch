import logging
print("welcome")
logging.info(".......program execution started .....")
a=input("Enter a value:")
b=input("Enter b value:")
logging.info("a,b values extered successfully")
logging.debug(f"before conversion a={a},b={b}")
try:
    a=float(a)
    logging.info("a value converted")
    b=float(b)
    logging.info("b value converted")
    logging.debug(f"after conversion a={a},b={b}")
    res=a/b
    logging.info("result calculated well")
    print(f"res={res}")
    logging.debug("res=%s"%res)
except ZeroDivisionError as err:
    print("expecting b!=0")
    logging.exception(err)
except ValueError as err:
    print("expecting nly digits")
    logging.exception(err)
except Exception as err:
    print(err)
    logging.exception(err)
print("thanks")
logging.info(".....program execution completed.....")