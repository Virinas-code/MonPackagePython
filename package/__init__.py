#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UN TRUC TROP COOL!"""
# Bla bla de license
# Bla bla


class HelloWorld:
    """Un truc pour afficher Hello World!."""

    def __init__(self, greeting: str = "World") -> None:
        """
        Initialise le Hello World!.

        :param str greeting: La personne à saluer.
        """
        self.greeting: str = "Hello " + greeting + "!"
        """Phrase pour saluer."""

    def get_greeting(self) -> str:
        """
        Obtient la phrase à dire.

        Vous pouvez aussi utiliser :obj:`package.HelloWorld.greeting`.

        :return: La phrase à dire.
        :rtype: str
        """
        return self.greeting

    def greet(self) -> None:
        """Dire la phrase :D"""
        print(self.greeting)


def nul() -> None:
    """
    RIEN DU TOUT.

    :return: RIEN.
    :rtype: None
    """
    return None


if __name__ == "__main__":
    greeter: HelloWorld = HelloWorld("someone")
    greeter.greet()
