class Customer:
    def __init__(self, first_name, last_name, ni_number):
        self._first_name = first_name
        self._last_name = last_name
        self._ni_number = ni_number

    def __eq__(self, other):
        return self._first_name == other._first_name and self._last_name == other._last_name and self._ni_number == other._ni_number

    def __hash__(self):
        return hash((self._first_name, self._last_name))


if __name__ == '__main__':
    first_customer = Customer('Helen', 'Vu')
    second_customer = Customer('Helen', 'Vu')
    print(first_customer == second_customer)
    print(first_customer.__eq__(second_customer)) # Equivalent to the line above

    print(hash(first_customer))
    print(hash(second_customer))
