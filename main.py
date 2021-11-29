from banking.bank import Bank
from banking.controller import BankController
from banking.commands import Deposit, Withdrawal, Transfer, Batch

def main() -> None:

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account("LidiaBaciu")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    controller.execute(Deposit(account1, 100000))
    
    controller.execute(Batch(
        commands=[
            Deposit(account2, 100000), 
            Deposit(account3, 100000), 
            Withdrawal(account3, 1000000000),
            Transfer(from_account=account2, to_account=account1, amount=50000)
            ]
        )
    )
    
    # controller.undo()
    
    # controller.execute(Withdrawal(account1, 150000))
    # controller.undo()
    
    print(bank)


if __name__ == "__main__":
    main()