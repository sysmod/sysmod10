# Modified by: Spencer Borland (sborla@cs.mcgill.ca)
# Date: March, 2003
# Comments: Modified for the Statechart formalism
##############################################################################
# Author: Ernesto Posse
# Date:   June 4, 2002
# Module: devs_utils.py
# Description: A set of utilities used by the devs meta-model in ATOM3
# Functions provided:
#   isterminal(semantic_object)
#   get_node_parent(semantic_object)
#   midpoint(visual_obj1, visual_obj2)
#   create_connection(source, target, conn_type)
#   is_possible_sibling(obj1, obj2)
#   connection_class(semantic_obj1, semantic_obj2)
#   connect_to_node_parent(semantic_object)
#   recursive_apply(semantic_object, node_operation, connection_operation)
#   move_children(semantic_object)
#   init_box(visual_object)
#   move_to(visual_object, x, y)
#   getbbox(node_parent, canvas)
#   adjust_bbox(model, padx = 5, pady = 5, namepadx = 0, namepady = -7)
#   resize_to_default(visual_object)
#   set_visibility(visual_object)
#   show_links(settings_node, containment_class)
#   apply_visibility(settings_node, box_class)

from Basic           import *
from History         import *
from Orthogonal      import *
from Composite       import *
from contains        import *
from orthogonality   import *
from Hyperedge       import *
from ATOM3           import *

GF_COMPOSITE_TEXT    = "gf1"
GF_COMPOSITE_BOX     = "gf2"
GF_ORTHOGONAL_TEXT   = "gf1"
GF_ORTHOGONAL_BOX    = "gf5"
GF_HISTORY_STAR      = "gf2"
GF_BASIC_TEXT        = "gf1"
GF_BASIC_OVAL        = "gf3"

import traceback, pprint
def where():
	pprint.pprint(traceback.extract_stack())

###############################################################################
# Composite
###############################################################################
def Composite_DROP(self):
  parent = get_node_parent(self)
  if parent != None:
    adjust_bbox(parent.graphObject_)
  move_children(self)

def Composite_DRAG(self):
  self.initdrag = (self.graphObject_.x, self.graphObject_.y)

def Composite_MOVE(self):
  move_children(self)

def Composite_CREATE(self):
  self.root        = self.rootNode
  self.atom3i      = self.root.parent
  self.children    = []
  self.node_parent = None
  self.graphObject_.child_hyper_restore = {}
  is_default = self.is_default.getValue()[1]
  if is_default:
    set_box_outline(self.graphObject_, "DARKGREEN")
  else:
    set_box_outline(self.graphObject_, "DARKBLUE")

def Composite_Visual_EDIT(self):
	is_default = self.semanticObject.is_default.getValue()[1]
	if is_default: set_box_outline(self, "DARKGREEN")
	else: set_box_outline(self, "DARKBLUE")
	set_visibility(self)

def Composite_EDIT(self):
  pass

def Composite_Visual_CREATE(self):
  pass

###############################################################################
# Orthogonal
###############################################################################
def Orthogonal_DROP(self):
  parent = get_node_parent(self)
  if parent != None:
    adjust_bbox(parent.graphObject_)
  move_children(self)

def Orthogonal_DRAG(self):
  self.initdrag = (self.graphObject_.x, self.graphObject_.y)

def Orthogonal_MOVE(self):
  move_children(self)

def Orthogonal_CREATE(self):
  self.root        = self.rootNode
  self.atom3i      = self.root.parent
  self.children    = []
  self.node_parent = None
  self.graphObject_.child_hyper_restore = {}
  init_box(self.graphObject_)

def Orthogonal_EDIT(self):
  set_visibility(self.graphObject_)

###############################################################################
# Basic
###############################################################################
def Basic_DROP(self):
  parent = get_node_parent(self)
  if parent != None:
    adjust_bbox(parent.graphObject_)

def Basic_MOVE(self):
  delta = (self.graphObject_.x - self.initdrag[0], self.graphObject_.y - self.initdrag[1])
  move_reflexive_links(self, delta[0], delta[1])
  self.initdrag = (self.initdrag[0]+delta[0], self.initdrag[1]+delta[1])

def Basic_DRAG(self):
  self.initdrag = (self.graphObject_.x, self.graphObject_.y)

def Basic_CREATE(self):
  self.root        = self.rootNode
  self.atom3i      = self.root.parent
  self.children    = []
  self.node_parent = None

def Basic_Visual_EDIT_CREATE(self):
  is_default = self.semanticObject.is_default.getValue()[1]
  if is_default: set_box_outline(self, "DARKGREEN")
  else: set_box_outline(self, "DARKBLUE")

###############################################################################
# History
###############################################################################
def History_DROP(self):
  parent = get_node_parent(self)
  if parent != None:
    adjust_bbox(parent.graphObject_)

def History_MOVE(self):
  pass
#  parent = get_node_parent(self)
#  if parent != None:
#    adjust_bbox(parent.graphObject_)

def History_DRAG(self):
  self.initdrag = (self.graphObject_.x, self.graphObject_.y)

def History_CREATE(self):
  self.root        = self.rootNode
  self.atom3i      = self.root.parent
  self.children    = []
  self.node_parent = None

def History_Visual_EDIT_CREATE(self):
  is_default = self.semanticObject.is_default.getValue()[1]
  star = self.semanticObject.star.getValue()[1]
  if is_default: set_box_outline(self, "DARKGREEN")
  else: set_box_outline(self, "DARKBLUE")
  if star: getattr(self,GF_HISTORY_STAR).setVisible(1)
  else: getattr(self,GF_HISTORY_STAR).setVisible(0)

###############################################################################
# visual_settings
###############################################################################
def visual_settings_EDIT_CREATE(self):
  self.rootNode.visual_settings = self
  show_links(self, contains)
  show_links(self, orthogonality)
  show_links(self, Hyperedge)
  apply_visibility(self, Composite)
  #apply_visibility(self, History)
  #apply_visibility(self, Basic)

###############################################################################
# contains
###############################################################################
def contains_DELETE(self):
  delete_connection(self)

def contains_CREATE(self):
  self.root = self.rootNode
  self.atom3i = self.root.parent
  self.node_parent = None
  #place_connection(self)
  show_link(self)

def contains_CONNECT(self):
  establish_containment_connection(self)
  #place_connection(self)
  show_link(self)

###############################################################################
# Hyperedge
###############################################################################
def Hyperedge_DELETE(self):
	pass

def Hyperedge_CONNECT(self):
  establish_peer_connection(self)
#  place_connection(self)
  show_link(self)
  Hyperedge_DROP(self)

def Hyperedge_CREATE(self):
  self.root = self.rootNode
  self.atom3i = self.root.parent
  self.node_parent = None
  Hyperedge_DROP(self)

def Hyperedge_DROP(self):
	adjacent_nodes = []
	adjacent_nodes += self.out_connections_
	adjacent_nodes += self.in_connections_
	if len(adjacent_nodes) == 0: return
	the_parent = get_node_parent(adjacent_nodes[0])
	for node in adjacent_nodes:
		parent = get_node_parent(node)
		if is_parent(parent, the_parent):
			the_parent = parent
	if the_parent != None:
		adjust_bbox(the_parent.graphObject_)

def Hyperedge_MOVE(self):
	pass

###############################################################################
# orthogonality
###############################################################################
def orthogonality_DELETE(self):
	pass

def orthogonality_CREATE(self):
	self.root = self.rootNode
	self.atom3i = self.root.parent
	self.node_parent = None

	place_connection(self)
	show_link(self)

def orthogonality_CONNECT(self):
	establish_containment_connection(self)
	place_connection(self)
	show_link(self)

