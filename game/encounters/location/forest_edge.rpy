label forest_edge:

    $ current_area = "Forest Edge"

    scene bg forest_edge_bg

    "[loc('location.forest_edge.description.1')]"
    "[loc('location.forest_edge.description.2')]"
    "[loc('location.forest_edge.description.3')]"

    jump forest_edge_menu

label forest_edge_menu:
    scene bg forest_edge_bg

    menu:

        "[loc('location.forest_edge.option.go_left')]":

            call spend_time(1) from _call_spend_time_9

            "[loc('location.forest_edge.result.go_left')]"

            jump deep_forest_1

        "[loc('location.forest_edge.option.go_right')]":

            call spend_time(1) from _call_spend_time_10

            "[loc('location.forest_edge.result.go_right')]"

            jump deep_forest_2

        "[loc('location.forest_edge.option.search_area')]":

            call spend_time(1) from _call_spend_time_11

            "[loc('location.forest_edge.result.search_area_1')]"
            "[loc('location.forest_edge.result.search_area_2')]"

            jump forest_edge_menu

        "[loc('travel.travel')]":

            jump travel