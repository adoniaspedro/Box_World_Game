# Box World

## Running the application
Go to the main.py file and change the **filename** variable value to either the *"map1.txt"*, *"map2.txt"* or *"map3.txt"* files.
And then simply run the main.py file

If wanting to run the application on the Windows cmd terminal:
### Running the app with the first map
*python main.py map1.txt*

### Running the app with the second map
*python main.py map2.txt*

### Running the app with the third map
*python main.py map3.txt*


Graph Searching
===============
Objective: Depth First Search (DFS), Breadth First Search (BFS), Dijkstra’s and A* Search algorithms applied to a simple “box” based world.

Quick Start:
------------
Download code. Extract to your favourite work location. The file to run is main.py. You will need to specify a map file to load. Something like:
  **    C:>python main.py map1.txt**

Keys (map1 and map2):
-----
1: “clear” (white)<br>
2: “mud” (grey-brownish)<br>
3: “water” (blue)<br>
4: “wall” (black)<br>
5: “start”<br>
6: “target”

Keys (map3):
-----
1: "bush" (white)<br>
2: "mud" (grey-brownish)<br>
3: "water" (aqua)<br>
4: "mountain" (light green)<br>
5: "road" (orange)<br>
6: "wall" (dark grey)<br>
7: "start"<br>
8: "target"

SPACE: force a replan (execute search)<br>
N and M: cycle (back or forward) through the search methods and replan.<br>
UP and DOWN: Increase or decrease the search step limit by one.<br>
0: Remove the search step limit. (A full search will be performed.)

E: toggle edges on/off for the current navigation graph (thin blue lines)<br>
L: toggle box (node) index values on/off (useful for understanding search and path details).<br>
C: toggle box “centre” markers on/off<br>
T: toggle tree on/off for the current search if available<br>
P: toggle path on/off for the current search if there is a successful route.

About map 3
----
Map 3 (map3.txt) is a larger, more varied map than the first two. It is also the map that is loaded if you run main.py without naming a map file. The world is 14 x 13 boxes, with the start ("S") at box 42 (column 0, row 3, counting from the bottom left) and the target ("T") at box 95 (column 11, row 6).

Unlike maps 1 and 2 it uses all six box kinds, written in the map file as:

- ".": "bush" (white)
- "m": "mud" (grey-brownish)
- "~": "water" (aqua)
- "B": "mountain" (light green)
- "R": "road" (orange)
- "X": "wall" (dark grey)

**Layout**

- The start sits in a bush and mud strip along the lower left.
- Directly above it a river of water runs across the whole map, with a single land box at the far left edge.
- A line of walls runs along the second row from the bottom (also with a gap at the far left), and a wall column closes off the right-hand side of the lower area. The direct routes are therefore either expensive (water) or blocked (walls).
- Above the river sits a band of mountain, then a central lake, and a second patch of mountain next to the target.
- Roads frame the top and left edges of the map and cross it along the third row from the top (with one mud box breaking that road).

**The agents**

Four agents plan and walk a route at the same time (coloured line = planned path, coloured circle = the agent moving along it). They use the same map and search, but each has its own movement costs for each kind of box. The cost of a move depends on the kind of box being left and the kind being entered, and diagonal moves cost 1.4142 times as much as straight ones. Because map 3 contains every box kind, the agents behave very differently on it:

- Agent 1 (black path, green circle): prefers roads, where moving from road to road is cheapest.
- Agent 2 (yellow path, blue circle): prefers mountain boxes, where moving from mountain to mountain is cheapest.
- Agent 3 (purple path, yellow circle): can move through walls, which cost the same as the cheapest move.
- Agent 4 (orange path, black circle): ignores terrain, so every move costs the same.

**Routes taken**

With the unedited map and the default search (Dijkstra) the agents choose these routes:

- Agent 1: 23 boxes, cost about 32.1. Up the left-hand road, across the road along row 10 (stepping onto a bush box to avoid the mud) and down the right-hand road to the target.
- Agent 2: 13 boxes, cost about 17.1. Across the band of mountain boxes, then straight on to the target.
- Agent 3: 17 boxes, cost about 21.3. Through the line of walls along the bottom and up the wall column on the right.
- Agent 4: 12 boxes, cost about 12.2. Almost straight across, crossing the river at a single water box.

Try changing boxes (for example turn a stretch of road into water, or open a gap in the walls) to see how each agent re-plans. The agents are also present on maps 1 and 2, but those maps only use bush, mud, water and walls, so the routes differ much less.

About maps 1 and 2
----
There are two simple maps to start with named map1.txt and map2.txt. You can create your own later if you wish.

The worlds boxes can be changed with a combination of selecting the box “kind” (show in the top left text) and then left-clicking on to a box. There are currently four different box kinds:

- 1: “clear” (white)
- 2: “mud” (grey-brownish)
- 3: “water” (blue)
- 4: “wall” (black)

Walls are not included (have no edges) in the navigation graph.

For each search a start (“S”) and target (“T”) box is needed. To change the location of either, first set the kind value, and click on to a box:

- 5: “start”
- 6: “target”

You can allocate start or target to wall box that has no edges, however this will stop any search from being successful!

Pressing the SPACE key will perform a search using the current map and search mode, however most changes to the world force a new search to be done immediately.

- "SPACE": performace full search (if not already done)

There are currently four different search modes, which can be cycled through using the N and M keys (backwards and forwards respectively).

- "N": previous search mode
- "M": next search mode

The search modes are:

- “BFS” for Best First search algorithm
- “DFS” for Depth First search algorithm
- “Dijkstra” for Dijkstra’s lowest-cost-so-far search algorithm
- “A*” (written as “AStar”) for the lowest cost-so-far + lowest-estimated-cost algorithm

Search “depth” (the number of search steps taken) can be limited and changed using the UP and DOWN arrow keys. The limit can be removed using the “0” key.

- "UP": increase search step depth limit
- "DOWN": decrease search step depth
- "0": remove search step limit