init python:
    def item_label(item):
        return loc("item." + item) if item in inventory_item_keys() else item

    def inventory_item_keys():
        return (
            "knife",
            "mental_charm",
            "light_charm",
            "holy_badge",
            "seal_material_a",
            "seal_material_b",
            "seal_material_c",
        )
