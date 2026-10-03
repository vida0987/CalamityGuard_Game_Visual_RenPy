label travel:
    $ current_area = "Village Roads"
    menu:
        "[loc('travel.village_gate')]":
            call spend_time(2) from _call_spend_time_31
            jump village_gate
        "[loc('travel.well')]":
            call spend_time(2) from _call_spend_time_32
            jump well
        "[loc('travel.house_a')]":
            call spend_time(2) from _call_spend_time_33
            jump house_a
        "[loc('travel.house_b')]":
            call spend_time(2) from _call_spend_time_34
            jump house_b
        "[loc('travel.church')]":
            call spend_time(2) from _call_spend_time_35
            jump church
        "[loc('travel.forest_edge')]":
            call spend_time(2) from _call_spend_time_36
            jump forest_edge
        "[loc('travel.deep_forest')]" if deep_forest_unlocked:
            call spend_time(2) from _call_spend_time_37
            jump deep_forest
        "[loc('travel.graveyard')]" if graveyard_unlocked:
            call spend_time(2) from _call_spend_time_38
            jump graveyard
        "[loc('travel.leave')]":
            jump normal_ending
