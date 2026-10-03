label encounter_church_monster:
    "[loc('dialogue.church_monster.attack')]"
    call combat(loc("character.church_monster"), 1, 1, "images/monster/tree_monster_B.png") from _call_combat_2
    if _return == "victory":
        "[loc('dialogue.church_monster.defeat')]"
    return _return
