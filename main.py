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

    controller.register(Deposit(account1, 100000))
    
    controller.register(Batch(
        commands=[
            Deposit(account2, 100000), 
            Deposit(account3, 100000), 
            Transfer(from_account=account2, to_account=account1, amount=50000)
            ]
        )
    )
    
    bank.clear_cache()
    controller.compute_balances()
    print(bank)


if __name__ == "__main__":
    main()