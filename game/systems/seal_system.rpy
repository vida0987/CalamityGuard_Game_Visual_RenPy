label check_seal:
    if grave_2 and grave_6 and grave_7:
        $ seal_complete = True
        "[loc('dialogue.system.seal_complete')]"
    else:
        "[loc('dialogue.system.seal_incomplete')]"
    return
