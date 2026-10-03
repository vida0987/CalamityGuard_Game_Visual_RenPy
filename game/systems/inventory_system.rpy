init python:
    def add_item(item):
        if item not in renpy.store.inventory:
            renpy.store.inventory.append(item)

    def has_item(item):
        return item in renpy.store.inventory

    def remove_item(item):
        if item in renpy.store.inventory:
            renpy.store.inventory.remove(item)
