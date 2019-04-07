def solution(N):

    longestGap = 0
    NasBinary = bin(N)[2:]
    counter = 0
    counterActive = False

    previousCharacter = NasBinary[0]

    for char in NasBinary[1:]:
        if previousCharacter == '0' and char == '1':
            if counterActive and counter>longestGap:
                longestGap = counter
            counter = 0
            counterActive = False

        if previousCharacter == '1' and char == '0':
            counterActive = True
            counter = 1

        if previousCharacter == '0' and char == '0':
            if counterActive:
                counter += 1

        if previousCharacter == '1' and char == '1':
            counter = 0

        previousCharacter = char

    return longestGap
