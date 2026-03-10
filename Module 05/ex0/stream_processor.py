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

        if not type(data) is not str or len(data) == 0:
            return False
        for item in data:
            if type(item) is not (int) or type(data) is not (float):
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

    def validate(self, data) -> bool:
        if type(data) is not dict or len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            idx = 0
            for i in range(len(data)):
                if data[i] == ":":
                    idx = i
                break
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
