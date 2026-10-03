init python:

    def roll_damage(roll_count=1):
        total_damage = 0
        rolls = []

        damage_table = [0, 1, 2, 1, 2, 3]

        for _ in range(roll_count):
            roll = renpy.random.randint(1, 6)
            damage = damage_table[roll - 1]

            rolls.append(roll)
            total_damage += damage

        return rolls, total_damage


label combat(enemy_name_arg, enemy_hp_arg, enemy_damage_arg, enemy_image_arg, can_run=True, require_weapon=False):

    if require_weapon and not (
        has_item("knife")
        or has_item("light_charm")
        or has_item("holy_badge")
        or has_item("sword")
    ):
        jump no_weapon_ending

    $ enemy_name = enemy_name_arg
    $ enemy_hp = enemy_hp_arg
    $ enemy_damage = enemy_damage_arg
    $ enemy_image = enemy_image_arg
    $ enemy_active = True

    scene expression enemy_image

    while enemy_hp > 0:

        # =========================
        # CHỌN HÀNH ĐỘNG
        # =========================

        menu:

            "[loc('dialogue.combat.punch')]":
                $ attack_type = "punch"

            "[loc('dialogue.combat.use_knife')]" if has_item("knife"):
                $ attack_type = "knife"

            "[loc('dialogue.combat.use_light_charm')]" if has_item("light_charm"):
                $ attack_type = "light_charm"

            "[loc('dialogue.combat.run')]" if can_run:
                $ enemy_active = False
                return "escape"


        # =========================
        # XÁC ĐỊNH SỐ LẦN ROLL
        # =========================

        $ roll_count = 3 if has_item("sword") else 1


        # =========================
        # ROLL DAMAGE
        # =========================

        $ rolls, damage = roll_damage(roll_count)


        # =========================
        # XỬ LÝ HIỆU ỨNG TRANG BỊ
        # =========================

        if attack_type == "knife":

            $ damage += 2

        elif attack_type == "light_charm":

            $ damage += 4
            $ remove_item("light_charm")


        # =========================
        # GÂY DAMAGE
        # =========================

        $ enemy_hp -= damage


        # =========================
        # HIỂN THỊ KẾT QUẢ
        # =========================

        if enemy_hp > 0:

            "[loc('dialogue.combat.attack_result', damage=damage)]"

        else:

            "[loc('dialogue.combat.attack_result_defeat', damage=damage)]"


        # =========================
        # QUÁI PHẢN CÔNG
        # =========================

        if enemy_hp > 0:

            $ received_damage = enemy_damage

            if has_item("holy_badge"):
                $ received_damage = max(0, received_damage - 1)

            $ hp -= received_damage

            "[loc('dialogue.combat.counterattack', enemy_name=enemy_name, damage=received_damage)]"

            call check_survival from _call_check_survival_1


    $ enemy_active = False

    return "victory"