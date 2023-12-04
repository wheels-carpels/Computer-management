from transaction import Transaction

class TransactionManager:
    def __init__(self, computer_manager, user_manager):
        self.computer_manager = computer_manager
        self.user_manager = user_manager
        self.transactions = []

    def borrow_computer(self, user, computer):
        transaction = Transaction(user, computer)
        computer_index = self.computer_manager.computers.index(computer)
        if self.computer_manager.computers[computer_index].is_available():
            self.computer_manager.computers[computer_index].set_available(False)
            self.transactions.append(transaction)
        else:
            print("Computer not available for borrowing.")

    def return_computer(self, user, computer):
        computer_index = self.computer_manager.computers.index(computer)
        if not self.computer_manager.computers[computer_index].is_available():
            self.computer_manager.computers[computer_index].set_available(True)
            for transaction in self.transactions:
                if transaction.get_user() == user and transaction.get_computer() == computer:
                    self.transactions.remove(transaction)
                    break

    def display_transactions(self):
        print("Transaction Details:")
        for transaction in self.transactions:
            print(f"User: {transaction.get_user().get_name()}, Computer: {transaction.get_computer().get_type()} - {transaction.get_computer().get_brand()} - {transaction.get_computer().get_processor()} - {transaction.get_computer().get_memory()}GB")
        print()
