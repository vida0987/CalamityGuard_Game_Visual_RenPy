label sewer:

    $ current_area = "Underground Sewer"

    scene bg sewer_bg

    "[loc('location.sewer.description.1')]"
    "[loc('location.sewer.description.2')]"
    "[loc('location.sewer.description.3')]"

    menu:

        "[loc('location.sewer.option.inspect_gold')]":

            $ gold_found = True
            $ add_item("gold")

            call spend_time(1) from _call_spend_time_27

            "[loc('location.sewer.result.gold_result_1')]"
            "[loc('location.sewer.result.gold_result_2')]"

            jump sewer

        "[loc('location.sewer.option.take_sword')]":

            $ sword_found = True
            $ add_item("sword")

            call spend_time(1) from _call_spend_time_28

            "[loc('location.sewer.result.sword_result_1')]"
            "[loc('location.sewer.result.sword_result_2')]"

            jump sewer

        "[loc('location.sewer.option.read_document')]" if not ritual_found:

            $ ritual_found = True
            $ add_item("ritual_document")

            call spend_time(1) from _call_spend_time_29

            "[loc('location.sewer.result.document_result_1')]"
            "[loc('location.sewer.result.document_result_2')]"
            "[loc('location.sewer.result.document_result_3')]"

            jump sewer

        "[loc('location.sewer.option.follow_rats')]":

            call encounter_rat_king from _call_encounter_rat_king

            jump sewer

        "[loc('location.sewer.option.perform_ritual')]" if ritual_found:

            jump secret_ending

        "[loc('location.sewer.option.return_well')]":

            jump well