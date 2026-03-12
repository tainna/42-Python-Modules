from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if type(data) is not list or len(data) == 0:
            return False
        for item in data:
            if type(item) is not int and type(item) is not (float):
                return False

        return True

    def process(self, data: Any) -> str:

        try:
            d_size = len(data)
            d_sum = sum(data)
            d_med = d_sum / d_size

            return (
                f"Processed {d_size} numeric values, "
                f"sum={d_sum}, avg={d_med:.1f}"
            )
        except ValueError as error:
            return (f"Error processing numeric data: {error}")


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is not str or len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:

        try:
            len_d = len(data)
            word_count = 0
            in_word = False
            for char in data:
                if char == ' ' or char == '\n' or char == '\t':
                    in_word = False
                elif not in_word:
                    word_count += 1
                    in_word = True
            return (f"Processed text: {len_d} characters, {word_count} words")
        except ValueError as error:
            return (f"Error processing data: {error}")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is not str or len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            idx = 0
            for i in range(len(data)):
                if data[i] == ":":
                    idx = i
            if idx == 0:
                return f"Invalid log formay: {data}"
            level = data[:idx]
            message = data[idx+2:]

            if level == "ERROR":
                prefix = "[ALERT]"
            else:
                prefix = f"[{level}]"
            return f"{prefix} {level} level detected: {message}"
        except Exception as error:
            return f"Error processing log data: {error}"


if __name__ == "__main__":
    print("== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    """Numeric Processor"""
    num_proc = NumericProcessor()
    data_n = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data_n}")

    if num_proc.validate(data_n):
        print("Validation: Numeric data verified")
        result_n = num_proc.process(data_n)
        print(num_proc.format_output(result_n))

    """Text Processor"""
    text_proc = TextProcessor()
    data_t = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(f"Processing data: {data_t}")

    if text_proc.validate(data_t):
        print("Validation: Text data verified")
        result_t = text_proc.process(data_t)
        print(text_proc.format_output(result_t))

    """Log Processor"""
    log_proc = LogProcessor()
    data_l = "RROR: Connection timeout"
    print("\nInitializing Log Processor...")
    print(f"Processing data: {data_l}")

    if log_proc.validate(data_l):
        print("Validation: Log entry verified")
        result_l = log_proc.process(data_l)
        print(log_proc.format_output(result_l))

    print("\n=== Polymorphic Processing Demo ===")

    """ All toguether"""
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data = [
        [1, 2, 3],
        "Hello Nexus World",
        "INFO: System ready"
    ]

    print("Processing multiple data types through same interface...")

    for i in range(3):
        proc = processors[i]
        dado = test_data[i]

        if proc.validate(dado):
            resultado = proc.process(dado)
            print(f"Result {i + 1}: {resultado}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
