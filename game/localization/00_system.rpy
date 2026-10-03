init -10 python:
    LOCALIZED_TEXT = {
        "en": {},
        "vi": {},
    }
    _locations_normalized = False

    def _normalize_locations():
        """Expose location choices and outcomes in nested groups."""
        global _locations_normalized
        if _locations_normalized:
            return

        for language_data in LOCALIZED_TEXT.values():
            for location_data in language_data.get("location", {}).values():
                if not isinstance(location_data, dict):
                    continue

                options = location_data.setdefault("option", {})
                results = location_data.setdefault("result", {})
                for key, value in list(location_data.items()):
                    if key in ("description", "option", "result", "travel"):
                        continue
                    if key.endswith(("_result", "_quiet")) or key in ("seal_closes", "final_grave"):
                        results.setdefault(key, value)
                    else:
                        options.setdefault(key, value)
                    del location_data[key]

                location_data.pop("travel", None)

        _locations_normalized = True

    def t(key, **values):
        """Resolve a dot-notation localization key in the selected language."""
        _normalize_locations()
        language = getattr(renpy.store, "ui_language", "en")

        def resolve(language_data):
            value = language_data
            for part in key.split("."):
                if not isinstance(value, dict) or part not in value:
                    return None
                value = value[part]
            return value if isinstance(value, str) else None

        text = resolve(LOCALIZED_TEXT.get(language, {}))
        if text is None:
            text = resolve(LOCALIZED_TEXT.get("en", {}))
        if text is None:
            return "[Missing: {}]".format(key)

        return text.format(**values)

    def loc(key, **values):
        return t(key, **values)

    def toggle_game_music():
        renpy.store.music_enabled = not renpy.store.music_enabled
        if renpy.store.music_enabled:
            renpy.music.play("audio/nhac_test.mp3", loop=True)
        else:
            renpy.music.stop()
