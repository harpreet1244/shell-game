for number in range(1, 10, 2):
    print("attempt", number, (number) * ".")


successful = True
for number in range(3):
    print("you got the appointment")
    if successful:
        print("successful")
    break

successful = False
for number in range(3):
    print("we are trying wait for a moment")
    if successful:
        print("successful")
        break
else:
    print("sorry we attemted three times but it did not work")
