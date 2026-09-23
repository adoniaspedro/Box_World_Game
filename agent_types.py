#Goes on the road to reach the final destination (green)
box_types = {
	"BUSH":{"symbol":'.', "cost":{"BUSH":2, "MUD":5,"WATER":7,"MOUNTAIN":4,"ROAD":2}, "colour":"WHITE"},
	"MUD":{"symbol":'m', "cost":{"BUSH":2, "MUD":7,"WATER":9,"MOUNTAIN":4,"ROAD":3}, "colour":"BROWN"},
	"WATER":{"symbol":'~', "cost":{"BUSH":2, "MUD":9,"WATER":10,"MOUNTAIN":4,"ROAD":4}, "colour":"AQUA"},
	"MOUNTAIN":{"symbol":'B', "cost":{"BUSH":2, "MUD":6,"WATER":10,"MOUNTAIN":4,"ROAD":3}, "colour":"LIGHT_GREEN"},
	"ROAD":{"symbol":'R', "cost":{"BUSH":2, "MUD":4,"WATER":10,"MOUNTAIN":4,"ROAD":1}, "colour":"ORANGE"},
	"WALL":{"symbol":'X', "colour":"GREY"},
}

#Box values for by agent 1 - Mainly goes through bushes (blue)
agent2 = {
	"BUSH":{"symbol":'.', "cost":{"BUSH":2, "MUD":5,"WATER":7,"MOUNTAIN":2,"ROAD":2}, "colour":"WHITE"},
	"MUD":{"symbol":'m', "cost":{"BUSH":2, "MUD":7,"WATER":9,"MOUNTAIN":4,"ROAD":3}, "colour":"BROWN"},
	"WATER":{"symbol":'~', "cost":{"BUSH":2, "MUD":9,"WATER":10,"MOUNTAIN":4,"ROAD":4}, "colour":"AQUA"},
	"MOUNTAIN":{"symbol":'B', "cost":{"BUSH":2, "MUD":4,"WATER":10,"MOUNTAIN":1,"ROAD":2}, "colour":"LIGHT_GREEN"},
	"ROAD":{"symbol":'R', "cost":{"BUSH":2, "MUD":4,"WATER":10,"MOUNTAIN":1,"ROAD":1}, "colour":"ORANGE"},
	"WALL":{"symbol":'X', "colour":"GREY"},
}

#Box values for agent 2 - Goes through the Wall's (yellow)
agent3 = {
	"BUSH":{"symbol":'.', "cost":{"BUSH":2, "MUD":5,"WATER":7,"MOUNTAIN":4,"ROAD":2,"WALL":1}, "colour":"WHITE"},
	"MUD":{"symbol":'m', "cost":{"BUSH":2, "MUD":7,"WATER":9,"MOUNTAIN":4,"ROAD":3,"WALL":1}, "colour":"BROWN"},
	"WATER":{"symbol":'~', "cost":{"BUSH":2, "MUD":9,"WATER":10,"MOUNTAIN":4,"ROAD":4,"WALL":1}, "colour":"AQUA"},
	"MOUNTAIN":{"symbol":'B', "cost":{"BUSH":2, "MUD":6,"WATER":10,"MOUNTAIN":4,"ROAD":3,"WALL":1}, "colour":"LIGHT_GREEN"},
	"ROAD":{"symbol":'R', "cost":{"BUSH":2, "MUD":4,"WATER":10,"MOUNTAIN":4,"ROAD":1,"WALL":1}, "colour":"ORANGE"},
	"WALL":{"symbol":'X', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1,"WALL":1}, "colour":"GREY"},
}

#Box values used by agent 3 - Ignores terrain values (black)
agent4 = {
	"BUSH":{"symbol":'.', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1}, "colour":"WHITE"},
	"MUD":{"symbol":'m', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1}, "colour":"BROWN"},
	"WATER":{"symbol":'B', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1}, "colour":"AQUA"},
	"MOUNTAIN":{"symbol":'R', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1}, "colour":"LIGHT_GREEN"},
	"ROAD":{"symbol":'~', "cost":{"BUSH":1, "MUD":1,"WATER":1,"MOUNTAIN":1,"ROAD":1}, "colour":"ORANGE"},
	"WALL":{"symbol":'X', "colour":"GREY"},
}