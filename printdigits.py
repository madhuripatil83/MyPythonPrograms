
def print_digits(num):
    tensdig = int(num) //10
    print("tens digit of " + str(num)  + " is " + str(tensdig))
    onesdig = int(num) % 10
    print("ones digit of " + str(num)  + " is " + str(onesdig))

def main():
     print ("enter a digit in range 0 to 99\n")  
     num = int(input())
     print_digits(num)

main()     
