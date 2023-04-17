import bankaccount


def main():

    # Получить начальный остаток
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount
    saving = bankaccount.BankAccount(start_bal)

    # Внести на счет зарплату пользователя
    pay = float(input('Сколько вы получили на этой неделе? '))
    print('Вношу эту сумму на ваш счет.')
    saving.deposit(pay)

    # Показать остаток.
    print(saving)

    # Выдать деньги со счета пользователя
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с вашего счета.')
    saving.withdraw(cash)

    print(saving)


if __name__ == '__main__':
    main()
