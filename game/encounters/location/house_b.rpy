label house_b:

    $ current_area = "House B"

    scene bg house_B_bg

    "[loc('location.house_b.description.1')]"
    "[loc('location.house_b.description.2')]"
    "[loc('location.house_b.description.3')]"

    menu:

        "[loc('location.house_b.option.examine_notebook')]":

            call spend_time(1) from _call_spend_time_24

            "[loc('location.house_b.result.notebook_result_1')]"
            "[loc('location.house_b.result.notebook_result_2')]"
            "[loc('location.house_b.result.notebook_result_3')]"
            "[loc('location.house_b.result.notebook_result_4')]"
            "[loc('location.house_b.result.notebook_result_5')]"

            jump house_b

        "[loc('location.house_b.option.search_bed')]":

            call spend_time(1) from _call_spend_time_25

            $ add_item("mental_charm")

            "[loc('location.house_b.result.bed_result_1')]"
            "[loc('location.house_b.result.bed_result_2')]"
            "[loc('location.house_b.result.bed_result_3')]"

            jump house_b

        "[loc('location.house_b.option.search_house')]":

            call spend_time(1) from _call_spend_time_26
            $ seal_material_b = True
            $ add_item("seal_material_b")

            "[loc('location.house_b.result.search_result_1')]"
            "[loc('location.house_b.result.search_result_2')]"
            "[loc('location.house_b.result.search_result_3')]"
            "[loc('location.house_b.result.search_result_4')]"
            "[loc('location.house_b.result.search_result_5')]"
            "[loc('location.house_b.result.search_result_6')]"
            "[loc('location.house_b.result.search_result_7')]"
            "[loc('location.house_b.result.search_result_8')]"

            jump house_b

        "[loc('travel.travel')]":

            jump travel