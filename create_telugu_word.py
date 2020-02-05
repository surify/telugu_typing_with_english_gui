#!/usr/bin/env python3

from mapping import vowels_mapping, consonants_mapping, sounds_mapping,\
                    silent, consonants, vowels, specials

def createTeluguWord(syllables):
    """Takes a list of telugu syllables written in english script
    and returns telugu word.
    """
    telugu_word = ''
    # the below for loop loops 1 time for each syllable in the word
    for each in syllables:
        # if syllable starts with a vowel(this can only be case with first syllable,
        # as no other syllable in the word can start with a vowel
        if each[0] in vowels:
            # for example 'a' or 'aa'
            if len(each) == 1:
                telugu_word += vowels_mapping[each][0]
            elif len(each) == 2:
                if each[0] in vowels and each[1] in specials:
                    telugu_word += (vowels_mapping[each[0]][0] + vowels_mapping[each[1]][0])
                elif each[0] in vowels and each[1] in vowels:
                    telugu_word += vowels_mapping[each[0:]][0]
            # for example 'aam' or 'aan'
            elif len(each) == 3:
                telugu_word += (vowels_mapping[each[:2]][0] + vowels_mapping[each[2]][0])
        # if the syllable starts with a consonant(including m and n)
        else:
            if len(each) == 1:
                telugu_word += (consonants_mapping[each[0]][0] + silent)
            else:
                # if the syllable's length is > 1
                i = 0
                while i < (len(each) - 1):
                    if each[i] not in vowels:
                        if each[i+1] not in vowels:
                            if each[i+1] == 'h':
                                telugu_word += consonants_mapping[each[i : i + 2]][0]
                                i += 2
                            else:
                                telugu_word += (consonants_mapping[each[i]][0] + silent)
                                i += 1
                        else:
                            if each[i-1] not in vowels:
                                telugu_word += (silent + consonants_mapping[each[i]][0])
                            else:
                                telugu_word += consonants_mapping[each[i]][0]
                            i += 1
                    else:
                        break
                each = each[i : ]
                if len(each) == 1:
                    if each[0] not in vowels:
                        telugu_word += (silent + consonants_mapping[each[0]][0])
                    else:
                        telugu_word += sounds_mapping[each[0]][0]
                elif len(each) > 1:
                    if len(each) == 3:
                        print(each)
                        telugu_word += (sounds_mapping[each[0 : 2]][0] + sounds_mapping[each[2]])
                    elif each[0] in vowels and each[1] in vowels:
                        telugu_word += sounds_mapping[each][0]
                    elif each[0] in vowels and each[1] in specials:
                        telugu_word += (sounds_mapping[each[0]][0] + sounds_mapping[each[1]])
                else:
                    print("new kind of mapping")
    return telugu_word
