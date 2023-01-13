
def minion_game(string):
    # # your code goes here
    # stuart_consonants = set()
    # kevin_vowels = set()
    # kevin_score = 0
    # stuart_score = 0
    # for i in range(1,len(string)+1):
    #     for j in range(len(string)):
    #         sub = string[j::i]
    #         #print(sub)
    #         if sub[0] in vowels:
    #             kevin_vowels.add(sub)
    #         else:
    #             stuart_consonants.add(sub)
    # for i in string:
    #     for j in kevin_vowels:
    #         if j in string:
    #             print(i)
    #             kevin_score +=1
    #     for j in stuart_consonants:
    #         if j in string:
    #             stuart_score +=1
    # print('vogais', kevin_vowels, kevin_score)
    # print('cons', stuart_consonants, stuart_score)
    alphabet = [chr(i) for i in range(65, 65+26)]
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = list(filter(lambda elmnt: not elmnt in vowels, alphabet))

    def count(s, li):
        result = 0
        for i in range(len(s)):
            if s[i] in li:
                result += len(s[i:])
                print(s[i:])
        return result

    score = {}
    score['Stuart'] = count(string, consonants)
    score['Kevin'] = count(string, vowels)


    if score['Stuart'] == score['Kevin']:
        print('Draw')
    else:
        print(f"Stuart {score['Stuart']}" if score['Stuart'] > score['Kevin'] else f"Kevin {score['Kevin']}")


if __name__ == '__main__':
    s = 'BANANA'#input()
    minion_game(s)