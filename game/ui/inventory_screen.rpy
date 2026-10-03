screen inventory_panel():
    vbox:
        xfill True
        spacing 18
        text "[loc('ui.inventory')]" xalign 0.5
        text "[loc('ui.items', count=len(inventory))]" xalign 0.5

        if inventory:
            for item in inventory:
                text "- [item_label(item)]"
        else:
            text "[loc('ui.empty')]" xalign 0.5

# Kept as an alias for any future modal inventory use.
screen inventory_screen():
    use inventory_panel
