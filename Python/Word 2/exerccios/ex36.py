# Function to calculate loan eligibility
def calculate_loan_eligibility(name, salary, house_value, pay_years):
    # Calculate the monthly installment
    monthly_installment = house_value / (pay_years * 12)
    monthly_installment = round(monthly_installment, 2)

    # Calculate 30% of the borrower's salary
    max_affordable_payment = (30 * salary) / 100
    max_affordable_payment = round(max_affordable_payment, 2)

    # Check loan eligibility
    if monthly_installment <= max_affordable_payment:
        print(f'EMPRÉSTIMO CONFIRMADO, {name.upper()}!!!')
        print('-=-' * 20)
        print(f'Valor da Casa: R${house_value}')
        print(f'Tempo de Empréstimo: {pay_years} anos')
        print(f'Valor da Parcela Mensal: R${monthly_installment}')
        print('-=-' * 20)
        print('Tenha um ótimo dia!!!')
    else:
        print('-=-' * 20)
        print(f'EMPRÉSTIMO RECUSADO, {name.upper()}!!!')
        print('-=-' * 20)
        print('Tenha um ótimo dia!!!')


# Main program
if __name__ == "__main__":
    # Gather user input
    name = input('Qual é o nome da pessoa que deseja fazer o empréstimo?: ')
    salary = float(input('Qual é o salário de quem deseja o empréstimo?: R$'))
    house_value = float(input('Qual é o valor da casa?: R$'))
    pay_years = float(input('Em quantos anos você deseja pagar?: '))

    # Call the function to determine eligibility
    calculate_loan_eligibility(name, salary, house_value, pay_years)
