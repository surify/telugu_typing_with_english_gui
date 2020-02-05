#!/usr/bin/env python3


from mapping import consonants, vowels, specials
from create_telugu_word import createTeluguWord


def separateSyllables(word):
    """This function takes a telugu word written in english script and breaks
    it into parts where each part forms a single telugu letter(syllable).

    It does the breaking by comparing various conditions below where each
    condition is explained with an example.
    """
    global vowels, consonants, specials
    syllables = []
    word = list(word)
    starts_with_consonant = False
    while word:
        # syllable begins with a vowel
        if word[0] in vowels:
            # if only one character remains in the word
            if len(word) == 1:
                syllable_end = 1
            # if two characters remain in the word
            elif len(word) == 2:
                # for example a|b
                if (word[1] in consonants) or (word[1] == 'n'):
                    syllable_end = 1
                # for example a|a or a|m
                elif ((word[1] in vowels) or
                      (word[1] == 'm')):
                    syllable_end = 2
            # if more than two characters remain in the word
            else:
                # for example a|ma or a|mma or a|kka
                if ((word[1] in specials and word[2] in vowels) or
                    (word[1] == word[2] and word[1] in specials) or
                    (word[1] in consonants)):
                    syllable_end = 1
                # for example an|ji or aa|ku or aa|me
                elif ((word[1] in specials and word[2] in consonants) or
                     (word[1] in vowels and word[2] not in specials) or
                     (len(word) > 3 and word[1] in vowels and
                      word[2] in specials and word[3] in vowels)):
                    syllable_end = 2
                # for example aam|botu
                elif ((word[1] in vowels and word[2] in specials)):
                    print("syllable")
                    syllable_end = 3
            # if the syllable had started with a consonant we will add the vowel part to the
            # last item in the syllables list as the consonant part is already appended to
            # the syllables list
            if starts_with_consonant:
                syllables[-1] += (''.join(word[0 : syllable_end]))
                starts_with_consonant = False
            # if the syllable had started with a vowel(the first syllable in the word)
            # we will append the syllable to the syllables list
            else:
                syllables.append(''.join(word[0 : syllable_end]))
            del word[0 : syllable_end]
        # if syllable begins with a consonant, we will take the consonant part of the syllable
        # and add it to the syllables list and now the second part of the syllable now start with
        # a vowel and it will pass through the if elif elif elif condition and the vowel part will
        # be appended to the consonant part.
        else:
            starts_with_consonant = True
            temp = ''
            vowel_break = False
            for i in range(len(word)):
                if word[i] not in vowels:
                    temp += word[i]
                else:
                    vowel_break = True
                    break
            syllables.append(temp)
            if vowel_break:
                del word[ : i]
            else:
                del word[ : i + 1]
    print(syllables)
    return syllables


if __name__ == '__main__':
    while True:
        word = input("Enter a word: ")
        if word:
            syllables = separateSyllables(word)
            print(syllables)
            print(createTeluguWord(syllables))
        else:
            # pressing Enter without entering a word exits the program
            break
