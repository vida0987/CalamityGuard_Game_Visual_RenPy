label graveyard:
    $ current_area = "Graveyard"
    scene bg graveyard_bg
    "[loc('location.graveyard.description')]"
    if grave_7 and grave_6 and grave_2:
        "[loc('location.graveyard.result.final_grave')]"
        jump boss
    menu:
        "[loc('location.graveyard.option.grave_1')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_12
            jump graveyard
        "[loc('location.graveyard.option.grave_2')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_13
            jump grave_two
        "[loc('location.graveyard.option.grave_3')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_14
            call encounter_grave_monster from _call_encounter_grave_monster_1
            jump graveyard
        "[loc('location.graveyard.option.grave_4')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_15
            jump boss
        "[loc('location.graveyard.option.grave_5')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_16
            jump graveyard
        "[loc('location.graveyard.option.grave_6')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_17
            jump grave_six
        "[loc('location.graveyard.option.grave_7')]":
            if not has_item("shovel"):
                    call spend_time(1) from _call_spend_time_18
            jump grave_seven
        "[loc('location.graveyard.option.return_church')]":
            jump church
        "[loc('travel.travel')]":
            jump travel

label grave_two: 
    if not grave_2:
        "[loc('location.graveyard.result.grave_two_description')]"
        menu:
            "[loc('location.graveyard.option.place_green')]" if seal_material_b:
                $ seal_material_b = False
                $ remove_item("seal_material_b")
                $ grave_2 = True
                "[loc('location.graveyard.result.seal_closes')]"
            "[loc('location.graveyard.option.leave')]":
                jump graveyard
    else:
        "[loc('location.graveyard.result.grave_fine')]"
    call check_seal from _call_check_seal
    jump graveyard

label grave_six:
    if not grave_6:
        "[loc('location.graveyard.result.grave_six_description')]"
        menu:
            "[loc('location.graveyard.option.place_blue')]" if seal_material_a:
                $ seal_material_a = False
                $ remove_item("seal_material_a")
                $ grave_6 = True
                "[loc('location.graveyard.result.seal_closes')]"
            "[loc('location.graveyard.option.leave')]":
                jump graveyard
    else:
        "[loc('location.graveyard.result.grave_fine')]"
    call check_seal from _call_check_seal_1
    jump graveyard

label grave_seven:
    if not grave_7:
        "[loc('location.graveyard.result.grave_seven_description')]"
        menu:
            "[loc('location.graveyard.option.place_ritual')]" if seal_material_c:
                $ seal_material_c = False
                $ remove_item("seal_material_c")
                $ grave_7 = True
                "[loc('location.graveyard.result.seal_closes')]"
            "[loc('location.graveyard.option.leave')]":
                jump graveyard
    else:
        "[loc('location.graveyard.result.grave_fine')]"
    call check_seal from _call_check_seal_2
    jump graveyard

