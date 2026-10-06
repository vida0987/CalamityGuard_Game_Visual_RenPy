label village_gate:

    $ current_area = "Village Gate"

    scene bg village_gate_bg

    "[loc('location.village_gate.description')]"

    jump village_gate_menu

label village_gate_menu:
    scene bg village_gate_bg

    menu:

        "[loc('location.village_gate.option.examine_gate')]":

            call spend_time(1) from _call_spend_time_30 

            "[loc('location.village_gate.result.gate_result')]"

            jump village_gate_menu

        "[loc('location.village_gate.option.examine_tree')]":

            call spend_time(1) from _call_spend_time_39 

            "[loc('location.village_gate.result.tree_result_1')]"

            "[loc('location.village_gate.result.tree_result_2')]"

            jump village_gate_menu

        "[loc('location.village_gate.option.examine_stone')]":

            call spend_time(1) from _call_spend_time_40

            "[loc('location.village_gate.result.stone_result')]"

            jump village_gate_menu

        "[loc('location.village_gate.option.look_sky')]":

            call spend_time(1) from _call_spend_time_41

            "[loc('location.village_gate.result.sky_result')]"

            jump village_gate_menu

        "[loc('location.village_gate.option.read_note')]" if not note_read:

            $ note_read = True

            call spend_time(1) from _call_spend_time_42

            "[loc('location.village_gate.result.note_result_1')]"

            "[loc('location.village_gate.result.note_result_2')]"

            "[loc('location.village_gate.result.note_result_3')]"

            jump village_gate_menu

        "[loc('location.village_gate.option.leave')]":

            jump normal_ending

        "[loc('travel.travel')]":

            jump travel