###############################################################################
# genRTpythonDEVS
# called when the button "pythonDEVS-RT" is clicked
###############################################################################
def gen_pythonDEVSRT(self):
  import gen_code
  top_level_nodes = top_nodes(self.ASGroot)
  gen_code.Statechart2DEVS(top_level_nodes)

def is_parent(parent, child):
	if parent == child: return 0
	current = child
	while current != None:
		if current == parent: return 1
		current = get_node_parent(current)
	return 0

# adjust_bbox adjusts the bounding box of a model depending on its children.
# Assumes that model is a semantic object.
# SB: optimizations
def adjust_bbox(visual_object, padx=5, pady=5, namepadx=0, namepady=-7):
	canvas = visual_object.dc
	to_move = associate_links_with_connectors(visual_object)
	bbox = getbbox(visual_object)
	coords = (bbox[0]-padx, bbox[1]-pady, bbox[2]+padx, bbox[3]+pady)
	if isinstance(visual_object, graph_Composite):
		canvas.coords(getattr(visual_object,GF_COMPOSITE_BOX).handler, coords)
		canvas.coords(getattr(visual_object,GF_COMPOSITE_TEXT).handler, coords[0], coords[1]-7)
	else:
		canvas.coords(getattr(visual_object,GF_ORTHOGONAL_BOX).handler, coords)
		canvas.coords(getattr(visual_object,GF_ORTHOGONAL_TEXT).handler, coords[0], coords[1]-7)
	point = [coords[0], (coords[1]+coords[3])/2]
	canvas.coords(visual_object.connectors[0], tuple(point+point))
	point = [coords[2], (coords[1]+coords[3])/2]
	canvas.coords(visual_object.connectors[1], tuple(point+point))
	point = [(coords[0]+coords[2])/2, coords[1]]
	canvas.coords(visual_object.connectors[2], tuple(point+point))
	point = [(coords[0]+coords[2])/2, coords[3]]
	canvas.coords(visual_object.connectors[3], tuple(point+point))
	# adjust links which point to connectors
	move_links_to_connectors(visual_object, to_move)
	# may need to adjust parent contours
	node_parent = get_node_parent(visual_object.semanticObject)
	if node_parent != None and get_class_name(node_parent) != 'ATOM3':
		adjust_bbox(node_parent.graphObject_, padx, pady, namepadx, namepady)

# SB: added the following 2 methods to account for the fact that
# there is NO WAY to find out what link in connected to what connector!!!
def associate_links_with_connectors(g):
	canvas = g.dc
	associated = []
	from graphLink import graphLink
	for l in g.connections:
		con, order, sobj, lobj, obj = l
		if isinstance(obj, graphLink):
			for out_con in obj.out_connections_:
				out_con_handle = out_con[0]
				out_coords = canvas.coords(out_con_handle)
				for connector_handle in g.connectors:
					connector_coords = canvas.coords(connector_handle)
					if connector_coords[0] == out_coords[0] and connector_coords[1] == out_coords[1]:
						associated.append((out_con_handle, connector_handle))
				for in_con in obj.in_connections_:
					in_con_handle = in_con[0]
					in_coords = canvas.coords(in_con_handle)
					for connector_handle in g.connectors:
						connector_coords = canvas.coords(connector_handle)
						if connector_coords[0] == in_coords[0] and connector_coords[1] == in_coords[1]:
							associated.append((in_con_handle, connector_handle))
	return associated

def move_links_to_connectors(g, to_move):
	canvas = g.dc
	for connection_handle, connector_handle in to_move:
		connector_coords = canvas.coords(connector_handle)
		connection_coords = canvas.coords(connection_handle)
		new_coords = tuple([connection_handle, connector_coords[0], connector_coords[1]] + connection_coords[2:])
		apply(canvas.coords, new_coords)

# apply_visibility applies the visibility settings to boxes.
# Note!: It might not redraw things correctly. It depends on the order
# of appearance on the root's list of nodes for the given class.
def apply_visibility(settings_node, box_class):
  root = settings_node.rootNode
  for box_object in root.listNodes[box_class.__name__]:
    set_visibility(box_object.graphObject_)

# broadcast_containment_connection receives a parent and a child and  
# creates the same connection for all the siblings of the child that do not
# have a parent.
# It is intended only for setting an atomic_devs as the common
# parent of a family of states. Ports and coupled_devs are ignored.
# Entities and relations that already have a parent are ignored.
def broadcast_containment_connection2(node_parent, child):
  def broadcast(entity, visited):
    if entity in visited:
      return visited
    if entity.node_parent == None:
      relation = create_connection(node_parent,
                                   entity,
                                   containment_connection_class(node_parent,entity))
      set_parent_child_relation(node_parent, entity, relation)
    visited = visited+[entity]
    for relation in entity.out_connections_:
      if not is_containment_relation(relation):
        if relation.node_parent == None or not is_legal(relation.node_parent):
          relation.node_parent = node_parent
          if relation not in node_parent.children:
            node_parent.children.append(relation)
        for sibling in relation.out_connections_:
          visited = broadcast(sibling, visited)
    for relation in entity.in_connections_:
      if relation.node_parent == None or not is_legal(relation.node_parent):
        relation.node_parent = node_parent
        if relation not in node_parent.children:
          node_parent.children.append(relation)
      if not is_containment_relation(relation):
        for sibling in relation.in_connections_:
          visited = broadcast(sibling, visited)
    return visited
  if node_parent != None:
    broadcast(child, [])

# SB
# new broadcast_containment_connection which sets the parent of link
# iff two nodes have the same parent  
def broadcast_containment_connection(node_parent, child):
  def broadcast(the_parent, entity):
    for relation in entity.out_connections_:
        for sibling in relation.out_connections_:
          if sibling.node_parent == the_parent:
            relation.node_parent = node_parent
            if relation not in node_parent.children:
              node_parent.children.append(relation)
    for relation in entity.in_connections_:
      if not is_containment_relation(relation):
        for sibling in relation.in_connections_:
          if sibling.node_parent == the_parent:
            relation.node_parent = node_parent
            if relation not in node_parent.children:
              node_parent.children.append(relation)
  if node_parent != None:
    broadcast(node_parent, child)

# connect_to_node_parent appends a node to the parent's list of children. If the
# given node has not explicitely been connected to the parent, it looks in
# the siblings for a parent, if any.
def connect_to_node_parent(entity):
  node_parent = get_node_parent(entity)
  if node_parent != None:
    set_parent_child_relation(node_parent, entity)
    adjust_bbox(node_parent.graphObject_)
  else:
    node_parent = get_siblings_parent(entity)
    if node_parent != None:
      relation = create_connection(node_parent,
                                   entity,
                                   containment_connection_class(node_parent, entity))
      set_parent_child_relation(node_parent, entity, relation)
      adjust_bbox(node_parent.graphObject_)

# connection_class returns the type of connection allowed between two
# given semantic objects. It returns the class.
def connection_class(semantic_obj1, semantic_obj2):
  relations = { 
                (Composite, Composite):       Hyperedge,
                (Composite, Composite):       contains,
                (Composite, Orthogonal):      contains,
                (Orthogonal, Composite):      contains,
                (Basic, Composite):           Hyperedge,
                (History, Composite):         Hyperedge,
                (Composite, Basic):           Hyperedge,
                (Composite, History):         Hyperedge
              }
  return relations[(get_class(semantic_obj1), get_class(semantic_obj2))]

