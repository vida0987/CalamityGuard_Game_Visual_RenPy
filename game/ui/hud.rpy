screen character_panel():
    vbox:
        xfill True
        spacing 18

        text "[loc('ui.character')]" xalign 0.5

        vbox:
            spacing 6
            text "[loc('ui.hp')]"
            bar value StaticValue(hp, max_hp) xfill True
            text "[hp] / [max_hp]" xalign 0.5

        vbox:
            spacing 4
            text "[loc('ui.time')]"
            text "[time]" size 42 xalign 0.5

        vbox:
            spacing 4
            text "[loc('ui.loop')]"
            text "[loop]" size 42 xalign 0.5

        if enemy_active:
            null height 18
            vbox:
                xfill True
                spacing 6
                text "[loc('ui.enemy')]" xalign 0.5
                text "[enemy_name]" xalign 0.5
                text "[loc('ui.enemy_hp', value=enemy_hp)]" xalign 0.5
                text "[loc('ui.attack')]: [enemy_damage]" xalign 0.5

        null height 18
        vbox:
            xfill True
            spacing 6
            text "[loc('ui.language')]" xalign 0.5
            hbox:
                xalign 0.5
                spacing 8
                textbutton "EN" action SetVariable("ui_language", "en") sensitive ui_language != "en"
                textbutton "VI" action SetVariable("ui_language", "vi") sensitive ui_language != "vi"

            text "[loc('ui.music')]" xalign 0.5
            textbutton "[loc('ui.music_on') if music_enabled else loc('ui.music_off')]" action Function(toggle_game_music) xalign 0.5
