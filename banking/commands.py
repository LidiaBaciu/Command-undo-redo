from dataclasses import dataclass
from banking.account import Account

@dataclass
class Deposit:
    account: Account
    amount: int
    
    @property
    def transaction_details(self) -> str:
        return f"${self.amount / 100:.2f} to acount {self.account.name}"
    
    def execute(self) -> None:
        self.account.deposit(self.amount)
        print(f"Deposited {self.transaction_details}")
        
    def undo(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Undid deposit of {self.transaction_details}")
    
    def redo(self) -> None:
        self.account.deposit(self.amount)
        print(f"Redid deposit of {self.transaction_details}")
    
@dataclass
class Withdrawal:
    account: Account
    amount: int
    
    @property
    def transaction_details(self) -> str:
        return f"${self.amount / 100:.2f} to acount {self.account.name}"
    
    def execute(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Withdrawn {self.transaction_details}")
       
    def undo(self) -> None:
        self.account.deposit(self.amount)
        print(f"Undid deposit of {self.transaction_details}")
    
    def redo(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Redid deposit of {self.transaction_details}")
       
@dataclass 
class Transfer:
    from_account: Account
    to_account: Account
    amount: int
    
    @property
    def transaction_details(self) -> str:
        return f"{self.amount/100:.2f} from account {self.from_account.name} to account {self.to_account}."
    
    def execute(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Transfered {self.transaction_details}")
        
    def undo(self) -> None:
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)
        print(f"Undid transfer of {self.transaction_details}")
    
    def redo(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Redid transfer of {self.transaction_details}")