# containment_connection_class returns the type of the containment connection
# allowed between two given semantic objects. It returns the class.
def containment_connection_class(semantic_obj1, semantic_obj2):
  relations = { 
                (Composite, Basic):           contains,
                (Composite, Composite):       contains,
                (Composite, History):         contains,
                (Composite, Orthogonal):      orthogonality,
                (Orthogonal, Composite):      contains,
                (Orthogonal, Basic):          contains,
                (Orthogonal, History):        contains
              }
  return relations[(get_class(semantic_obj1), get_class(semantic_obj2))]

# create_connection creates a new link between a given source and target, of
# a given connection type 'conn_type'. Returns the newly created connection.
def create_connection(source, target, conn_type):
  root   = source.rootNode
  atom3i = root.parent
  canvas = atom3i.UMLmodel
  # Check global preconditions
  atom3i.globalPrecondition(root)
  # Create semantic object for the connection/link/relation
  conn_object = conn_type(atom3i)
  # Obtain the class of visual objects of type 'conn_type', i.e. 'graph_<conn_type>'
  graph_conn_type_name = "graph_"+conn_type.__name__
  exec "from "+graph_conn_type_name+" import *" in atom3i.__dict__
  graph_conn_type = eval(graph_conn_type_name)
  # Assign the visual type to the semantic object
  conn_object.graphClass_ = graph_conn_type
  # Draw connection if graphics are enabled
  if atom3i.genGraphics:
    mid = midpoint(source.graphObject_, target.graphObject_)
    new_graph_obj = graph_conn_type(mid[0], mid[1], conn_object)
    new_graph_obj.DrawObject(canvas)
    canvas.addtag_withtag(get_class_name(conn_object), new_graph_obj.tag)
  else: new_graph_obj = None
  conn_object.graphObject_ = new_graph_obj
  # Add semantic object to the instance of atom3 and to the ASG root  
  atom3i.conn_object       = conn_object   # This might cause a bug!
  root.addNode(conn_object)
  # Check global postconditions
  atom3i.globalAndLocalPostcondition(conn_object, root)
  # Create semantic connection between source and target in the ASG, and
  # draw it in the canvas. (Note: drawConnections does both)
  source_vertex = source.graphObject_.getCoordsVertex()
  target_vertex = target.graphObject_.getCoordsVertex()
  interpoints1 = [source_vertex[0], source_vertex[1], mid[0], mid[1]]
  interpoints2 = [mid[0], mid[1], target_vertex[0] ,target_vertex[1]]
  temp_obj_from = atom3i.sem_objFrom
  temp_obj_to   = atom3i.sem_objTo
  atom3i.sem_objFrom = None
  atom3i.sem_objTo   = None
  atom3i.drawConnections((source, conn_object, interpoints1, 0, 2),
                         (conn_object, target, interpoints2, 0, 2))
  atom3i.sem_objFrom = temp_obj_from
  atom3i.sem_objTo   = temp_obj_to
  return conn_object

# delete_connection deletes a connection/link/relation, by updating
# the source's children list
def delete_connection(semantic_connection):
  if is_containment_relation(semantic_connection):
    targets = get_targets(semantic_connection)
    for target in targets:
      reset_parent_child_relation(target)

# do_nothing
def do_nothing(x):
  pass

# dynamic_adjust takes an entity and if it already has a parent,
# automatically adjusts the parent's bounding box. Otherwise, if it
# overlaps 
def dynamic_adjust(semantic_object):
  node_parent = get_node_parent(self)
  if node_parent != None:
    adjust_bbox(node_parent.graphObject_)
  else:
    if overlap(self, node_parent):
      if self not in node_parent.children:
        node_parent.children.append(self)
      create_connection(node_parent, self, contains_state)
      adjust = node_parent.auto_adjust.getValue()[1]
      if adjust:
        adjust_bbox(node_parent.graphObject_)

# establish_containment_connection(l) sets up a connection l,
# if l is a containment relation that has source and target, 
# and then broadcasts it to all of the target's siblings.
def establish_containment_connection(link):
  if is_fully_specified_relation(link) :
    source  = get_source(link)
    targets = get_targets(link)
    target  = targets[0]
    for node in targets:
      if node == link.atom3i.sem_objTo:
        target = node
        break
    if is_legal_containment_relation(source, target, link):
      set_parent_child_relation(source, target, link)
      broadcast_containment_connection(source, target)
      adjust_bbox(source.graphObject_)

# establish_peer_connection(l) sets up a connection l
# if l has source or target, sets its parent to
def establish_peer_connection(link):
  if is_fully_specified_relation(link):
    source  = get_source(link)
    targets = get_targets(link)
    target  = None
    for node in targets:
      if link.atom3i.sem_objTo == node:
        target = node
        break
    if target != None:  # because when loading behaviour is different.
      node_parent = get_node_parent(link)
      set_parent_child_relation(node_parent, link)
# SB: the following line is removed to allow interlevel transitions
#      broadcast_containment_connection(get_node_parent(source), source)

def find_default(root):
  histories = root.listNodes['History']
  composites = root.listNodes['Composite']
  basics = root.listNodes['Basic']
  orthogonals = root.listNodes['Orthogonal']
  default_node = None
  for node in histories+composites+basics+orthogonals:
    default = node.is_default.getValue()[1]
    if default:
      default_node = node
      break
  return default_node

def has_parent(node):
  for t in node.in_connections_:
    if isinstance(t, contains) or isinstance(t, orthogonality):
      return 1
  return 0

def has_incoming(node):
  for t in node.in_connections_:
    if isinstance(t, Hyperedge):
      return 1
  return 0

def top_nodes(root):
  histories = root.listNodes['History']
  composites = root.listNodes['Composite']
  basics = root.listNodes['Basic']
  orthogonals = root.listNodes['Orthogonal']
  all  = histories+composites+basics+orthogonals
  top_level_nodes = []
  for node in all:
    if not has_parent(node):
#      if node.is_default.getValue()[1] or not has_incoming(node):
      top_level_nodes.append(node)
  return top_level_nodes

# find_root looks at all the nodes in the graph and choses the one which is
# supposed to be the root. If there is more than one root or no nodes,
# a message is printed on the console
def find_root(root):
  coupled_models = root.listNodes['coupled_devs']
  atomic_models  = root.listNodes['atomic_devs']
  roots = []
  for node in coupled_models + atomic_models:
    parent = get_node_parent(node)
    if parent == None:
      roots.append(node)
  if roots == []:
    print "There is no root!"
  elif len(roots) > 1:
    print "There is more than one root!"
  if roots != []:
    return roots[0]
  return None

# get_box_coords returns the visual_entity's current box as a 4-tuple
# (not to be confused with the bounding box of its contents). 
def get_box_coords(visual_entity):
  semantic_object = visual_entity.semanticObject
  box = None
  if is_entity(semantic_object):
    for gf in visual_entity.graphForms:
      if gf.elementType == "rectangle":
        box = gf.getCoords()
        break
  return box

# get_box_fill returns the entity's box's current fill color.
def get_box_fill(visual_entity):
  semantic_object = visual_entity.semanticObject
  color = None
  if is_entity(semantic_object) and not is_terminal(semantic_object):
    canvas = visual_entity.dc
    for gf in visual_entity.graphForms:
      if gf.elementType == "rectangle":
        color = canvas.itemcget(gf.handler, "fill")
        break
  return color

# get_box_outline returns the entity's box's current border color.
def get_box_outline(visual_entity):
  semantic_object = visual_entity.semanticObject
  color = None
  if is_entity(semantic_object) and not is_terminal(semantic_object):
    canvas = visual_entity.dc
    for gf in visual_entity.graphForms:
      if gf.elementType == "rectangle":
        color = canvas.itemcget(gf.handler, "outline")
        break
  return color

