while True:
    value = int(input('GIVE VALUE BETWEEN 0 TO 999: '))
    ones_place = {0: '', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'Eighteen', 19: 'Nineteen'}
    tens_place = {0: '', 2: 'TWENTY', 3: 'THIRTY', 4: 'FORTY', 5: 'FIFTY', 6: 'SIXTY', 7: 'SEVENTY', 8: 'EIGHTY', 9: 'NINETY'}

    if value == 0:
        print('ZERO')

    elif value <= 19 and (value > 0):
        print(ones_place[value])

    elif (value < 100) and (value >= 20):
        tens_value = (value//10)
        val_one = (value % 10)
        print(tens_place[tens_value] + ' ' + ones_place[val_one])

    elif (value < 1000) and (value >= 100):
        hundred_value = value//100
        tens_val = value-(100*hundred_value)
        val_ten = tens_val//10
        val_one = value % 10
        print(ones_place[hundred_value], 'HUNDRED', tens_place[val_ten], ones_place[val_one])