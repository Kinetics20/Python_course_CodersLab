class Price23Vat:
    def __init__(self, pretax):
        self.set_pretax(pretax)

    def get_net(self):
        return self._net

    def get_pretax(self):
        return self._pretax

    def get_tax(self):
        return self._tax

    def set_net(self, value):
        self._net = value
        self._pretax = value * 1.23
        self._tax = self._pretax - self._net

    def set_pretax(self, value):
        self._pretax = value
        self._net = value / 1.23
        self._tax = self._pretax - self._net

    def set_tax(self, value):
        self._tax = value
        self._pretax = self._net + self._tax
        self._net = self._pretax / 1.23
