__author__ = 'KittipatDechkul'

def main():
    hangman_input = input("")
    hangman = hangman_input.split(" ")
    result = ['_'] * 12
    wrong , pos = list() , list()
    score = 0
    print(*result, sep=" ")
    for i in range(5):
        ans = input("")
        for j in range(len(hangman)):
            if hangman[j] == ans:
                pos.append(j)
        if pos != []:
            for k in range(len(pos)):
                result[pos[k]] = ans
                score += 1
        else:
            wrong.append(ans)
        print(*result, *wrong)
        pos.clear()
    print(score)
if __name__ == '__main__':
    main()