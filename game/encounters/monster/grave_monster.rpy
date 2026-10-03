label encounter_grave_monster:
    "[loc('dialogue.grave_monster.attack')]"
    call combat(loc("character.grave_monster"), 2, 1, "images/monster/tree_monster_A.png") from _call_combat_4
    return _return
