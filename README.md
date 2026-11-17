# Piece the Nation

A drag-and-drop tile puzzle that teaches US geography with a little history built in. Students drag labeled state and territory tiles onto a blank map with no internal borders. It is a single self-contained web page, so it works offline and on GitHub Pages.

## Levels

| Level | Map | Source file |
|---|---|---|
| 1789 | The Thirteen (original states' 1789 borders standing in for the colonies) | `1789030` |
| 1803 | After the Louisiana Purchase | `1803040` |
| 1848 | After the Mexican Cession | `1848080` |
| 1912 | The lower 48 | `1912080` |

Challenge settings: Guided (names shown, wide snap), Explorer (names shown), Cartographer (shapes only, tight snap). Tap-then-tap and keyboard selection work as alternatives to dragging.

## Run it

Open `index.html` in a browser. No build step or server is needed. To publish, enable GitHub Pages for the `main` branch root.

## Sources

Every history fact in the game carries a numbered source (see the Sources button in the game).

- Admission and ratification dates: Congressional Research Service, *Admission of States to the Union: A Historical Reference Guide* (R47747, updated Jan. 6, 2026).
- Year each colony was settled: Ballotpedia, *Original thirteen states*; thirteen-colony range: Encyclopedia.com.
- Treaty facts: National Archives (Louisiana Purchase Treaty; Treaty of Guadalupe Hidalgo), National Park Service, USGS National Atlas.

## Map data and its limits

Boundaries come from [poezn/us-history-maps](https://github.com/poezn/us-history-maps) (Michael Porath, 2012). That repository states no license, so confirm terms before redistributing the data or the page beyond classroom use. Borders were simplified for play and are approximate. Colonial charters and Native nations' lands are not drawn. For exact borders, use the Newberry Library Atlas of Historical County Boundaries.

## Rebuilding `index.html`

`build/` holds the scripts that produce the page:

- `build_data.py` projects the source GeoJSON (Albers equal-area), simplifies it and writes tile geometry.
- `facts.py` holds the sourced facts and level text.
- `build_html.py` merges both into `template.html` and writes `index.html`.

Paths inside the scripts point at the author's workspace; edit `SRC`, `OUT` and the file paths at the top of each script before running. Requires Python 3 with `shapely` 2.1+ and `numpy`.
