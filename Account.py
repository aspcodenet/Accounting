from enum import Enum 

class WithdrawalResult(Enum):
    Ok = 1
    NotEnoughSaldo = 2
    Max4000krPerDay = 3    

class Account:
    def __init__(self, kontonummer:str):
        self._kontonummer = kontonummer
        self._saldo = 0

    def getSaldo(self) -> int:
        return self._saldo
    
    def withdraw(self, amount:int) -> WithdrawalResult:
        if amount > 4000:
            return WithdrawalResult.Max4000krPerDay

        if self._saldo < amount:
            return WithdrawalResult.NotEnoughSaldo

        self._saldo = self._saldo - amount
        return WithdrawalResult.Ok
