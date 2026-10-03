label deep_forest:
    jump deep_forest_1

label deep_forest_1:
    $ current_area = "Deep Forest I"
    scene bg deep_forest_bg
    "[loc('location.deep_forest_1.description.1')]"
    "[loc('location.deep_forest_1.description.2')]"
    "[loc('location.deep_forest_1.description.3')]"

    if not forest_monster_dead:
        call combat(loc("character.forest_monster"), 2, 1, "images/monster/tree_monster_A.png", False) from _call_combat_deep_forest_1
        $ forest_monster_dead = True

    jump deep_forest_1_after_battle

label deep_forest_1_after_battle:
    scene bg deep_forest_2_bg
    "[loc('location.deep_forest_1.description.after_battle.1')]"
    "[loc('location.deep_forest_1.description.after_battle.2')]"

    menu:
        "[loc('location.deep_forest_1.option.inspect_body')]":
            call spend_time(1) from _call_spend_time_5
            "[loc('location.deep_forest_1.result.inspect_body.1')]"
            "[loc('location.deep_forest_1.result.inspect_body.2')]"
            "[loc('location.deep_forest_1.result.inspect_body.3')]"
            "[loc('location.deep_forest_1.result.inspect_body.4')]"
            "[loc('location.deep_forest_1.result.inspect_body.5')]"
            "[loc('location.deep_forest_1.result.inspect_body.6')]"
            "[loc('location.deep_forest_1.result.inspect_body.7')]"
            "[loc('location.deep_forest_1.result.inspect_body.8')]"
            "[loc('location.deep_forest_1.result.inspect_body.9')]"
            jump deep_forest_1_after_battle
        "[loc('location.deep_forest_1.option.tear_body')]" if not seal_material_c:
            call spend_time(1) from _call_spend_time_6
            "[loc('location.deep_forest_1.result.tear_body.1')]"
            "[loc('location.deep_forest_1.result.tear_body.2')]"
            "[loc('location.deep_forest_1.result.tear_body.3')]"
            "[loc('location.deep_forest_1.result.tear_body.4')]"
            $ seal_material_c = True
            $ add_item("seal_material_c")
            jump deep_forest_1_after_battle
        "[loc('location.deep_forest_1.option.back')]":
            jump travel