# getbbox returns the bounding box of the objects inside a given semantic
# object in the given canvas.
def getbbox(visual_object):
  minx, miny, maxx, maxy = 10000, 10000, -10000, -10000
  canvas = visual_object.dc
  visible_graph_forms = filter(lambda gf: not gf.hidden,
                               get_child_gforms(visual_object))
  visible_segments = filter(lambda s: is_segment_visible(s, canvas),
                            get_child_link_segments(visual_object))
  visible_connectors = filter(lambda c: is_connector_visible(c, canvas),
                              get_child_connectors(visual_object))
  for grform in visible_graph_forms:
    bbx = canvas.bbox(grform.handler)
    if bbx:
      if bbx[0] < minx: minx = bbx[0]
      if bbx[1] < miny: miny = bbx[1]
      if bbx[2] > maxx: maxx = bbx[2]
      if bbx[3] > maxy: maxy = bbx[3]
# SB: commented out 7 lines below to avoid weird resizing of bbox
  for segment in visible_segments:
    bbx = canvas.bbox(segment)
    if bbx:
      if bbx[0] < minx: minx = bbx[0]
      if bbx[1] < miny: miny = bbx[1]
      if bbx[2] > maxx: maxx = bbx[2]
      if bbx[3] > maxy: maxy = bbx[3]
  for connector in visible_connectors:
    bbx = canvas.bbox(connector)
    if bbx:
      if bbx[0] < minx: minx = bbx[0]
      if bbx[1] < miny: miny = bbx[1]
      if bbx[2] > maxx: maxx = bbx[2]
      if bbx[3] > maxy: maxy = bbx[3]
  default_width = get_visual_setting(visual_object, "default_width")
  default_height = get_visual_setting(visual_object, "default_height")
  if (minx + default_width) > maxx:  maxx = minx + default_width
  if (miny + default_height) > maxy: maxy = miny + default_height
  if visible_graph_forms + visible_segments + visible_connectors == []:
    prefix = visual_object.tag+"."
    if isinstance(visual_object, graph_Composite):
      current_bbox = canvas.coords(getattr(visual_object, GF_COMPOSITE_BOX).handler)
    else:
      current_bbox = canvas.coords(getattr(visual_object, GF_ORTHOGONAL_BOX).handler)
    minx, miny = current_bbox[0], current_bbox[1]
    maxx = minx + default_width
    maxy = miny + default_height
  return (minx, miny, maxx, maxy)

# get_child_gforms returns all of the graphical forms of the given node
def get_child_gforms(visual_object, deep = 1):
  canvas = visual_object.dc
  semantic_object = visual_object.semanticObject
  def get_node_gforms(node):
    if node != semantic_object:
      if is_entity(node):
        return node.graphObject_.graphForms
      elif is_link(node) and not is_containment_relation(node):
        gforms = []
        link_color = get_visual_setting(node.graphObject_, "color")
        if node.graphObject_.centerObject:
          gforms = gforms + node.graphObject_.centerObject.graphForms
        for ic in node.graphObject_.in_connections_:
          handler, tag, seg_obj, link_obj = ic
          if seg_obj:
            gforms = gforms + seg_obj.graphForms
          if link_obj:
            gforms = gforms + link_obj.graphForms
##           segment = GraphicalForm(canvas, handler, 'insegment_'+tag)
##           segment.Color = link_color
##           gforms.append(segment)
        for oc in node.graphObject_.out_connections_:
          handler, tag, seg_obj, link_obj = oc
          if seg_obj:
            gforms = gforms + seg_obj.graphForms
          if link_obj:
            gforms = gforms + link_obj.graphForms
##           segment = GraphicalForm(canvas, handler, 'outsegment_'+tag)
##           segment.Color = link_color
##           gforms.append(segment)
        return gforms
  return reduce(lambda x,y: x+y,
                filter(lambda x: x != None,
                       recursive_get(semantic_object,
                                     get_node_gforms,
                                     deep).values()),
                [])
                

# get_child_connectors(visual_object) returns all the children's connectors
def get_child_connectors(visual_object, deep = 1):
  canvas = visual_object.dc
  semantic_object = visual_object.semanticObject
  def get_node_connectors(node):
    if node != semantic_object:
      if is_entity(node):
        return node.graphObject_.connectors
      elif is_link(node) and not is_containment_relation(node):
        connectors = []
        if node.graphObject_.centerObject:
          connectors = connectors + node.graphObject_.centerObject.connectors
        for ic in node.graphObject_.in_connections_:
          handler, tag, seg_obj, link_obj = ic
          if seg_obj:
            connectors = connectors + seg_obj.connectors
          if link_obj:
            connectors = connectors + link_obj.connectors
        for oc in node.graphObject_.out_connections_:
          handler, tag, seg_obj, link_obj = oc
          if seg_obj:
            connectors = connectors + seg_obj.connectors
          if link_obj:
            connectors = connectors + link_obj.connectors
        return connectors
  return reduce(lambda x,y: x+y,
                filter(lambda x: x != None,
                       recursive_get(semantic_object,
                                     get_node_connectors,
                                     deep).values()),
                [])

def get_children(visual_entity):
	children = []
	semantic_obj = visual_entity.semanticObject
	for connected in semantic_obj.out_connections_:
		if isinstance(connected, contains):
			if len(connected.out_connections_) <= 0: continue
			child = connected.out_connections_[0]
			children.append(child)
	return children

# get_child_link_segments
def get_child_link_segments(visual_object, deep = 1):
	children = get_children(visual_object)
	def get_node_link_segments(node):
		if is_link(node):
			# check sources and destinations
			for source in node.in_connections_:
				if source not in children: return []
			for destination in node.out_connections_:
				if destination not in children: return []
			return get_link_segments(node.graphObject_)
	return reduce(lambda x, y: x+y,filter(lambda x: x != None,recursive_get(visual_object.semanticObject,get_node_link_segments,deep).values()),[])

# get_class(object) returns the python class of the object.
def get_class(object):
  return object.__class__

# get_class_name(object) returns the name of the python class of the object.
def get_class_name(object):
  return object.__class__.__name__

# get_default_size returns the default size of a visual_object
def get_default_size(visual_object):
  width  = get_visual_setting(visual_object, "default_width")
  height = get_visual_setting(visual_object, "default_height")
  return (width, height)

# get_link_segments
def get_link_segments(visual_link):
  return map(lambda entry: entry[0], visual_link.in_connections_ + visual_link.out_connections_)

# get_node_parent gets the parent (duh!) of a given semantic object, bypassing
# the relation to the parent; i.e. for a state, finds the atomic devs to
# which it belongs, and for an atomic devs or coupled devs, finds the
# coupled devs it belongs to, if any.
def get_node_parent(semantic_object):
  try:
    if semantic_object.node_parent != None and is_legal(semantic_object.node_parent):
      return semantic_object.node_parent
  except AttributeError:
    pass
  node_parent = None
  if is_entity(semantic_object):
    node_parent = lookup_entitys_parent(semantic_object)
  elif is_link(semantic_object):
    node_parent = lookup_links_parent(semantic_object)
  return node_parent

# get_siblings_parent returns the parent of a possible sibling of the given
# semantic object.
def get_siblings_parent(entity):
  node_parent = None
  found = 0
  for relation in entity.in_connections_:
    try:
      if not is_containment_relation(relation):
        related_object = relation.in_connections_[0]
        if is_possible_sibling(related_object, entity):
          node_parent = get_node_parent(related_object)
          if node_parent != None and node_parent != entity:
            found = 1 
            break
    except IndexError:
      pass
  if not found:
    for relation in entity.out_connections_:
      try:
        if not is_containment_relation(relation):
          related_object = relation.out_connections_[0]
          if is_possible_sibling(related_object, entity):
            node_parent = get_node_parent(related_object)
            if node_parent != None and node_parent != entity:
              found = 1
              break
      except IndexError:
        pass
  return node_parent

