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
    print(f'Ваш остаток на счете составляет: {saving.get_balance(): ,.2f} руб.')


if __name__ == '__main__':
    main()
