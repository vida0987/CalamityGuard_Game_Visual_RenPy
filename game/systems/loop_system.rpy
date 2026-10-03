label death_reset:
    scene bg death_reset_bg
    "[loc('dialogue.system.death')]"
    jump reset_loop

label reset_loop:
    $ loop += 1
    $ hp = STARTING_HP
    $ time = STARTING_TIME
    $ inventory = []
    $ seal_material_a = False
    $ seal_material_b = False
    $ seal_material_c = False
    $ ritual_found = False
    $ sewer_unlocked = False
    $ graveyard_unlocked = False
    $ deep_forest_unlocked = False
    $ church_monster_dead = False
    $ forest_monster_dead = False
    $ grave_2 = False
    $ grave_6 = False
    $ grave_7 = False
    $ seal_complete = False
    $ escaped = False
    $ tree_checked = False
    $ note_read = False
    $ forest_observed = False
    $ rat_king_talked = False
    $ enemy_active = False
    $ deep_forest_2_monsters_killed = 0
    $ deep_forest_2_npc_met = False
    hide forest_monster
    hide boss_monster_sealed
    hide boss_monster_unsealed
    hide rat_king
    "[loc('dialogue.system.reset')]"
    jump village_gate