# get_source(r) returns the source of a given relation. It assumes the
# relation to be fully specified.
def get_source(relation):
  try:
    return relation.in_connections_[0]
  except IndexError:
    return None

# get_sourceget_targets(r) returns the target of a given relation. It assumes
# the relation to be fully specified.
def get_target(relation):
  try:
    return relation.out_connections_[0]
  except IndexError:
    return None

# get_sourceget_targets(r) returns the targets of a given relation. It assumes
# the relation to be fully specified.
def get_targets(relation):
  return relation.out_connections_

# get_text_coords returns the entity's text's coords. 
def get_text_coords(visual_entity):
  semantic_object = visual_entity.semanticObject
  pos = None
  if is_entity(semantic_object):
    for gf in visual_entity.graphForms:
      if gf.elementType == "text":
        pos = gf.getCoords()
        break
  return pos

# get_text_fill returns the entity's text's a fill color.
def get_text_fill(visual_entity):
  semantic_object = visual_entity.semanticObject
  color = None
  if is_entity(semantic_object):
    canvas = visual_entity.dc
    for gf in visual_entity.graphForms:
      if gf.elementType == "text":
        color = canvas.itemcget(gf.handler, "fill")
        break
  return color

# get_visual_setting returns the specified setting (a string) for the object.
# Settings are: color, width, height, and their availability depends on the
# type of object.
def get_visual_setting(visual_object, setting):
  def boolean_attribute(a):
    return a == "visible" or a == "links_visible"
  root = visual_object.semanticObject.rootNode
  class_name = get_class_name(visual_object.semanticObject)
  try:
    visual_settings = root.visual_settings
    setting_value = eval("visual_settings."+class_name+"_"+setting+".getValue()")
    if boolean_attribute(setting): return setting_value[1]
    return setting_value
  except AttributeError:
    map = { 
            'contains_color':                    'pink',
            'Composite_default_width':           50.0,
            'Composite_default_height':          50.0,
            'Orthogonal_default_width':          50.0,
            'Orthogonal_default_height':         50.0,
            'contains_links_visible':            ('',0),
            'orthogonality_links_visible':       ('',0),
            'orthogonality_color':               'lightblue',
            'Hyperedge_links_visible':           ('',1),
            'Hyperedge_color':                   'darkblue',
            'Composite_color':                   'lightgray',
            'Orthogonal_color':                  'lightgray'
          }
    setting_value = map[(class_name+"_"+setting)]
    if boolean_attribute(setting):
      return setting_value[1]
    return setting_value

# has_children(entity)
def has_children(entity):
  for child in entity.children:
    if is_entity(child):
      return 1
  return 0

def get_child_hyperedges(visual_entity):
  def __get_connected_hyperedges(entity):
    visual_entity = entity.graphObject_
    hyperedges = []
    for connection in visual_entity.connections:
      handle, direction, a, b, obj = connection
      if isinstance(obj, graph_Hyperedge):
        hyperedges.append((handle, obj))
    return hyperedges
  def __get_child_hyperedges(visual_entity, handles=[]):
    children = get_all_children(visual_entity)
    all_hyperedges = []
    for child in children:
#      if not is_visible(child.graphObject_): continue
      hyperedges = __get_connected_hyperedges(child)
      all_hyperedges += hyperedges
    return all_hyperedges
  return __get_child_hyperedges(visual_entity, [])

def get_all_children(visual_entity):
  children = []
  semantic_obj = visual_entity.semanticObject
  for connected in semantic_obj.out_connections_:
    if is_containment_relation(connected):
      if len(connected.out_connections_) == 0: continue
      child = connected.out_connections_[0]
      children.append(child)
      if not is_terminal(child):
        children += get_all_children(child.graphObject_)
  return children

def get_connected_entities(hyperedge):
  def __get_connected_entities(hyperedge):
    hyper = hyperedge.semanticObject
    entities = []
    entities += hyper.in_connections_ + hyper.out_connections_
    return entities
  if not isinstance(hyperedge, graph_Hyperedge): return []
  else:
    return __get_connected_entities(hyperedge)

def set_segment_point(handle, canvas, point):
  coords = canvas.coords(handle)
  coords[0], coords[1] = point[0], point[1]
  apply(canvas.coords, tuple([handle] + coords))

def hide_interior(visual_entity):
  semantic_object = visual_entity.semanticObject
  canvas = visual_entity.dc
  color = get_visual_setting(visual_entity, "color")
  for gform in get_child_gforms(visual_entity, deep=1):
    gform.setVisible(None)
  for connector in get_child_connectors(visual_entity, deep=1):
    make_connector_invisible(connector, canvas)
  hyper_tuples = get_child_hyperedges(visual_entity)
  children = get_all_children(visual_entity)
  #visual_entity.child_hyper_restore = {}
  new_coords = get_box_coords(visual_entity)
  midx = ((new_coords[2]-new_coords[0])/2) + new_coords[0]
  midy = ((new_coords[3]-new_coords[1])/2) + new_coords[1]
  for handle,hyper_obj in hyper_tuples:
    entities = get_connected_entities(hyper_obj)
    hide = 1
    for entity in entities:
      if entity not in children:
        hide = 0
        break
    if hide:
      make_segment_invisible(handle, canvas)
    else:
      coords = canvas.coords(handle)
      if not visual_entity.child_hyper_restore.has_key(handle):
        visual_entity.child_hyper_restore[handle] = (coords[0]-midx, coords[1]-midy)
      set_segment_point(handle, canvas, (midx,midy))
      set_link_visibility(hyper_obj.semanticObject, 1)
  set_box_fill(visual_entity, color)

# indent(n) returns a string of n spaces; it is used for pretty printing.
def indent(n):
  s = ""
  for i in range(n):
    s = s + " "
  return s

# init_box adds a "box" tag to all boxes in an object's appearance, and a
# "name" tag to all names.
# The argument is expected to be of class graphEntity.
def init_box(visual_object):
  prefix = visual_object.tag+"."
  canvas = visual_object.dc
  box    = []
  width  = get_visual_setting(visual_object, "default_width")
  height = get_visual_setting(visual_object, "default_height")
  visual_object.last_dims = (width, height)
  visual_object.scale     = (1.0, 1.0)
  for gform in visual_object.graphForms:
    if gform.elementType == "rectangle":
      existing_tags = list(canvas.gettags(gform.handler))
      canvas.itemconfig(gform.handler,
                        tags = tuple(existing_tags + [prefix+"box"]))
      adjust_bbox(visual_object)
    elif gform.elementType == "text":
      existing_tags = list(canvas.gettags(gform.handler))
      canvas.itemconfig(gform.handler,
                        tags = tuple(existing_tags + [prefix+"name"]))
  for conn_handler in visual_object.connectors:
    existing_tags = list(canvas.gettags(conn_handler))
    canvas.itemconfig(conn_handler,
                      tags = tuple(existing_tags + [prefix+"conn"]))
  save_appearance(visual_object)

# init_circle saves the circle's default size in the object and marks it with
# an "oval" tag
def init_circle(visual_object):
  prefix = visual_object.tag+"."
  canvas = visual_object.dc
  for gform in visual_object.graphForms:
    if gform.elementType == "oval":
      existing_tags = list(canvas.gettags(gform.handler))
      canvas.itemconfig(gform.handler,
                        tags = tuple(existing_tags + [prefix+"oval"]))
      box = canvas.coords(gform.handler)
      visual_object.last_dims = (box[2] - box[0], box[3] - box[1])
      visual_object.scale = (1.0, 1.0)
      break

