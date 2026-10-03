label encounter_forest_monster:
    show forest_monster at center with dissolve
    if forest_observed:
        "[loc('dialogue.forest_monster.unaware')]"
    else:
        $ hp -= 2
        "[loc('dialogue.forest_monster.ambush')]"
        call check_survival from _call_check_survival
    call combat(loc("character.forest_monster"), 2, 1, "images/monster/tree_monster_A.png", False) from _call_combat_3
    hide forest_monster with dissolve
    return _return
