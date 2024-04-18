import random
def generate_otp(l):
    print("generate otp")
    otp=''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',k=l))
    return otp
otp = generate_otp(4)
print("the generated otp is :",otp)