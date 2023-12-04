class Computer:
    def __init__(self, type, brand, processor, memory):
        self.type = type
        self.brand = brand
        self.processor = processor
        self.memory = memory
        self.available = True

    def get_type(self):
        return self.type

    def get_brand(self):
        return self.brand

    def get_processor(self):
        return self.processor

    def get_memory(self):
        return self.memory

    def is_available(self):
        return self.available

    def set_available(self, available):
        self.available = available
