label deep_forest_2:

    $ current_area = "Deep Forest II"

    scene bg deep_forest_bg

    "[loc('location.deep_forest_2.description.1')]"
    "[loc('location.deep_forest_2.description.2')]"

    jump deep_forest_2_menu

label deep_forest_2_menu:
    scene bg deep_forest_bg

    menu:

        "[loc('location.deep_forest_2.option.go_forward')]":

            call spend_time(1) from _call_spend_time_7
            if deep_forest_2_monsters_killed < 3:
                "[loc('location.deep_forest_2.result.go_forward_1')]"
                "[loc('location.deep_forest_2.result.go_forward_2')]"

                call combat(
                    loc("character.forest_monster"),
                    2,
                    1,
                    "images/monster/tree_monster_A.png",
                    False
                ) from _call_combat_5

                if _return == "victory":

                    $ deep_forest_2_monsters_killed += 1

                jump deep_forest_2_menu
            else:
                if not deep_forest_2_npc_met:
                    $ deep_forest_2_npc_met = True
                    call cultist from _call_cultist

                jump deep_forest_2_menu

        "[loc('location.deep_forest_2.option.return')]":

            call spend_time(1) from _call_spend_time_8

            "[loc('location.deep_forest_2.result.return_1')]"

            jump forest_edge