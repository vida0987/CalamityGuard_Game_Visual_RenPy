screen game_layout():
    # The transparent middle leaves the scene, dialogue, and choices visible.
    zorder 10

    fixed:
        xfill True
        yfill True

        frame:
            xalign 0.0
            xsize 240
            yfill True
            background Solid("#15110ee6")
            padding (24, 32)
            use character_panel 

        frame:
            xalign 1.0
            xsize 240
            yfill True
            background Solid("#15110ee6")
            padding (24, 32)
            use inventory_panel
