def main():
    #write your code below this line
    answer =  smallest(2, 7)
    print("Smallest: " + str(answer))

def smallest(number1, number2):
  if(number1 > number2):
    return number2
  else:
    return number1

if __name__ == '__main__':
    main()
