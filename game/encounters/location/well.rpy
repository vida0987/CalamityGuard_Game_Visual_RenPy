label well:

    $ current_area = "Well"

    scene bg well_bg

    "[loc('location.well.description.1')]"
    "[loc('location.well.description.2')]"

    jump well_menu

label well_menu:
    scene bg well_bg

    menu:

        "[loc('location.well.option.pull_bucket')]" if not seal_material_a:

            $ seal_material_a = True
            $ add_item("seal_material_a")

            call spend_time(1) from _call_spend_time_43

            "[loc('location.well.result.fragment_result_1')]"
            "[loc('location.well.result.fragment_result_2')]"
            "[loc('location.well.result.fragment_result_3')]"

            jump well_menu

        "[loc('location.well.option.search_well')]":

            $ add_item("talisman")

            call spend_time(1) from _call_spend_time_44

            "[loc('location.well.result.symbol_result_1')]"
            "[loc('location.well.result.symbol_result_2')]"
            "[loc('location.well.result.symbol_result_3')]"

            jump well_menu

        "[loc('location.well.option.examine_shaft')]" if not sewer_unlocked:

            $ sewer_unlocked = True

            call spend_time(1) from _call_spend_time_45

            "[loc('location.well.result.sewer_result_1')]"
            "[loc('location.well.result.sewer_result_2')]"
            "[loc('location.well.result.sewer_result_3')]"
            "[loc('location.well.result.sewer_result_4')]"

            jump well_menu

        "[loc('location.well.option.enter_sewer')]" if sewer_unlocked:

            jump sewer

        "[loc('travel.travel')]":

            jump travel