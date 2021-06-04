from dataclasses import dataclass

from wired.dataclasses import factory


@factory()
@dataclass
class Greeter:
    name: str = 'Copol'

    def __call__(self, customer: str) -> str:
        msg = 'Hello {customer}! And welcome, hoping you enjoy your stay. My name is {name}, how are you?'
        return msg.format(customer=customer, name=self.name)
