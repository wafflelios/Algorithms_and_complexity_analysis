def main():
    orc_growth = input().split()
    supposed_growth = input().split()
    dictionary = {}
    for counter in range(0, len(orc_growth) - 1):
        if orc_growth[counter] != orc_growth[counter + 1]:
            counter_L = orc_growth[:counter + 1].count(orc_growth[counter])
            counter_R = len(orc_growth[counter:]) - orc_growth[counter:].count(orc_growth[counter])
            multy = counter_L * counter_R
            if (orc_growth[counter] not in dictionary.keys()) or (dictionary[orc_growth[counter]] < multy):
                dictionary[orc_growth[counter]] = multy
    for grow in supposed_growth:
        if grow not in dictionary.keys():
            print(0, end=' ')
        else:
            print(dictionary[grow], end=' ')


main()
