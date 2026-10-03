label house_a:

    $ current_area = "House A"

    scene bg house_A_bg

    "[loc('location.house_a.description.1')]"
    "[loc('location.house_a.description.2')]"
    "[loc('location.house_a.description.3')]"
    "[loc('location.house_a.description.4')]"

    menu:

        "[loc('location.house_a.option.take_rake')]" if not has_item("rake"):

            $ add_item("rake")

            call spend_time(1) from _call_spend_time_19

            "[loc('location.house_a.result.rake_result')]"

            jump house_a

        "[loc('location.house_a.option.take_shovel')]" if not has_item("shovel"):

            $ add_item("shovel")

            call spend_time(1) from _call_spend_time_20

            "[loc('location.house_a.result.shovel_result')]"

            jump house_a

        "[loc('location.house_a.option.take_knife')]" if not has_item("knife"):

            $ add_item("knife")

            call spend_time(1) from _call_spend_time_21

            "[loc('location.house_a.result.knife_result')]"

            jump house_a

        "[loc('location.house_a.option.take_hammer')]" if not has_item("hammer"):

            $ add_item("hammer")

            call spend_time(1) from _call_spend_time_22

            "[loc('location.house_a.result.hammer_result')]"

            jump house_a

        "[loc('location.house_a.option.search_house')]":

            call spend_time(1) from _call_spend_time_23

            "[loc('location.house_a.result.house_result_1')]"

            "[loc('location.house_a.result.house_result_2')]"

            "[loc('location.house_a.result.house_result_3')]"

            jump house_a

        "[loc('travel.travel')]":

            jump travel