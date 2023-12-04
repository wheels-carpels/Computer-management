from computer import Computer

class ComputerManager:
    def __init__(self):
        self.computers = []

    def add_computer(self, type, brand, processor, memory):
        computer = Computer(type, brand, processor, memory)
        self.computers.append(computer)

    def display_computers(self):
        print("Available Computers:")
        for index, computer in enumerate(self.computers):
            availability = "Available" if computer.is_available() else "Borrowed"
            print(f"{index + 1}. {computer.get_type()} - {computer.get_brand()} - {computer.get_processor()} - {computer.get_memory()}GB - {availability}")
        print()

    def get_computer_by_index(self, index):
        return self.computers[index]
