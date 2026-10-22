from math import hypot
from enum import Enum
from graphics import COLOUR_NAMES, window
import pyglet
from point2d import Point2D
from graph import SparseGraph, Node, Edge
from searches import SEARCHES
from agent_types import *
from agent import agent

min_edge_cost = 1.0 # must be min value for heuristic cost to work

# def edge_cost(k1, k2):
# 	k1 = box_type.index(k1)
# 	k2 = box_type.index(k2)
# 	return edge_cost_matrix[k1][k2]

search_modes = list(SEARCHES.keys())

class Box(object):
	'''A single box for boxworld. '''

	def __init__(self,index, x, y, width, height, type='.'):
		self.x = x
		self.y = y
		self.index = index
		self.width = width
		self.height = height
		for key, value in box_types.items():
			if value['symbol'] == type:
				self.type = key
		#a box must be able to draw:
		# - a box with a grey outline and an (optional) filled colour
		self.box = pyglet.shapes.BorderedRectangle(
			x, y, width, height, border=1,
			color=COLOUR_NAMES[box_types[self.type]["colour"]], 
			border_color=COLOUR_NAMES["LIGHT_GREY"],
			batch=window.get_batch()
		)
		# - a label showing the box index
		self.label = pyglet.text.Label(
			str(index),
			font_name='Times New Roman',
			font_size=12,
			x=x+width//2, y=y+height//2,
			anchor_x='center', anchor_y='center',
			color=COLOUR_NAMES["BLACK"],
			batch=window.get_batch("numbers")
		)
		
		# nav graph node
		self.node = None

	def set_type(self, type):
		#this code gets repeated in a couple of places in theis func, so I made it a function-within-a-function
		#it's usually good practice to make sure things are only ever done in a single location, but sometimes that can make things harder to read
		def update_box(type):
			self.type = type
			self.box.color = COLOUR_NAMES[box_types[self.type]["colour"]]
		if type in box_types:
			update_box(type)
			return
		else:
			for key, value in box_types.items():
				if value['symbol'] == type:
					update_box(key)
					return
		print('not a known tile type "%s"' % type)
	
	def center(self):
		return Point2D(self.x+self.width//2, self.y+self.height//2)

class BoxWorld(object):
	'''A world made up of boxes. '''

	def __init__(self, x_boxes, y_boxes, window_width, window_height):
		self.boxes = [None]*x_boxes*y_boxes
		self.x_boxes= x_boxes 
		self.y_boxes= y_boxes 
		box_width = window_width // x_boxes
		box_height = window_height // y_boxes
		self.wx = (window_width-1) // self.x_boxes
		self.wy = (window_height-1) // self.y_boxes 
		for i in range(len(self.boxes)):
			self.boxes[i] = Box(
				i,
				i%x_boxes*box_width,
				i//x_boxes%y_boxes*box_height,
				box_width,box_height
			)
		
		self.start = self.boxes[1]
		self.start_marker = pyglet.shapes.Arc( #in pyglet a circle is filled, an arc is unfilled
			self.boxes[1].center().x,
			self.boxes[1].center().y,
			15, segments=30,
			color=COLOUR_NAMES["RED"],
			batch=window.get_batch("path"),
			thickness=4
		)
		self.target = self.boxes[2]
		self.target_marker = pyglet.shapes.Arc(
			self.boxes[2].center().x,
			self.boxes[2].center().y,
			15, segments=30,
			color=COLOUR_NAMES["GREEN"],
			batch=window.get_batch("path"),
			thickness=4
		)

		#lists used to store the primitives that render out our various pathfinding data
		self.render_path = []
		self.render_tree = []
		self.render_open_nodes = []
		self.render_graph = []
		self.render_agents = []
		self.agents = [
			agent(self.start,self.target,agent2,self._max,self.x_boxes,self.y_boxes,self.boxes,2,COLOUR_NAMES['YELLOW'],COLOUR_NAMES['BLUE']),
			agent(self.start,self.target,agent3,self._max,self.x_boxes,self.y_boxes,self.boxes,3,COLOUR_NAMES['PURPLE'],COLOUR_NAMES['YELLOW']),
			agent(self.start,self.target,agent4,self._max,self.x_boxes,self.y_boxes,self.boxes,4,COLOUR_NAMES['ORANGE'],COLOUR_NAMES['BLACK']),
			agent(self.start,self.target,box_types,self._max,self.x_boxes,self.y_boxes,self.boxes,1,COLOUR_NAMES['BLACK'],COLOUR_NAMES['GREEN'])
		]

		self.reset_navgraph()

	def get_box_by_xy(self, ix, iy):
		idx = (self.x_boxes * iy) + ix
		return self.boxes[idx] if idx < len(self.boxes) else None

	def get_box_by_pos(self, x, y):
		idx = int(self.x_boxes * (y // self.wy)) + int(x // self.wx)
		return self.boxes[idx] if idx < len(self.boxes) else None

	def _max(self, idx1, idx2):
		'''Return the straight line distance between two points on a 2-D
		Cartesian plane. Argh, Pythagoras... trouble maker. '''
		x1, y1 = self.boxes[idx1].pos
		x2, y2 = self.boxes[idx2].pos
		return max(abs(x1-x2),abs(y1-y2)) * min_edge_cost


	def reset_navgraph(self):
		''' Create and store a new nav graph for this box world configuration.
		The graph is build by adding NavNode to the graph for each of the
		boxes in box world. Then edges are created (4-sided).
		'''
		for l in self.render_graph:
			try:
				l.delete() 
			except:
				pass
		for a in self.agents:
			a.reset_navgraph()
			self.render_graph.append(a.render_graph)

	def set_start(self, idx):
		'''Set the start box based on its index idx value. '''
		# remove any existing start node, set new start node
		if self.target == self.boxes[idx]:
			print("Can't have the same start and end boxes!")
			return
		self.start = self.boxes[idx]
		self.start_marker.x = self.start.center().x
		self.start_marker.y = self.start.center().y
		for agent in self.agents:
			agent.set_start(idx)

	def set_target(self, idx):
		'''Set the target box based on its index idx value. '''
		# remove any existing target node, set new target node
		if self.start == self.boxes[idx]:
			print("Can't have the same start and end boxes!")
			return
		self.target = self.boxes[idx]
		self.target_marker.x = self.target.center().x
		self.target_marker.y = self.target.center().y
		for agent in self.agents:
			agent.set_target(idx)

	def plan_path(self):
		'''Conduct a nav-graph search from the current world start node to the
		current target node, using a search method that matches the string
		specified in `search`.
		'''
		for l in self.render_path:
			try:
				l.delete() #pyglets l.delete method is slightly broken
			except:
				pass
		for l in self.render_tree:
			try:
				l.delete() 
			except:
				pass
		for l in self.render_open_nodes:
			try:
				l.delete() 
			except:
				pass
		for a in self.agents:
			a.reset()
			a.plan_path()
			self.render_path.append(a.render_path)
			self.render_tree.append(a.render_tree)
			self.render_open_nodes.append(a.render_open_nodes)
	
	def update(self):
		for l in self.render_agents:
			try:
				l.delete() 
			except:
				pass
		for a in self.agents:
			a.update()
			self.render_agents.append(a.render_agents)



	@classmethod
	def FromFile(cls, filename ):
		'''Support a the construction of a BoxWorld map from a simple text file.
		See the module doc details at the top of this file for format details.
		'''
		# open and read the file
		f = open(filename)
		lines = []
		for line in f.readlines():
			line = line.strip()
			if line and not line.startswith('#'):
				lines.append(line)
		f.close()
		# first line is the number of boxes width, height
		nx, ny = [int(bit) for bit in lines.pop(0).split()]
		# Create a new BoxWorld to store all the new boxes in...
		world = BoxWorld(nx, ny, window.width, window.height)
		# Get and set the Start and Target tiles
		s_idx, t_idx = [int(bit) for bit in lines.pop(0).split()]
		world.set_start(s_idx)
		world.set_target(t_idx)
		# Ready to process each line
		assert len(lines) == ny, "Number of rows doesn't match data."
		# read each line
		idx = 0
		for line in reversed(lines): # in reverse order
			bits = line.split()
			assert len(bits) == nx, "Number of columns doesn't match data."
			for bit in bits:
				bit = bit.strip()
				world.boxes[idx].set_type(bit)
				idx += 1
		world.reset_navgraph()
		return world