# Norton Village

Norton Village is a text-only visual novel that immerses players in a cosmic horror investigation. Set in a mysterious village, players will explore various locations, gather information, and make choices that will affect the outcome of their journey. The game emphasizes exploration, information gathering, and creating a sense of unease, all while under the pressure of time.

## Gameplay Mechanics

- **HP**: Players start with a maximum of 7 HP. Encounters may cause damage, affecting survival.
- **TIME**: Players begin with 30 TIME, which decreases with travel and actions. If TIME reaches 0, the game resets.
- **LOOP**: The game tracks the number of loops experienced, increasing after each reset.
- **Inventory**: Collect items that influence gameplay, including weapons and materials.
- **Simple Combat**: Engage in combat with enemies using normal attacks or items.
- **Multiple Endings**: The game features various outcomes based on player choices and actions.

## State Variables

- **Health**: `hp`, `max_hp`
- **Time**: `time`, `loop`
- **Items**: `knife`, `mental_charm`, `light_charm`, `holy_badge`, `water_sample`, `bark_piece`, `seal_knowledge`, `seal_materials`, `seal_complete`
- **Monsters**: `church_monster_dead`, `forest_monster_dead`
- **Unlocks**: `sewer_unlocked`, `deep_forest_unlocked`, `graveyard_unlocked`
- **Graves**: `grave_2`, `grave_6`, `grave_7`
- **Ritual**: `ritual_found`

## Game Structure

The game features six main areas and four hidden areas, each with unique interactions and descriptions. Players navigate through these locations, making choices that will lead to different endings.

## Installation Instructions

1. Download the project files.
2. Ensure you have Ren'Py installed on your system.
3. Place the project folder in the Ren'Py projects directory.
4. Launch Ren'Py and select "Norton Village" to start playing.

## License

This project is licensed under [insert license type here]. Please refer to the LICENSE file for more details. 

## Acknowledgments

Thank you for exploring Norton Village. We hope you enjoy the experience and uncover the mysteries that lie within!