# is_connector_visible(connector_handler, canvas)
def is_connector_visible(connector_handler, canvas):
  fill = canvas.itemcget(connector_handler, "fill")
  outline = canvas.itemcget(connector_handler, "outline")
  return fill != "" or outline != ""

# is_containment_relation returns 1 if the given semantic object is a
# link with ype contains_<x> where <x> is in {state, model,
def is_containment_relation(relation):
  return isinstance(relation, contains) or isinstance(relation, orthogonality)

# is_entity
def is_entity(semantic_object):
  return isinstance(semantic_object, Composite) or isinstance(semantic_object, Basic) or isinstance(semantic_object, History) or isinstance(semantic_object, Orthogonal)

# is_fully_specified_relation(r) returns true if the link r has both
# an incomming connection and at least one outgoing connection.
def is_fully_specified_relation(relation):
  return len(relation.in_connections_) == 1 and len(relation.out_connections_) >= 1

# is_legal returns true is the argument is a legal Statechart entity
def is_legal(entity):
  return isinstance(entity, Composite) or isinstance(entity, Basic) or isinstance(entity, History) or isinstance(entity, Orthogonal)

# is_legal_containment_relation(source, target, relation)
def is_legal_containment_relation(source, target, relation):
  return is_containment_relation(relation) and \
         isinstance(relation, containment_connection_class(source, target)) and \
         source != target

# is_link
def is_link(semantic_object):
  return isinstance(semantic_object, Hyperedge) or is_containment_relation(semantic_object)

# is_possible_sibling returns true if the two objects can be siblings;
# for instance, an atomic devs and a coupled devs, or two states.
# Counterexamples are states and atomic_devs.

def is_possible_sibling(obj1, obj2):
  if obj1 == obj2: return 0
  incompatible_types = [(atomic_devs, state),
                        (coupled_devs, state)]
  for incomp in incompatible_types:
    if isinstance(obj1, incomp[0]) and isinstance(obj2, incomp[1]):
      return 0
    elif isinstance(obj1, incomp[1]) and isinstance(obj2, incomp[0]):
      return 0
  return 1

# is_segment_visible returns tru if the fill of a segment is ""
def is_segment_visible(segment_handler, canvas):
  return canvas.itemcget(segment_handler, "fill") != ""

# is_terminal returns true (1) for entities that are not composite, i.e.
# states, and false (0) for composite entities, i.e. atomic_devs
# and coupled_devs models.
def is_terminal(semantic_object):
  return isinstance(semantic_object, Basic) or isinstance(semantic_object, History) or is_link(semantic_object)

# is_visible(visual_entity) returns true if its contents are visible.
def is_visible(visual_entity):
  return visual_entity.semanticObject.visible.getValue()[1]

# lookup_entitys_parent looks up for the parent of an entity in the graph.
def lookup_entitys_parent(entity):
  node_parent = None
  for relation in entity.in_connections_:
    if is_containment_relation(relation):
      try:
        node_parent = relation.in_connections_[0]
        if not is_terminal(node_parent):
          break
      except IndexError:
        pass
  return node_parent

# lookup_links_parent looks up for the parent of a link in the graph.
def lookup_links_parent(link):
  node_parent = None
  if is_containment_relation(link):
    try:
      node_parent = link.in_connections_[0]
    except IndexError:
      pass
  elif isinstance(link, Hyperedge):
    found = 0
    for source in link.in_connections_:
      node_parent = get_node_parent(source)
      if node_parent != None:
        found = 1
        break
    if not found:
      for target in link.out_connections_:
        node_parent = get_node_parent(target)
        if node_parent != None:
          break
  return node_parent

# make_connector_invisible(connector_handler, canvas)
def make_connector_invisible(connector_handler, canvas):
  canvas.itemconfigure(connector_handler, fill = "", outline = "")

# make_connector_invisible(connector_handler, canvas)
def make_connector_visible(connector_handler, canvas):
  canvas.itemconfigure(connector_handler, fill = "red", outline = "black")

# make_segment_invisible(segment_handler, canvas)
def make_segment_invisible(segment_handler, canvas):
  canvas.itemconfigure(segment_handler, fill = "")

# make_segment_invisible(segment_handler, canvas)
def make_segment_visible(segment_handler, color, canvas):
  canvas.itemconfigure(segment_handler, fill = color)

# midpoint takes two visual objects and returns the point in the middle of them
def midpoint(visual_obj1, visual_obj2):
  x0, y0 = visual_obj1.x, visual_obj1.y
  x1, y1 = visual_obj2.x, visual_obj2.y
  return (x0 + (x1-x0)/2, y0 + (y1-y0)/2)

# move_children moves all the graphical objects of all children of the given
# object. It assumes that the semantic object has an attribute initdrag,
# initialized by a drag event.
def move_children(entity):
  delta = (entity.graphObject_.x - entity.initdrag[0], entity.graphObject_.y - entity.initdrag[1])
  def move_node(node):
    if node != entity:
      if is_link(node):
        node.graphObject_.selectedHandler = node.graphObject_.ALL_SELECTED
      node.graphObject_.Move(delta[0], delta[1])
  recursive_apply(entity, move_node, do_nothing)
  move_reflexive_links(entity, delta[0], delta[1])
  entity.initdrag = (entity.initdrag[0]+delta[0], entity.initdrag[1]+delta[1])

# move_reflexive_links
# moves links if their sources and destinations are entity or entity's children
def move_reflexive_links(entity, delta_x, delta_y):
  if is_terminal(entity): all_children = []
  else: all_children = get_all_children(entity.graphObject_)
  for oc in entity.out_connections_:
    move = 1
    for source in oc.in_connections_:
      if source not in all_children+[entity]:
        move = 0
        break
    for destination in oc.out_connections_:
      if destination not in all_children+[entity]:
        move = 0
        break
    if move:
      oc.graphObject_.selectedHandler = graphLink.ALL_SELECTED
      oc.graphObject_.Move(delta_x, delta_y)

# move_to moves a visual object to an absolute position x,y on the canvas.
def move_to(visual_object, x, y):
  current_pos = (visual_object.x, visual_object.y)
  delta       = (x - current_pos[0], y - current_pos[1])
  if isinstance(visual_object, graphLink):
    visual_object.selectedHandler = visual_object.ALL_SELECTED
  visual_object.Move(delta[0], delta[1])

# place_connection(node) puts the connection 'node' in the middle between its
# parent and child.
# SB: this function is bad news... only re draws things after user has 
# carefully planned layout
def place_connection(node):
  if is_fully_specified_relation(node):
    x0, y0 = node.in_connections_[0].graphObject_.getCoordsVertex()
    x1, y1 = node.out_connections_[0].graphObject_.getCoordsVertex()
    x = x0 + (x1 - x0) / 2
    y = y0 + (y1 - y0) / 2
    move_to(node.graphObject_, x, y)

# place_containment_connection(node) puts the connection 'node' on
# the connector of the parent.
def place_containment_connection(node):
  x0, y0 = node.in_connections_[0].graphObject_.getCoordsVertex()
  move_to(node.graphObject_, x0, y0)

