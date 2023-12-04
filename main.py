from computer_manager import ComputerManager
from user_manager import UserManager
from transaction_manager import TransactionManager

def main():
    # Initialize computer, user, and transaction managers
    computer_manager = ComputerManager()
    user_manager = UserManager()
    transaction_manager = TransactionManager(computer_manager, user_manager)

    # Add computers
    computer_manager.add_computer("Desktop", "Dell", "Core i5", 8)
    computer_manager.add_computer("Laptop", "HP", "Core i7", 16)

    # Display available computers
    computer_manager.display_computers()

    # Create users
    user1 = user_manager.create_user("Alice")
    user2 = user_manager.create_user("Bob")

    # Display users
    user_manager.display_users()

    # Users perform transactions
    transaction_manager.borrow_computer(user1, computer_manager.get_computer_by_index(0))
    transaction_manager.borrow_computer(user2, computer_manager.get_computer_by_index(1))

    # Display transaction details
    transaction_manager.display_transactions()

    # Users return computers
    transaction_manager.return_computer(user1, computer_manager.get_computer_by_index(0))
    transaction_manager.return_computer(user2, computer_manager.get_computer_by_index(1))

    # Display available computers after returns
    computer_manager.display_computers()

if __name__ == "__main__":
    main()
