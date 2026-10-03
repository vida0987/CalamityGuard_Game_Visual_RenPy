label boss:
    $ current_area = "Grave #4"
    if seal_complete:
        show boss_monster_sealed at center with dissolve
        "[loc('dialogue.boss.sealed_intro')]"
        call combat(loc("character.sealed_entity"), 5, 2, "images/monster/seal_boss.png", False, False) from _call_combat
        hide boss_monster_sealed with dissolve
        if _return == "victory":
            jump good_ending
    else:
        show boss_monster_unsealed at center with dissolve
        "[loc('dialogue.boss.unsealed_intro')]"
        call combat(loc("character.unsealed_entity"), 15, 3, "images/monster/un_seal_boss.jpg", False, False) from _call_combat_1
        hide boss_monster_unsealed with dissolve
        if _return == "victory":
            jump normal_success_ending
