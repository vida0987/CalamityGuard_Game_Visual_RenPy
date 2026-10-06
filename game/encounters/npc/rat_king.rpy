label encounter_rat_king:

    show npc rat_king at rat_king_center with dissolve

    "[loc('dialogue.rat_king.result.conversation_intro')]"

    jump encounter_rat_king_menu

label encounter_rat_king_menu:
    menu:

        "[loc('dialogue.rat_king.question.ask')]":

            "[loc('dialogue.rat_king.result.ask_1')]"
            "[loc('dialogue.rat_king.result.ask_2')]"

            menu:

                "[loc('dialogue.rat_king.question.give_cheese')]":

                    $ infernal_gold = True
                    $ rat_king_gold = True

                    "[loc('dialogue.rat_king.result.give_cheese_1')]"
                    "[loc('dialogue.rat_king.result.give_cheese_2')]"
                    "[loc('dialogue.rat_king.result.give_cheese_3')]"
                    "[loc('dialogue.rat_king.result.give_cheese_4')]"

                    jump encounter_rat_king_menu

                "[loc('dialogue.rat_king.question.keep_cheese')]":

                    "[loc('dialogue.rat_king.result.keep_cheese_1')]"
                    "[loc('dialogue.rat_king.result.keep_cheese_2')]"
                    "[loc('dialogue.rat_king.result.keep_cheese_3')]"

                    jump encounter_rat_king_menu

        "[loc('dialogue.rat_king.question.identity')]":

            "[loc('dialogue.rat_king.result.identity_1')]"
            "[loc('dialogue.rat_king.result.identity_2')]"
            "[loc('dialogue.rat_king.result.identity_3')]"
            "[loc('dialogue.rat_king.result.identity_4')]"
            "[loc('dialogue.rat_king.result.identity_5')]"

            jump encounter_rat_king_menu

        "[loc('dialogue.rat_king.question.attack')]":

            "[loc('dialogue.rat_king.result.attack_1')]"
            "[loc('dialogue.rat_king.result.attack_2')]"
            "[loc('dialogue.rat_king.result.attack_3')]"

            jump rat_king_bad_end

        "[loc('dialogue.rat_king.question.leave')]":

            hide npc rat_king with dissolve

            return


label rat_king_bad_end:

    "[loc('dialogue.rat_king.result.bad_end_1')]"
    "[loc('dialogue.rat_king.result.bad_end_2')]"

    jump death_reset