# recursive_apply applies an operation recursively to all children of a 
# composite entity, and their ourwards connections.
# It assumes that non-terminal nodes have an attribute 'children' which
# is a list of semantic objects.
# The arguments are the root of the composite entity, the operation to
# apply to the nodes, which must be able to receive the node as argument,
# and the operation to apply to connections, which must be able to receive
# the connection as argument.
# if deep if different to None or 0, the recursion will be done regardless
# of the visibility of composite models. If it is 0, models with hidden
# interiors (black boxes) will be treated as terminals in the recursion.
def recursive_apply(semantic_object, node_pre_operation, node_post_operation, deep = 1):
  def terminal(node):
    if deep:
      return is_terminal(node)
    else:
      if is_terminal(node):
        return 1
      else:
        return not node.visible.getValue()[1]
  # SB: added seen parameter 'seen' to avoid cycles
  def do_recursive_apply(node, ind=0, seen=[]):
    if not (node in seen):
      seen.append(node)
      node_pre_operation(node)
      if not terminal(node):
        for child in node.children:
            do_recursive_apply(child, ind+2, seen)
      node_post_operation(node)
  do_recursive_apply(semantic_object, 0, [])

# recursive_get gathers information recusrively from a node's components.
# It returns a dictionary indexed by the nodes. A common use is to call
# the "values" method on the dictionary to obtain a list of the values.
def recursive_get(semantic_object, node_get, deep = 1):
  def terminal(node):
    if deep:
      return is_terminal(node)
    else:
      if is_terminal(node):
        return 1
      else:
        return not node.visible.getValue()[1]
  def do_recursive_get(node, dict, ind = 0, seen = []):
    dict[node] = node_get(node)
    if not terminal(node):
      for child in node.children:
        if child not in seen:
          seen.append(child)
          dict = do_recursive_get(child, dict, ind+2, seen)
    return dict
  dict = {}
  dict = do_recursive_get(semantic_object, dict)
  return dict

# redraw_entity(entity) draws an entity and its children according to their
# visibility attribute
def redraw_entity(visual_entity):
  def restore_child_hypers(visual_entity):
    canvas = visual_entity.dc
    for handle in visual_entity.child_hyper_restore:
      x,y = visual_entity.child_hyper_restore[handle]
      coords = canvas.coords(handle)
      set_segment_point(handle, canvas, (coords[0]+x,coords[1]+y))
    visual_entity.child_hyper_restore = {}
  def redraw_node(node):
    if is_entity(node):
      set_entity_visibility(node, 1)
      if not is_terminal(node):
        set_entity_visibility(node, 1)
        visible = node.visible.getValue()[1]
        if visible:
          reveal_interior(node.graphObject_)
        else:
          hide_interior(node.graphObject_)      
    elif is_link(node):
      if is_containment_relation(node):
        visible = get_visual_setting(node.graphObject_, "links_visible")
        if node.node_parent != None:
          visible = visible and node.node_parent.visible.getValue()[1]
        set_link_visibility(node, visible)
      else:
        visible = 1
        if node.node_parent != None:
          visible = node.node_parent.visible.getValue()[1]
        set_link_visibility(node, visible)
        if node.node_parent != None:
          adjust_bbox(node.node_parent.graphObject_)
  recursive_apply(visual_entity.semanticObject, do_nothing, redraw_node, deep=0)
  restore_child_hypers(visual_entity)

# reset_parent_child_relation is the dual of set_parent_child_relation
# it removes the entity from it's parent's children list, and sets its
# parent to None.
def reset_parent_child_relation(entity):
  try:
    if entity != None and entity.node_parent != None:
      entity.node_parent.children.remove(entity)
      entity.node_parent = None
  except AttributeError:
    pass

# resize_to_default scales all the objects inside a given one to the
# default for that type of object
def resize_to_default(visual_entity):
#  semantic_object = visual_entity.semanticObject
#  if is_entity(semantic_object) and not is_terminal(semantic_object):
#    default_width = get_visual_setting(visual_entity, "default_width")+0.0
#    default_height = get_visual_setting(visual_entity, "default_height")+0.0
#    current_box = get_box_coords(visual_entity)
    adjust_bbox(visual_entity)

# resize_to_original scales the object to the size before it was scaled to
# the default size.
def resize_to_original(visual_object):
  try:
    semantic_object = visual_object.semanticObject
    canvas = visual_object.dc
    xscale = 1.0 / visual_object.scale[0] 
    yscale = 1.0 / visual_object.scale[1]
    prefix  = visual_object.tag+"."
    box = canvas.coords(canvas.find_withtag(prefix+"box")[0])
    xorigin = box[0]
    yorigin = box[1]
    def scale_node(node):
      if is_entity(node):
        scale_entity(node.graphObject_, semantic_object, xorigin, yorigin, xscale, yscale, 1)
      elif is_link(node):
        scale_link(node.graphObject_, semantic_object, xorigin, yorigin, xscale, yscale, 1)
    recursive_apply(semantic_object, scale_node, do_nothing)
  except AttributeError:
    pass

# restore_appearance, recovers the previously stored appearance of a
# visual entity.
def restore_appearance(visual_entity):
  visual_entity.graphForms = visual_entity.appearance[0]
  visual_entity.connectors = visual_entity.appearance[1]

# reveal_interior
def reveal_interior(visual_entity):
	semantic_object = visual_entity.semanticObject
	canvas = visual_entity.dc
	for gform in visual_entity.graphForms:
		gform.setVisible(1)
	for connector in visual_entity.connectors:
		make_connector_visible(connector, canvas)
	adjust_bbox(visual_entity)
	set_box_fill(visual_entity, "")
	# hack to ensure default stays default color
	if isinstance(visual_entity.semanticObject, Composite):
		if visual_entity.semanticObject.is_default.getValue()[1]:			
			set_box_outline(visual_entity, "darkgreen")
		else:
			set_box_outline(visual_entity, "darkblue")
	else:
		set_box_outline(visual_entity, "darkgray")

# save_appearance saves the visual_entity's current appearance in an attribute
# appearance of the entity's visual object, which is a pair (gl,cl) where
# gl is the list of graphical forms, and cl is the list of connectors.
def save_appearance(visual_entity):
  canvas = visual_entity.dc
  gfs = []
  for gf in visual_entity.graphForms:
    ngf = GraphicalForm(canvas, gf.handler, gf.name)
    ngf.Color = gf.Color
    ngf.bgColor = gf.bgColor
    ngf.hidden = gf.hidden
    ngf.antColor = gf.antColor
    gfs.append(ngf)
  cs = []
  for c in visual_entity.connectors:
    cs.append(c)
  visual_entity.appearance = (gfs, cs)

# scale_entity scales an entity.
def scale_entity(visual_entity, top_entity = None, xorigin = 0, yorigin = 0, xscale = 1, yscale = 1, visible = 1):
  if visual_entity == None: return
  canvas = visual_entity.dc
  for gform in visual_entity.graphForms:
    if visual_entity.semanticObject != top_entity:
      canvas.scale(gform.handler, xorigin, yorigin, xscale, yscale)
      gform.setVisible(visible)
    elif gform.elementType != 'text':
      canvas.scale(gform.handler, xorigin, yorigin, xscale, yscale)
  for connector_handler in visual_entity.connectors:
    canvas.scale(connector_handler, xorigin, yorigin, xscale, yscale)
    if visible:
      fill = 'red'
      outline = 'black'
    else:
      fill = ''
      outline = ''
    canvas.itemconfigure(connector_handler, fill = fill, outline = outline)

