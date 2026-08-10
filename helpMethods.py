
def getNumber(prompt = "", numberType = float):
    while True:
        try:
            num = numberType(input(prompt))
        except ValueError as e:
            print("Invalid Input. It should be a number")
        else:
            break
    return num


def getNumberInRange(rangeStart, rangeEnd):
    prompt = f"Enter a number between {rangeStart} and {rangeEnd}: "
    num = getNumber(prompt, int)

    while not (num >= rangeStart and num <= rangeEnd):
        print("Invalid Number")
        num = getNumber(prompt, int)

    return num
