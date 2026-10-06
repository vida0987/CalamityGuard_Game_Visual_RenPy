label church:

    $ current_area = "Church"

    scene bg chruch_bg

    "[loc('location.church.description.1')]"
    "[loc('location.church.description.2')]"
    "[loc('location.church.description.3')]"

    jump church_menu

label church_menu:
    scene bg chruch_bg

    menu:

        "[loc('location.church.option.use_main_entrance')]" if not church_monster_dead:

            call encounter_church_monster from _call_encounter_church_monster

            if _return == "victory":

                $ church_monster_dead = True

            jump church_menu

        "[loc('location.church.option.look_window')]" if not church_monster_dead:

            call spend_time(1) from _call_spend_time

            "[loc('location.church.result.window_result_1')]"
            "[loc('location.church.result.window_result_2')]"
            "[loc('location.church.result.window_result_3')]"

            call encounter_church_monster from _call_encounter_church_monster_1

            if _return == "victory":

                $ church_monster_dead = True

            jump church_menu

        "[loc('location.church.option.examine_rear_path')]" if not graveyard_unlocked:

            $ graveyard_unlocked = True

            call spend_time(1) from _call_spend_time_1

            "[loc('location.church.result.rear_path_result_1')]"
            "[loc('location.church.result.rear_path_result_2')]"

            jump graveyard

        "[loc('location.church.option.search_interior')]" if church_monster_dead:

            jump church_inside

        "[loc('location.church.option.enter_graveyard')]" if graveyard_unlocked:

            jump graveyard

        "[loc('travel.travel')]":

            jump travel

label church_inside:

    $ current_area = "Church"

    scene bg chruch_2_bg

    "[loc('location.church.description.interior_description.1')]"
    "[loc('location.church.description.interior_description.2')]"
    "[loc('location.church.description.interior_description.3')]"

    jump church_inside_menu

label church_inside_menu:
    scene bg chruch_2_bg

    menu:

        "[loc('location.church.option.search_holy_symbol')]" if not has_item("holy_badge"):

            $ add_item("holy_badge")

            call spend_time(1) from _call_spend_time_2

            "[loc('location.church.result.badge_result')]"

            jump church_inside_menu

        "[loc('location.church.option.search_confession')]":

            call spend_time(1) from _call_spend_time_3

            call encounter_priest from _call_encounter_priest

            jump church_inside_menu

        "[loc('location.church.option.open_graveyard_exit')]":

            $ graveyard_unlocked = True

            call spend_time(1) from _call_spend_time_4

            "[loc('location.church.result.exit_result')]"

            jump church_inside_menu

        "[loc('location.church.option.enter_graveyard')]" if graveyard_unlocked:

            jump graveyard

        "[loc('travel.travel')]":

            jump travel