# scale_link scales a link.
def scale_link(visual_link, top_entity = None, xorigin = 0, yorigin = 0, xscale = 1, yscale = 1, visible = 1):
  canvas = visual_link.dc
  scale_entity(visual_link.centerObject, top_entity, xorigin, yorigin, xscale, yscale, visible)
  color = get_visual_setting(visual_link, "color")
  if get_visual_settings(visual_link,"links_visible"):
    visible = 1
  else:
    visible = 0
  if visible: fill = color
  else: fill = ''
  for ic in visual_link.in_connections_:
    handler, tag, seg_obj, link_obj = ic
    scale_entity(seg_obj, top_entity, xorigin, yorigin, xscale, yscale, visible)
    scale_entity(link_obj, top_entity, xorigin, yorigin, xscale, yscale, visible)
    canvas.scale(handler, xorigin, yorigin, xscale, yscale)
    canvas.itemconfigure(handler, fill = fill)
  for oc in visual_link.out_connections_:
    handler, tag, seg_obj, link_obj = oc
    scale_entity(seg_obj, top_entity, xorigin, yorigin, xscale, yscale, visible)
    scale_entity(link_obj, top_entity, xorigin, yorigin, xscale, yscale, visible)
    canvas.scale(handler, xorigin, yorigin, xscale, yscale)
    canvas.itemconfigure(handler, fill = fill)

# set_box_coords changes the entity's box. The box is assumed to be a 4-tuple.
def set_box_coords(visual_entity, box):
  pass
#  semantic_object = visual_entity.semanticObject
#  if is_entity(semantic_object) and not is_terminal(semantic_object):
#    for gf in visual_entity.graphForms:
#      if gf.elementType == "rectangle":
#        gf.setCoords(box)
#        break

def set_box_fill(visual_entity, color):
	semantic_object = visual_entity.semanticObject
	canvas = visual_entity.dc
	if isinstance(semantic_object, Composite):
		canvas.itemconfigure(getattr(visual_entity, GF_COMPOSITE_BOX).handler, fill=color)
	elif isinstance(semantic_object, Orthogonal):
		canvas.itemconfigure(getattr(visual_entity, GF_ORTHOGONAL_BOX).handler, fill=color)		

# set_box_outline assigns the entity's box's a border color.
def set_box_outline(visual_entity, color):
  semantic_object = visual_entity.semanticObject
  if is_entity(semantic_object):
    canvas = visual_entity.dc
    for gf in visual_entity.graphForms:
      if gf.elementType == "rectangle" or gf.elementType == "oval":
        canvas.itemconfigure(gf.handler, outline = color)
        gf.Color = color
        break

# set_connector_visibility(conn, canvas, visible)
def set_connector_visibility(conn, canvas, visible = 1):
  if visible: make_connector_visible(conn, canvas)
  else:       make_connector_invisible(conn, canvas)

# set_segment_visibility(conn, canvas, fill)
def set_segment_visibility(conn, canvas, fill = "grey"):
  if fill != "": make_segment_visible(conn, fill, canvas)
  else:          make_segment_invisible(conn, canvas)

# set_entity_visibility draws the graphical forms and connectors of an entity
# but not its children!
def set_entity_visibility(entity, visible = 1):
  if entity != None:
    try: # Assume the entity is a semantic object
      for gform in entity.graphObject_.graphForms:
        gform.setVisible(visible)
      for connector in entity.graphObject_.connectors:
        set_connector_visibility(connector, entity.graphObject_.dc, visible)
    except AttributeError: # assume the entity is a graph object
      for gform in entity.graphForms:
        gform.setVisible(visible)
      for connector in entity.connectors:
        set_connector_visibility(connector, entity.dc, visible)

# set_link_visibility
def set_link_visibility(link, visible = 1):
  visual_link = link.graphObject_
  canvas      = visual_link.dc
  link_color  = get_visual_setting(visual_link, "color")
  set_entity_visibility(visual_link.centerObject, visible)
  for ic in visual_link.in_connections_:
    handler, tag, seg_obj, link_obj = ic
    set_entity_visibility(seg_obj, visible)
    set_entity_visibility(link_obj, visible)
    if visible: canvas.itemconfigure(handler, fill = link_color)
    else:       canvas.itemconfigure(handler, fill = "")
  for oc in visual_link.out_connections_:
    handler, tag, seg_obj, link_obj = oc
    set_entity_visibility(seg_obj, visible)
    set_entity_visibility(link_obj, visible)
    if visible: canvas.itemconfigure(handler, fill = link_color)
    else:       canvas.itemconfigure(handler, fill = "")

# set_parent_child_relation(p,c,r) assigns p to the attribute parent
# of the child c and the containment relation r, and adds c and r to p's 
# children list. It assumes that r is the containment relation already 
# connecting p to c. If no r is given, it is ignored.
def set_parent_child_relation(node_parent, child, relation = None):
  child.node_parent = node_parent
  if node_parent != None and is_legal(node_parent) and not is_terminal(node_parent) and child not in node_parent.children:
    node_parent.children.append(child)
  if relation != None and is_legal_containment_relation(node_parent, child, relation):
    relation.node_parent = node_parent
    if node_parent != None and is_legal(node_parent) and not is_terminal(node_parent) and relation not in node_parent.children:
      node_parent.children.append(relation)

# set_source(r, s) sets the source of the link r to s.
def set_source(relation, new_source):
  relation.in_connections_ = [new_source]

# set_targets(r, t) sets the targets of the link r to t.
def set_targets(relation, new_targets):
  relation.out_connections_ = new_targets

# set_text_coords changes the entity's text's coords. 
def set_text_coords(visual_entity, x, y):
  semantic_object = visual_entity.semanticObject
  if is_entity(semantic_object):
    for gf in visual_entity.graphForms:
      if gf.elementType == "text":
        gf.setCoords((x, y))
        break

# set_text_fill assigns the entity's text's a fill color.
def set_text_fill(visual_entity, color):
  semantic_object = visual_entity.semanticObject
  if is_entity(semantic_object):
    canvas = visual_entity.dc
    for gf in visual_entity.graphForms:
      if gf.elementType == "text":
        canvas.itemconfigure(gf.handler, fill = color)
        gf.Color = color
        break

# set_visibility changes the visibility of a given visual object, that is,
# is the entity's visible attribute is set to true, it makes the contents
# visible, otherwise it hides them.
def set_visibility(visual_object):
  semantic_object = visual_object.semanticObject
  visible = semantic_object.visible.getValue()[1]
  if visible:
    redraw_entity(visual_object)
  else:
    hide_interior(visual_object)

# show_link shows a single link depending on the global visual settings
def show_link(semantic_connection):
  visual_object = semantic_connection.graphObject_
  visible       = get_visual_setting(visual_object, "links_visible")
  set_link_visibility(semantic_connection, visible)

# show_links switches the visibility of containment relations
def show_links(settings_node, containment_class):
  root = settings_node.rootNode
  dummy_sem_obj = containment_class(root.parent)
  dummy_sem_obj.rootNode = root
  dummy_sem_obj.root = root
  visual_object = dummy_sem_obj.graphClass_(0,0,dummy_sem_obj)
  visible       = get_visual_setting(visual_object, "links_visible")
  color         = get_visual_setting(visual_object, "color")
  canvas  = settings_node.graphObject_.dc
  exec "from "+containment_class.__name__+" import *"
  if visible:
    for relation in root.listNodes[containment_class.__name__]:
      canvas.lift(relation.graphObject_)
      for insegment in relation.graphObject_.in_connections_:
        canvas.itemconfig(insegment[0], fill = color)
      for outsegment in relation.graphObject_.out_connections_:
        canvas.itemconfig(outsegment[0], fill = color)
  else:
    for relation in root.listNodes[containment_class.__name__]:
      canvas.lift(relation.graphObject_)
      for insegment in relation.graphObject_.in_connections_:
        canvas.itemconfig(insegment[0], fill = "")
      for outsegment in relation.graphObject_.out_connections_:
        canvas.itemconfig(outsegment[0], fill = "")
