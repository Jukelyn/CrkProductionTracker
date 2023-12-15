from item import Item

import tkinter
import customtkinter

items = []


def main():
    ...


def add_item(name: str, productionTime: int) -> None:
    for item in items:
        if item.name == name:
            raise ValueError(
                "Item already added. Perhaps you meant to edit the item instead?"
            )

    item = Item(name, productionTime)
    items.append(item)


def remove_item(name: str) -> None:
    global items

    new_items = [item for item in items if name != item.name]

    if len(new_items) == len(items):
        raise ValueError("The item you are trying to remove is not in the list.")

    items = new_items


if __name__ == "__main__":
    main()
