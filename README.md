# Stimcraft
> Stimulate your Starcraft II performances

## Usage

Use `vercel dev` for local development.

## UI
------------------------
|         Info         |
|       Economy        |
|         Army         |
| Strategy | Mechanics |
------------------------

- Info (Players, Map, Links DL+YT+GG|RS|ST, Date, Duration, Format, Matchup, Type, Realm, Region, Release)
- Economy (Worker, Income, Structures, Upgrades)
- Army (Units, Units Lost, Army Value)
- Strategy
  - Minimap
  - Build Order
  - Scouting
- Mechanics
  - EPM
  - Macro
  - Micro

## API
`GET /api/st-<id>` decodes the [Spawning Tool](https://lotv.spawningtool.com) replay `<id>` with [s2protocol](https://github.com/Blizzard/s2protocol), game events excluded:
```
attributeevents
details
header
initdata
messageevents
trackerevents
```

## Observer UI - WCS 3.0
A - Army Value
T - Structures
U - Units
I - Income
O > Observer
P > Pause
S - Spending
D - Production
F > Seek Forward
G - Upgrades
L - Units Lost
M - APM
W > Zoom In/Out
C > Camera follow
B > Seek Backward

n - Player/Observer n
F10 - Menu
F11 - Message
F12 - Tutorial
Shift-L - Units Lost Panel
Ctrl-Z - Toggle Interface
Ctrl-R - Unit/Worker Killed Panel
Ctrl-I - Income Panel
Ctrl-Q - Army/Worker Panel
Ctrl-C - APM Panel
Ctrl-V - EPM Panel
Ctrl-N - Player Panel
Ctrl-Shift-O - Observer Panel
) - Faster
- - Slower

### Links:
- https://cmsw.mit.edu/mit-overseer-observer-mod-starcraft-2/
- https://wcs.starcraft2.com/en-us/news/20563599/Pro-StarCraft-II-Explained:-Observer-Panel/
- https://imgur.com/a/fVEdZ

### Resources
- https://starcraft.fandom.com/wiki/List_of_StarCraft_II_units
- https://liquipedia.net/starcraft2/Protoss_Upgrades
- https://starcraft2.com/en-us/news/22938943
- https://comic.starcraft2.com/en-us/shadow-wars-part-1
- https://eu.battle.net/forums/en/sc2/18518180/
- https://www.download-free-fonts.com/details/90021/starcraft-normal
- https://www.download-free-fonts.com/details/76365/eurostile-extended
- https://www.download-free-fonts.com/details/79984/eurostile-bold-extended
- https://codepen.io/xonic/pen/KWMaqe
