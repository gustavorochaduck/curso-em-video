name = str(input('Type your name(Up to 10 words): '))

if len(name) <= 10:
    def quantidade_de_letras():
        separator = len(name)
        print(f'Quantity of leters is: {separator}')

    def upper_case():
        print(f'Upper Case: {name.upper()}')

    def upper_case_value():
        first_letter_upper_case_value = name[0]
        print(f'The first latter is upper case?: {first_letter_upper_case_value.isupper()}')

    quantidade_de_letras()
    upper_case_value()
    upper_case()

else:
    print('ERROR!!!')
    print('Exceeded 10 Word!!!')
