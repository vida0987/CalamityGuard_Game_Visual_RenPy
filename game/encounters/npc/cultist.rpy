default cultist_questions_asked = 0
default cultist_identity_asked = False
default cultist_purpose_asked = False
default cultist_monsters_asked = False

label cultist:
    $ cultist_questions_asked = 0
    $ cultist_identity_asked = False
    $ cultist_purpose_asked = False
    $ cultist_monsters_asked = False

    scene npc cultist
    "[loc('dialogue.cultist.intro.1')]"
    "[loc('dialogue.cultist.intro.2')]"

    while True:

        menu:
            "[loc('dialogue.cultist.question.identity')]" if not cultist_identity_asked:
                $ cultist_identity_asked = True
                $ cultist_questions_asked += 1

                "[loc('dialogue.cultist.result.identity.1')]"
                "[loc('dialogue.cultist.result.identity.2')]"

            "[loc('dialogue.cultist.question.purpose')]" if not cultist_purpose_asked:
                $ cultist_purpose_asked = True
                $ cultist_questions_asked += 1

                "[loc('dialogue.cultist.result.purpose.1')]"
                "[loc('dialogue.cultist.result.purpose.2')]"
                "[loc('dialogue.cultist.result.purpose.3')]"

            "[loc('dialogue.cultist.question.monsters')]" if not cultist_monsters_asked:
                $ cultist_monsters_asked = True
                $ cultist_questions_asked += 1
                "[loc('dialogue.cultist.result.monsters.1')]"
                "[loc('dialogue.cultist.result.monsters.2')]"

            "[loc('dialogue.cultist.question.attack')]":

                if cultist_questions_asked >= 1:
                    "[loc('dialogue.cultist.result.attack.one_question')]"

                else:
                    "[loc('dialogue.cultist.result.attack.no_question')]"

                $ cultist_hp = 2 + cultist_questions_asked

                call combat(
                    loc("character.cultist"),
                    cultist_hp,
                    1,
                    "images/npc/cultist.png",
                    False
                ) from _call_combat_6

                if _return == "victory":
                    "[loc('dialogue.cultist.result.after_battle')]"

                jump deep_forest_2