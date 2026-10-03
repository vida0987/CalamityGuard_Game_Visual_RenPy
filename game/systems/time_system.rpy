label spend_time(cost):
    $ time -= cost
    if time <= 0:
        jump time_over
    return

label check_survival:
    if hp <= 0:
        jump death_reset
    return

label time_over:
    "[loc('dialogue.system.time_over')]"
    jump reset_loop
