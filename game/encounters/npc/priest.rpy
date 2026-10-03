label encounter_priest:

    scene npc ghost_priest

    "[loc('dialogue.priest.intro')]"

    while True:

        menu:

            "[loc('dialogue.priest.question.ask_village')]":

                call spend_time(1) from _call_spend_time_46

                "[loc('dialogue.priest.result.village_1')]"
                "[loc('dialogue.priest.result.village_2')]"
                "[loc('dialogue.priest.result.village_3')]"
                "[loc('dialogue.priest.result.village_4')]"
                "[loc('dialogue.priest.result.village_5')]"
                "[loc('dialogue.priest.result.village_6')]" 

            "[loc('dialogue.priest.question.ask_monster')]":

                call spend_time(1) from _call_spend_time_47

                "[loc('dialogue.priest.result.monster_1')]"
                "[loc('dialogue.priest.result.monster_2')]"
                "[loc('dialogue.priest.result.monster_3')]"
                "[loc('dialogue.priest.result.monster_4')]"
                "[loc('dialogue.priest.result.monster_5')]"

            "[loc('dialogue.priest.question.ask_night_guard')]":

                call spend_time(1) from _call_spend_time_48

                "[loc('dialogue.priest.result.night_guard_1')]"
                "[loc('dialogue.priest.result.night_guard_2')]"
                "[loc('dialogue.priest.result.night_guard_3')]"
                "[loc('dialogue.priest.result.night_guard_4')]"
                "[loc('dialogue.priest.result.night_guard_5')]"

            "[loc('dialogue.priest.question.ask_priest')]":

                call spend_time(1) from _call_spend_time_49

                "[loc('dialogue.priest.result.self_1')]"
                "[loc('dialogue.priest.result.self_2')]"
                "[loc('dialogue.priest.result.self_3')]"
                "[loc('dialogue.priest.result.self_4')]"

            "[loc('dialogue.priest.question.leave')]":

                "[loc('dialogue.priest.result.leave_1')]"
                "[loc('dialogue.priest.result.leave_2')]"

                return