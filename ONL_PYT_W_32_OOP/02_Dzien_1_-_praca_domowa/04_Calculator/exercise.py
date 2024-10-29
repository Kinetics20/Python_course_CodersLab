class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self._log_operation(a, b, '+', result)
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        self._log_operation(a, b, '-', result)
        return result

    def mul(self, a, b):
        result = super().mul(a, b)
        self._log_operation(a, b, '*', result)
        return result

    def div(self, a, b):
        result = super().div(a, b)
        self._log_operation(a, b, '/', result)
        return result

    def _log_operation(self, a, b, operation, result):
        operation_str = f'{a} {operation} {b} = {result}'
        self.history.append(operation_str)


logger_calculator = LoggingCalculator()

result_add = logger_calculator.add(50, 13)
result_sub = logger_calculator.sub(120, 46)
result_mul = logger_calculator.mul(25, 87)
result_div = logger_calculator.div(18, 52)

print("History:")
for entry in logger_calculator.history:
    print(entry)