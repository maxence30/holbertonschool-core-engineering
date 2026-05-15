#!/usr/bin/env python3
"""
Module verboselist

Defines a VerboseList class that extends the built-in
list class with notification messages.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications
    when items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend the list with multiple items and print
        a notification.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print
        a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item from the list
        and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
    