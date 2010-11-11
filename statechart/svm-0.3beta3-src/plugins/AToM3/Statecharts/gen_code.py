###############################################################################
# gen_code.py
# Spencer Borland (sborla@cs.mcgill.ca)
# April 2003
# COMMENTS: Handles the transformation of a Statechart model into 
#           a pythonDEVS model.
###############################################################################

from Basic import *
from Composite import *
from History import *
from Orthogonal import *
from Hyperedge import *
from contains import *
from orthogonality import *
from RT_DEVS import *
from string import split
INFINITY = "INFINITY"

###############################################################################
# class SC2DEVS_TRANSITION
###############################################################################
class SC2DEVS_TRANSITION:
	ID = 0
	def __init__(self, name=""):
		SC2DEVS_TRANSITION.ID += 1
		self.ID = str(SC2DEVS_TRANSITION.ID)
		self.type = "TRANSITION"
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name
		self.trigger = None
		self.guard = None
		self.actions = []
		self.broadcast = None
		self.broadcast_to = None
		self.out_segments = []
		self.in_segments = []

	def copy(self):
		T = SC2DEVS_TRANSITION()
		T.set_name(self.name)
		T.trigger = self.trigger
		T.guard = self.guard
		T.actions = self.actions[:]
		T.broadcast = self.broadcast
		T.broadcast_to = self.broadcast_to
		T.out_segments = self.out_segments[:]
		T.in_segments = self.in_segments[:]
		return T

	def set_name(self, name):
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name

	def set_trigger(self, trigger):
		self.trigger = SC2DEVS_TRIGGER(trigger)

	def set_guard(self, guard):
		self.guard = SC2DEVS_GUARD(guard)

	def add_action(self, action):
		if is_valid_string(action): self.actions.append(action)

	def set_broadcast(self, broadcast, broadcast_to):
		from string import split
		if is_valid_string(broadcast): self.broadcast = broadcast
		if is_valid_string(broadcast_to): self.broadcast_to = split(broadcast_to, ".")
		else: self.broadcast_to = []

###############################################################################
# class SC2DEVS_NODE
###############################################################################
class SC2DEVS_NODE:
	ID = 0
	def __init__(self, type=""):
		SC2DEVS_NODE.ID += 1
		self.ID = str(SC2DEVS_NODE.ID)
		self.type = type
		self.name = type+"_"+self.ID
		self.is_default = 0
		self.default = None
		self.is_special = 0
		self.is_deep = 0
		self.enter_actions = []
		self.exit_actions = []
		self.children = []
		self.parent = None
		self.out_transitions = []
		self.in_transitions = []
		# transition_groups is a list of the form [(trigger, [transitions])]
		# it groups all the outgoing transitions into groups which have the same trigger
		# > trigger is an obj of type SC2DEVS_TRIGGER
		# > transitions is a list of objects of type SC2DEVS_TRANSITION
		self.transition_groups = []

	def set_name(self, name):
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name

###############################################################################
# class SC2DEVS_REGION
###############################################################################
class SC2DEVS_REGION:
	ID = 0
	def __init__(self, type="ORTHOGONAL"):
		SC2DEVS_NODE.ID += 1
		self.ID = str(SC2DEVS_NODE.ID)
		self.type = type
		self.name = "ORTHOGONAL_"+self.ID
		self.children = []
		self.enter_actions = []
		self.exit_actions = []
		self.parent = None
		self.out_transitions = []
		self.in_transitions = []
		self.transition_groups = []

	def set_name(self, name):
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name

###############################################################################
# class SC2DEVS_TRIGGER
###############################################################################
class SC2DEVS_TRIGGER:
	def __init__(self, trigger):
		from string import upper,find
		if trigger == None or trigger == "":
			self.type = "NONE"
			self.time = 0
		elif upper(trigger[0:5]) == "AFTER":
			# parse required elapsed time
			self.type = "AFTER"
			try:
				self.time = float(trigger[find(trigger,"(")+1:find(trigger,")")])
			except:
				print "Parse error on trigger,", trigger
				self.type = "NONE"
		else:
			self.type = "EVENT"
			self.event = str(trigger)

	def __cmp__(self, other):
		if self.type == other.type:
			if self.type == "NONE": return 0
			elif self.type == "AFTER":
				if self.time == other.time: return 0
				else: return -1
			elif self.type == "EVENT":
				if self.event == other.event: return 0
				else: return -1
			else: print "FATAL ERROR"
		return -1

###############################################################################
# class SC2DEVS_GUARD
###############################################################################
class SC2DEVS_GUARD:
	def __init__(self, guard):
		from string import upper,split,find
		if upper(guard[0:2]) == "IN":
			self.type = "REFERENCE"
			try:
				tmp = guard[find(guard,"(")+1:find(guard,")")]
				self.referenced_state = split(tmp, ".")
			except:
				self.type = "NONE"
		elif guard == "" or guard == None:
			self.type = "NONE"
		else:
			self.type = "EXPRESSION"
			self.expression = guard

###############################################################################
# class SC2DEVS_COUPLED_DEVS
###############################################################################
class SC2DEVS_COUPLED_DEVS:
	ID = 0
	def __init__(self):
		self.type = "COUPLED"
		self.relay = None
		self.is_relay = 0
		SC2DEVS_COUPLED_DEVS.ID += 1
		self.ID = str(SC2DEVS_COUPLED_DEVS.ID)
		self.name = self.type+"_"+self.ID
		# ports is list of 2-tuples (port_name, in-out)
		# > port_name is the name of the port
		# > in-out is a 1 or 0 value indicating an input(1) or output(0)
		self.ports = []
		# connections is a list of 2-tuples (in, out)
		# > in is the name in the in port after self.
		# > out is the name of the out port after self.
		self.connections = []
		# parent is an object of type SC2DEVS_COUPLED_DEVS or None
		self.parent = None
		self.X_self = None
		self.Y_self = None
		# submodels is a list of 2-tuple (name, submodel)
		# > name is the class attribute name for the submodel (usually submodel.name)
		# > submodel is a devs model
		self.submodels = []

	def set_name(self, name):
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name

	def add_submodel(self, name, model):
		if model != None:
			self.submodels.append((name, model))
			model.parent = self

###############################################################################
# class SC2DEVS_ATOMIC_DEVS
###############################################################################
class SC2DEVS_ATOMIC_DEVS:
	ID = 0
	def __init__(self):
		SC2DEVS_ATOMIC_DEVS.ID += 1
		self.ID = str(SC2DEVS_ATOMIC_DEVS.ID)
		self.is_relay = 0
		self.type = "ATOMIC"
		self.name = self.type+"_"+self.ID
		self.default = None
		self.parent = None
		# S is a list of states in the stateset
		self.states = []
		# ports is list of 2-tuples (port_name, in-out)
		# > port_name is the name of the port
		# > in-out is a 1 or 0 value indicating an input(1) or output(0)
		self.time_advance = {}
		# delta_internal is a dictionary of the form: {state: action}
		# > state is the source of the transition
		# > action is the code to be executed (should return the new state)
		self.delta_internal = {}
		# output_function (aka lambda) is a dictionary of the form {state: action}
		# > state is the required current state
		# > action is the code to be executed (should return None or DEVSevent instance)
		self.output_function = {}
		# triggers is a dictionary of the form {(event,inscope): action}
		# > inscope is a boolean indicating INSCOPE (not 0) or OUTSCOPE (0)
		# > event is the trigger event
		# > action is the action to be taken
		self.triggers = {}
		# transition_after_time specifies if an state has an outgoing transition
		# with an AFTER(X) trigger.  If this value is None, there is no trigger,
		# otherwise it must be set to (X, state) where
		# > X is the amount to time that must elapse before the transition can fire
		# > state is the destination of the 
		self.transition_after_time = None

	def set_name(self, name):
		if name == "" or name == None:
			self.name = self.type + "_" + self.ID
		else:
			self.name = name

	def add_state(self, state_str):
		if state_str == None or state_str == "":
			state = "S" + str(SC2DEVS_ATOMIC_DEVS.ID)
			SC2DEVS_ATOMIC_DEVS.ID += 1
		else:
			state = state_str
		self.states.append(state)
		return state

	def add_epsilon(self, epsilon=None):
		if epsilon == None:
			epsilon = "epsilon" + str(SC2DEVS_ATOMIC_DEVS.ID)
			SC2DEVS_ATOMIC_DEVS.ID += 1
		self.states.append(epsilon)
		self.time_advance[epsilon] = 0
		return epsilon

	def add_wait(self, wait=None):
		if wait == None:
			wait = "wait" + str(SC2DEVS_ATOMIC_DEVS.ID)
			SC2DEVS_ATOMIC_DEVS.ID += 1
		self.states.append(wait)
		self.time_advance[wait] = INFINITY
		return wait

	def set_time_advance(self, source, time):
		try: ta = self.time_advance[source]
		except: ta = INFINITY
		ta = min_ex(ta, time)
		self.time_advance[source] = ta

	def set_trigger(self, event, inscope, actions, destination, quotes=1):
		if quotes: action = actions + ["return self.states['"+destination+"']"]
		else: action = actions + ["return self.states["+destination+"]"]
		self.triggers[event,inscope] = clean_actions(action)

	def set_delta_internal(self, source, actions, destination, quotes=1):
		if quotes: action = actions + ["return self.states['"+destination+"']"]
		else: action = actions + ["return self.states["+destination+"]"]
		self.delta_internal[source] = clean_actions(action)

	def set_delta_int(self, source, actions):
		self.delta_internal[source] = clean_actions(actions)

	def set_delta_internal_guarded(self, source, guard, state_true, state_false, true_action=None):
		action = "if ("+guard+"):\n"
		if true_action != None: action += "\t"+true_action+"\n"
		action += "\treturn self.states['"+state_true+"']\n"
		action += "else: return self.states['"+state_false+"']"
		self.delta_internal[source] = clean_actions(action)

	def set_output_function_broadcast(self, source, broadcast_func, broadcast_to, node):
		if broadcast_to == None or broadcast_to == "": broadcast_to = []
		action = "def __outputFnc(self):\n"
		from string import split
		action_lines = split(broadcast_func, "\n")
		for line in action_lines: action += "\t"+line+"\n"
		action += "event = __outputFnc(self)\n"
		action += "if event != None:\n"
#		action += "\tevent.set_param('broadcast', 'TRUE')\n"
#		action += "\tevent.set_param('address', "+str(path(node,globals()["ROOT"])+broadcast_to)+")\n"
		action += "\tport_name = event.get_param('address')[0]\n"
		action += "\tdel event.get_param('address')[0]\n"
		action += "\tself.poke(self.ports[port_name], event)"
		val = clean_actions(action)
		self.output_function[source] = val

	def set_output_function(self, source, broadcast_func):
		action = "def __outputFnc(self):\n"
		from string import split
		action_lines = split(broadcast_func, "\n")
		for line in action_lines: action += "\t"+line+"\n"
		action += "event = __outputFnc(self)\n"
		action += "if event != None:\n"
#		action += "\tif len(event.get_param('address')) == 0:\n"
#		if is_relay(self):
#			action += "\t\tif event.get_param('broadcast') == 'TRUE':\n"
#			action += "\t\t\tself.poke(self.ports['_ALL_'], event)\n"
#		else:
#			action += "\t\tpass\n"
#		action += "\telse:\n"
		action += "\tport_name = event.get_param('address')[0]\n"
		action += "\tdel event.get_param('address')[0]\n"
		action += "\tself.poke(self.ports[port_name], event)"
		val = clean_actions(action)
		self.output_function[source] = val

###############################################################################
# GLOBAL FUNCTIONS
###############################################################################
def Statechart2DEVS(top_level_nodes):
	if top_level_nodes == []:
		print "NO REACHABLE STATES ON CANVAS"
		return
	print "START TRANSFORMATION"
	statechart = None

	print "ABOUT TO BUILD STATECHART"
	statechart = build_statechart(top_level_nodes, statechart)
	globals()["ROOT"] = statechart

	print "ABOUT TO VERIFY SYNTAX"
	errors = verify_syntax(statechart)
	if errors > 0:
		if errors == 1: print "There was 1 compilation error."
		else: print "There were %d compilation errors." % errors
		return
#	print_statechart(statechart)

	print "ABOUT TO BUILD DEVS"
	devs = build_devs(statechart)
#	print_devs(devs)

	print "ABOUT TO EMIT DEVS"
	emit_devs(devs)

	print "END TRANSFORMATION"

def print_statechart(node):
	def default_name(node):
		if node.default == None: return "None"
		return node.default.name
	def type_str(node):
		if is_history_star(node): return "H*"
		else: return node.type[0]
	def __print_transition(t, depth=0):
		print " "*depth, t.name, "[T]", t.trigger.type
		for node in t.out_segments:
			print " "*(depth+2), ">", node.name
	def __print_node(n, depth=0):
		if has_children(n):
			print " "*depth, n.name, "["+type_str(n)+"]", "[default: "+default_name(n)+"]"
		else:
			print " "*depth, n.name, "["+type_str(n)+"]"
		for t in n.out_transitions:
			__print_transition(t, depth+2)
		for child in n.children:
			__print_node(child, depth+2)
	__print_node(node, 0)

def print_devs(devs):
	def __print_coupled(coupled, depth):
		print depth*" " + "[COUPLED]", coupled.name
		for name,devs in coupled.submodels:
			__print_devs(devs, depth+2)
	def __print_atomic(atomic, depth):
		print depth*" " + "[ATOMIC]", atomic.name
		print depth*" " + "  [STATES]", atomic.states
		for source in atomic.delta_internal:
			for guard,action in atomic.delta_internal[source]:
				print depth*" " + "  [INT]", source
		for source,event in atomic.delta_external:
			for guard,action in atomic.delta_external[source,event]:
				print depth*" " + "  [EXT]", source, event
		for source in atomic.time_advance:
			time = atomic.time_advance[source]
			print depth*" " + "  [TA]", source, time
		for source in atomic.output_function:
			action = atomic.output_function[source]
			print depth*" " + "  [LAMBDA]", source
	def __print_devs(devs, depth):
		if is_coupled(devs):
			__print_coupled(devs, depth)
		else:
			__print_atomic(devs, depth)
	__print_devs(devs, 0)

###############################################################################
# HELPER FUNCTIONS
###############################################################################
def is_composite(node): return node.type == "COMPOSITE"
def is_terminal(node): return node.type == "BASIC" or node.type == "HISTORY"
def is_orthogonal(node): return node.type == "ORTHOGONAL"
def is_history(node): return node.type == "HISTORY"
def is_history_star(node): return node.type == "HISTORY" and node.star
def is_basic(node): return node.type == "BASIC"
def is_atomic(devs): return devs.type == "ATOMIC"
def is_coupled(devs): return devs.type == "COUPLED"
def is_relay(devs): return devs.is_relay

def min_ex(val1, val2):
  if val2 == INFINITY:
    return val1
  elif val1 == INFINITY:
    return val2
  elif val1 > val2:
    return val2
  else:
    return val1

def max_ex(val1, val2):
  if val1 == INFINITY:
    return val1
  elif val2 == INFINITY:
    return val2
  elif val1 > val2:
    return val1
  else:
    return val2

def has_children(node):
	if node == None: return 0
	return len(node.children) > 0

def has_basic_children(node):
	if node == None: return 0
	for child_node in node.children:
		if is_basic(child_node): return 1
	return 0

def all_sub_nodes(node):
	def __all_sub_nodes(node, all):
		if is_terminal(node): return
		for child_node in node.children:
			all.append(child_node)
			__all_sub_nodes(child_node, all)
	all = []
	__all_sub_nodes(node, all)
	return all

def is_hyper(transition):
	if transition == None: return 0
	if not isinstance(transition, SC2DEVS_TRANSITION): return 0
	return len(transition.out_segments) > 1 or len(transition.in_segments) > 1

def is_valid_string(s):
	if s == "" or s == None: return 0
	valid = 0
	for index in range(0,len(s)):
		if s[index] != '\n' and s[index] != ' ':
			valid = 1
	return valid

def condense(s):
	i = len(s)-1
	while i > 0:
		if s[i] != '\n': break
		i -= 1
	return s[0:i+1]

def clean_actions(actions):
	if type(actions) == str: cleaned = condense(actions)
	else:
		from string import join
		cleaned = condense(join(actions, ""))
	if is_valid_string(cleaned): return cleaned
	return None

def get_index(obj, list):
	index = 0
	for o in list:
		if o == obj:
			return index
		index += 1
	return -1

def is_next_level_orthogonal(node):
	if node == None: return 0
	if not has_children(node): return 0
	return is_orthogonal(node.children[0])

def delete_from_list(obj, list):
	index = get_index(obj, list)
	if index >= 0:
		del list[index]
		return 1
	return 0

def is_inscope_at_init(node):
	current = node
	while current != None:
		if not current.is_default:
			return 0
		current = current.parent
	return 1

def path(source, destination, is_transition=0):
	def __path(source, destination, source_path=[], destination_path=[]):
		if source == destination: return source_path, destination_path
		elif source.scope >= destination.scope:
			source_path.append("_PARENT_")
			return __path(source.parent, destination, source_path, destination_path)
		else:
			destination_path.append(destination.name)
			return __path(source, destination.parent, source_path, destination_path)
	if destination in all_sub_nodes(source)+[source] and is_transition: # must go up then down
		source_path, destination_path = __path(source.parent, destination)
		source_path.append("_PARENT_")
	else: source_path, destination_path = __path(source, destination)
	destination_path.reverse()
	return source_path+destination_path

def output(event, params):
	action = "event = DEVSevent('"+event+"')\n"
	for name,value in params:
		action += "event.set_param('"+name+"', "+str(value)+")\n"
	action += "return event"
	return action

def csq(referenced_state, source):
	source_to_ROOT = path(source, globals()["ROOT"])
	ROOT_to_source = path(globals()["ROOT"], source)
	address = source_to_ROOT+referenced_state
	from_address = []
	for s in referenced_state: from_address.append("_PARENT_")
	from_address = from_address+ROOT_to_source
	return output("CSQ", [("address",address), ("from_address",from_address)])

def enter_history(address, return_address):
	return output("ENTER", [("address",address), ("history","'TRUE'"), ("return_address", return_address)])

def enter_history_star(address, return_address):
	return output("ENTER", [("address",address), ("history","'TRUE'"), ("broadcast","'TRUE'"), ("return_address", return_address)])

def enter_state(address, return_address):
	return output("ENTER", [("address",address), ("return_address", return_address)])

def exitack(node_name):
	return output("EXITACK", [("history_state", "'"+node_name+"'"), ("address",["_PARENT_"])])

def exitall(orthogonal):
	if orthogonal:
		return output("EXITALL", [("address",["_ALL_"]), ("broadcast","'TRUE'")])
	else:
		action = "return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])"
		return action

def enter(source, destination, is_transition=0):
	if is_history_star(destination):
		address = path(source, destination.parent, is_transition)
		return_address = path(destination.parent, source, is_transition)
		return enter_history_star(address, return_address)
	elif is_history(destination):
		address = path(source, destination.parent, is_transition)
		return_address = path(destination.parent, source, is_transition)
		return enter_history(address, return_address)
	else:
		address = path(source, destination, is_transition)
		return_address = path(destination, source, is_transition)
		return enter_state(address, return_address)

def enter_default(composite_node):
	return output("ENTER", [("address", [composite_node.default.name]), ("return_address", ["_PARENT_"])])

def enter_default_all(composite_node):
	return output("ENTER", [("address", ["_ALL_"]), ("return_address", ["_PARENT_"])])

def enter_each_destination(t, relay, current, last, source):
	if len(t.out_segments) > 1:
		for i in range(0, len(t.out_segments)-1):
			destination = t.out_segments[i]
			epsilon_next = relay.add_epsilon()
			if source == destination: # REFLEXIVE
				last = "INSCOPE"
				relay.set_delta_internal(current, source.enter_actions, epsilon_next)
			else:
				relay.set_delta_internal(current, [], epsilon_next)
				relay.set_output_function(current, enter(source, destination, 1))
			current = epsilon_next
	destination = t.out_segments[len(t.out_segments)-1]
	if source == destination: # REFLEXIVE
		relay.set_delta_internal(current, source.enter_actions, "INSCOPE")
		if is_composite(source):
#			theenter = enter(source, source.default, 0)
			relay.set_output_function(current, enter(source, source.default, 0))
	else:
		relay.set_delta_internal(current, [], last)
		relay.set_output_function(current, enter(source, destination, 1))

#def enter_each_default(relay, current, last, parent):
#	if is_next_level_orthogonal(parent):
#		for child_node in parent.children:
#			epsilon = relay.add_epsilon()
#			if child_node == parent.children[len(parent.children)-1]: epsilon = last
#			relay.set_delta_internal(current, [], epsilon)
#			relay.set_output_function(current, enter(parent, child_node, 0))
#			current = epsilon
#	else:
#		relay.set_delta_internal(current, [], last)
#		relay.set_output_function(current, enter(parent, parent.default, 0))

def build_exitall(self, epsilon_start, epsilon_end, composite_node):
	self.set_output_function(epsilon_start, exitall(is_next_level_orthogonal(composite_node)))
	wait = self.add_wait()
	self.set_delta_internal(epsilon_start, [], wait)
	if is_next_level_orthogonal(composite_node):
		for i in range(0,len(composite_node.children)-1):
			wait_next = self.add_wait()
			action = "if get_from_Q(self.Q, 'EXITACK') != None: return self.states['"+wait_next+"']\n"
			action += "else: return self.state"
			self.set_delta_int(wait, [action])
			wait = wait_next
		action = "if get_from_Q(self.Q, 'EXITACK') != None: temp = '"+epsilon_end+"'\n"
		action += "else: temp = self.state.name\n"
		self.set_delta_internal(wait, [action]+composite_node.exit_actions, "temp", 0)
	else:
		action = "event = get_from_Q(self.Q, 'EXITACK')\n"
		action += "if event != None:\n"
		action += "\tself.history = event.get_param('history_state')\n"
		action += "\ttemp = '"+epsilon_end+"'\n"
		action += "else: temp = self.state.name\n"
		self.set_delta_internal(wait, [action]+composite_node.exit_actions, "temp", 0)

def build_core_transition(t, self, epsilon_true, node):
	epsilon_triggered = self.add_epsilon()
	if t.trigger.type == "EVENT":
		guard = "self.state != 'OUTSCOPE'"
	else:
		self.set_time_advance("INSCOPE", t.trigger.time)
		self.set_delta_internal("INSCOPE", [], epsilon_triggered)
	if t.guard.type == "REFERENCE":
		wait_csr = atomic.add_wait()
		atomic.set_delta_internal(epsilon_triggered, [], wait_csr)
		atomic.set_output_function(epsilon_triggered, csq(t.guard.referenced_state, "UP", node.name), "self.UP")
		exp = "self.event.get_param('value') == 'TRUE'"
#		atomic.set_delta_external_guarded(wait_csr, "CSR", exp, epsilon_true, "INSCOPE")
	else:
		self.set_delta_internal_guarded(epsilon_triggered, t.guard.expression, epsilon_true, "INSCOPE")

marked_hypers = [] # need this to stay in scope
def build_transition_hyper(t, atomic, node):
	if t in marked_hypers: return
	else: marked_hypers.append(t)
	# of all the sources of t, find the highest scoped
	min_scope = t.in_segments[0].scope
	min_scoped_node = t.in_segments[0]
	for source in t.in_segments:
		if source.scope < min_scope:
			min_scope = source.scope
			min_scoped_node = source
	parent = min_scoped_node.parent.parent
	relay = min_scoped_node.parent.parent.devs.relay # there must be a parent here
	# response to external event
	epsilon_true = relay.add_epsilon()
	build_core_transition(t, atomic, epsilon_true, node)
	current = epsilon_true
	# query each source of t, to ensure each is current
	# if at least one is not current, the transition should not fire
	for source in t.in_segments: # for each source, send query and wait for response
		wait = relay.add_wait()
		epsilon = relay.add_epsilon()
		relay.set_delta_internal(current, [], wait)
		relay.set_output_function(current, csq(source.name, "DOWN", parent.name), "self.DOWN")
		action = "value = self.event.get_param('value')\n"
		action += "if value == 'TRUE': temp = '"+epsilon+"'\n"
		action += "else: temp = 'INSCOPE'"
		current = epsilon
	# all sources of t are current and guard is true so send EXITALL
	wait = relay.add_wait()
	relay.set_delta_internal(current, t.actions, wait)
	action = "event = DEVSevent('EXITALL')\n"
	action += "event.set_param('broadcast', 'TRUE')\n"
	action += "return event"
	relay.set_output_function(current, action)
	# now wait for an EXITACK from each orthogonal
	current = wait
	for orthogonal in parent.children:
		wait = relay.add_wait()
#		relay.set_delta_external(current, "EXITACK", [], wait)
		current = wait
	relay.set_time_advance(current, 0) # the last wait should be an epsilon
	enter_each_destination(t, relay, current, "OUTSCOPE", parent)

def build_transition_group(trigger, transition_list, atomic, node):
	if len(transition_list) == 0: return
	epsilon_triggered = atomic.add_epsilon()
	if trigger.type == "EVENT":
		atomic.set_trigger(trigger.event, 1, [], epsilon_triggered)
	else: # AFTER
		atomic.set_trigger("_TIMEOUT_", 1, [], epsilon_triggered)
		atomic.transition_after_time = trigger.time
	# check each guard until we find one that is true
	current = epsilon_triggered
	for t in transition_list:
		epsilon_true = atomic.add_epsilon()
		epsilon_false = atomic.add_epsilon()
		epsilon_broadcast = atomic.add_epsilon()
		epsilon_exit = atomic.add_epsilon()
		epsilon_enter = atomic.add_epsilon()
		epsilon_output = atomic.add_epsilon()
		if t.guard.type == "REFERENCE":
			wait_csr = atomic.add_wait()
			atomic.set_delta_internal(current, [], wait_csr)
			atomic.set_output_function(current, csq(t.guard.referenced_state, node))
			action = "e = get_from_Q(self.Q, 'CSR')\n"
			action += "if e != None:\n"
			action += "\tif e.get_param('value') == 'TRUE': return self.states['"+epsilon_true+"']\n"
			action += "\telse: return '"+epsilon_false+"'\n"
			action += "else: return self.state"
			atomic.set_delta_int(wait_csr, [action])
		else:
			atomic.set_delta_internal_guarded(current, t.guard.expression, epsilon_true, epsilon_false)
		if is_basic(node):
			atomic.set_delta_internal(epsilon_true, t.actions+node.exit_actions, epsilon_exit)
		else: # exit action will be executed upon receiving an EXITACK (in build_exitall)
			atomic.set_delta_internal(epsilon_true, t.actions, epsilon_exit)
		if is_basic(node): epsilon_output = epsilon_exit
		else: build_exitall(atomic, epsilon_exit, epsilon_output, node)
		atomic.set_delta_internal(epsilon_output, [], epsilon_enter)
		atomic.set_output_function_broadcast(epsilon_output, t.broadcast, t.broadcast_to, node)
		enter_each_destination(t, atomic, epsilon_enter, "OUTSCOPE", node)
		current = epsilon_false
	atomic.set_delta_internal(current, [], "INSCOPE") # no guards were true

###############################################################################
# MAKE FUNCTIONS
###############################################################################
def makeTRANSITION(t):
	T = SC2DEVS_TRANSITION()
	T.set_name(t.name.getValue())
	T.set_trigger(t.trigger.getValue())
	T.set_guard(t.guard.getValue())
	T.add_action(t.action.getValue())
	T.set_broadcast(t.broadcast.getValue(), t.broadcast_to.getValue())
	return T

def makeSTATECHARTcomposite(c):
	S = SC2DEVS_NODE("COMPOSITE")
	S.set_name(c.name.getValue())
	S.is_default = c.is_default.getValue()[1]
	S.enter_actions.append(c.enter_action.getValue())
	S.exit_actions.append(c.exit_action.getValue())
	return S

def makeSTATECHARTbasic(b):
	S = SC2DEVS_NODE("BASIC")
	S.set_name(b.name.getValue())
	S.is_default = b.is_default.getValue()[1]
	S.enter_actions.append(b.enter_action.getValue())
	S.exit_actions.append(b.exit_action.getValue())
	return S

def makeSTATECHARThistory(h):
	S = SC2DEVS_NODE("HISTORY")
	S.set_name(h.name.getValue())
	S.is_default = h.is_default.getValue()[1]
	S.star = h.star.getValue()[1]
	return S

def makeSTATECHARTorthogonal(o):
	S = SC2DEVS_REGION("ORTHOGONAL")
	S.set_name(o.name.getValue())
	S.children = []
	S.parent = None
	return S

def makeNODE(node):
	if isinstance(node, Basic):
		N = makeSTATECHARTbasic(node)
	elif isinstance(node, Composite):
		N = makeSTATECHARTcomposite(node)
	elif isinstance(node, Orthogonal):
		N = makeSTATECHARTorthogonal(node)
	elif isinstance(node, History):
		N = makeSTATECHARThistory(node)
	else:
		print "FATAL TYPE ERROR"
		N = None
	return N

###############################################################################
# depth_first_action
# Applies an action to the Statechart, recusively (pseudo depth first order)
# to all children.
# PARAMS:
# > S: an instance of SC2DEVS_NODE
# > f: a function
###############################################################################
def depth_first_action(S, f):
	def __depth_first_action(node, f, marked=[]):
		if node in marked: return
		else: marked.append(node)
		# should copy iterated lists in case f deletes any items in them
		children = node.children[:]
		f(node)
		for child_node in children:
			__depth_first_action(child_node, f, marked)
		transitions = node.out_transitions[:]
		for t in transitions:
			out_segments = t.out_segments[:]
			for sibling_node in out_segments:
				__depth_first_action(sibling_node, f, marked)
	if S != None:
		__depth_first_action(S, f, [])

###############################################################################
# build_statechart
# This function simply reconstructs the statechart data structure in a more
# usable format than that used in atom3.
# PARAMS:
# > default_node: an entity from atom3 (Basic, Composite, or History)
# > STATECHART: an instance of class SC2DEVS_Statechart
# RETURNS: an instance of class SC2DEVS_Statechart
###############################################################################
def build_statechart(top_level_nodes, STATECHART):
	def __conglomerate(node, t):
		for trigger,transition_list in node.transition_groups:
			if trigger == t.trigger:
				transition_list.append(t)
				return
		node.transition_groups.append((t.trigger, [t]))
	def __set_scopes(root_statechart):
		def __set_scope(node, scope):
			node.scope = scope
			for child_node in node.children:
				__set_scope(child_node, scope+1)
		__set_scope(root_statechart, 0)
	def __build_transition(t, seen):
		if t in seen: return seen[t]
		T = makeTRANSITION(t)
		seen[t] = T
		for node in t.out_connections_:
			N = __build_node(node, seen)
			if N != None:
				N.in_transitions.append(T)
				T.out_segments.append(N)
		return T
	def __build_node(node, seen):
		if node in seen: return seen[node]
		N = makeNODE(node)
		seen[node] = N
		for t in node.out_connections_:
			if isinstance(t, contains) or isinstance(t, orthogonality):
				child = t.out_connections_[0]
				C = __build_node(child, seen)
				if C != None:
					N.children.append(C)
					C.parent = N
				if not is_orthogonal(C):
					if C.is_default:
						N.default = C
			elif isinstance(t, Hyperedge):
				T = __build_transition(t, seen)
				if T != None:
					T.in_segments.append(N)
					N.out_transitions.append(T)
					__conglomerate(N, T)
			else: print "FATAL ERROR"
		return N
	# start building
	R = SC2DEVS_NODE("COMPOSITE")
	R.is_default = 1
	R.set_name("ROOT")
	seen = {}
	for node in top_level_nodes:
		if node not in seen:
			N = __build_node(node, seen)
			seen[node] = N
			if not is_orthogonal(N):
				if N.is_default: R.default = N
		else:
			N = seen[node]
		R.children.append(N)
		N.parent = R
	__set_scopes(R)
	return R

###############################################################################
# verify_syntax
# This function verifies the syntax of a statechart model.
# PARAMS:
# > root_statechart: an instance of class SC2DEVS_NODE
# returns: the number of syntax errors
###############################################################################
def verify_syntax(root_statechart):
	return 0

###############################################################################
# class SC2DEVS_RELAY
###############################################################################
class SC2DEVS_RELAY(SC2DEVS_ATOMIC_DEVS):
	def __init__(self, composite_node):
		SC2DEVS_ATOMIC_DEVS.__init__(self)
		self.is_relay = 1
		self.scope = composite_node.scope
		if is_next_level_orthogonal(composite_node):
			self.is_orthogonal = 1
		else:
			self.is_orthogonal = 0
			self.history = composite_node.default.name
		self.name = "RELAY_" + composite_node.name + "_" + self.name
		self.add_wait("INSCOPE")
		self.add_wait("OUTSCOPE")
		self.add_epsilon("INSCOPE_DQ")
		self.add_epsilon("OUTSCOPE_DQ")
		self.set_delta_int("INSCOPE", ["return self.states['INSCOPE_DQ']"])
		self.set_delta_int("OUTSCOPE", ["return self.states['OUTSCOPE_DQ']"])
		self.build_relay(composite_node)

	def build_relay(self, composite_node):
		self.hook_default(composite_node)
		self.hook_history(composite_node)
		self.hook_history_star(composite_node)
		self.hook_alpha_relay(composite_node)
#		self.hook_exit(composite_node)
		self.handle_arbitrary_event(composite_node)
		self.handle_CSQ(composite_node)
		self.handle_EXITALL(composite_node)
		self.handle_ENTER_OUTSCOPE(composite_node)
		self.handle_ENTER_INSCOPE(composite_node)
		self.handle_transitions(composite_node)
		# set init
		if composite_node.parent == None: # composite_node is ROOT
#			self.add_epsilon("INIT")
#			enter_each_default(self, "INIT", "INSCOPE", composite_node)
			self.default = "__default_hook"
		else: self.default = "OUTSCOPE"

#	def hook_exit(self, composite_node):
#		self.add_epsilon("__exit_hook")
#		epsilon_end = self.add_epsilon()
#		build_exitall(self, "__exit_hook", epsilon_end, composite_node)
#		self.set_delta_internal(epsilon_end, [], "OUTSCOPE")
#		self.set_output_function(epsilon_end, "return EVENT('EXITACK', [('address', ['_PARENT_'])])")

	def hook_alpha_relay(self, composite_node):
		self.add_epsilon("__alpha_relay_hook")
		self.set_delta_internal("__alpha_relay_hook", [], "self.restore", 0)
		self.set_output_function("__alpha_relay_hook", "return self.event")

	def handle_transitions(self, composite_node):
		# transitions, hypers
		for t in composite_node.out_transitions:
			if len(t.in_segments) > 1:
				build_transition_hyper(t, self, composite_node)
		# transitions, groups
		for trigger,transition_list in composite_node.transition_groups:
			if len(t.in_segments) == 1:
				build_transition_group(trigger, transition_list, self, composite_node)

	def hook_default(self, composite_node):
		self.add_epsilon("__default_hook")
		epsilon = self.add_epsilon()
		self.set_delta_internal("__default_hook", [], epsilon)
		if is_next_level_orthogonal(composite_node): # default in each orthogonal
			self.set_delta_internal(epsilon, [], "INSCOPE")
			self.set_output_function(epsilon, enter_default_all(composite_node))
		else: # only one default state
			action = "self.current_child = '"+composite_node.default.name+"'\n"
			self.set_delta_internal(epsilon, [action], "INSCOPE")
			self.set_output_function(epsilon, enter_default(composite_node))

	def hook_history(self, composite_node):
		self.add_epsilon("__history_hook")
		action = "self.current_child = self.history\n"
		self.set_delta_internal("__history_hook", [action], "INSCOPE")
		action = "event = DEVSevent('ENTER')\n"
		action += "event.set_param('address', [self.history])\n"
		action += "event.set_param('history', 'TRUE')\n"
		action += "return event"
		self.set_output_function("__history_hook", action)

	def hook_history_star(self, composite_node):
		self.add_epsilon("__history_star_hook")
		action = "self.current_child = self.history\n"
		self.set_delta_internal("__history_star_hook", [action], "INSCOPE")
		action = "event = DEVSevent('ENTER')\n"
		action += "event.set_param('address', [self.history])\n"
		action += "event.set_param('broadcast', 'TRUE')\n"
		action += "event.set_param('history', 'TRUE')\n"
		action += "return event"
		self.set_output_function("__history_star_hook", action)
		
	def handle_arbitrary_event(self, composite_node):
		# build a relay_hook and broadcast_hook
		self.add_epsilon("__relay_hook")
		self.add_epsilon("__broadcast_hook")
		self.set_delta_internal("__relay_hook", [], "INSCOPE")
		self.set_delta_internal("__broadcast_hook", [], "INSCOPE")
		self.set_output_function("__relay_hook", "return self.event")
		if is_next_level_orthogonal(composite_node):
			action = "self.event.set_param('address', ['_ALL_'])\n"
		else:
			action = "self.event.set_param('address', [self.current_child])\n"			
		action += "self.event.set_param('broadcast', 'TRUE')\n"
		action += "return self.event"
		self.set_output_function("__broadcast_hook", action)

#	def handle_arbitrary_event(self, composite_node):
#		epsilon_relay = self.add_epsilon()
#		guard = "self.state != 'OUTSCOPE'"
#		self.set_delta_external_guarded(None, None, guard, epsilon_relay, "OUTSCOPE")
#		self.set_delta_internal(epsilon_relay, [], "INSCOPE")
#		action = "return self.event"
#		self.set_output_function(epsilon_relay, action)

	def handle_ENTER_OUTSCOPE(self, composite_node):
		epsilon_sub = self.add_epsilon()
		action = "if len(self.event.get_param('address')) == 0: # REACHED DESTINATION\n"
		action += "\tself.return_address = self.event.get_param('return_address')\n"
		action += "\tif self.event.get_param('history') == 'TRUE':\n"
		action += "\t\tif self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'\n"
		action += "\t\telse: temp = '__history_hook'\n"
		action += "\telse: temp = '__default_hook'\n"
		action += "else:\n"
		action += "\ttemp = '"+epsilon_sub+"'\n"
		action += "\tself.current_child = self.event.get_param('address')[0]\n"
		self.set_trigger("ENTER", 0, [action]+composite_node.enter_actions, "temp", 0)
		self.set_delta_internal(epsilon_sub, [], "INSCOPE")
		action = "return self.event"
		self.set_output_function(epsilon_sub, action)

	def handle_ENTER_INSCOPE(self, composite_node):
		epsilon_relay = self.add_epsilon()
		epsilon_parent = self.add_epsilon()
		action = "if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'\n"
		action += "elif self.event.get_param('address')[0] == '_PARENT_':\n"
		action += "\ttemp = '"+epsilon_parent+"'\n"
		action += "\tself.current_child = None\n"
		action += "else:\n"
		action += "\ttemp = '"+epsilon_relay+"'\n"
		action += "\tself.current_child = self.event.get_param('address')[0]\n"
		self.set_trigger("ENTER", 1, [action], "temp", 0)
		self.set_delta_internal(epsilon_relay, [], "INSCOPE")
		self.set_delta_internal(epsilon_parent, [], "OUTSCOPE")
		action = "return self.event"
		self.set_output_function(epsilon_parent, action)
		self.set_output_function(epsilon_relay, action)

	def handle_EXITALL(self, composite_node):
		epsilon_exitall = self.add_epsilon()
		epsilon_exitack = self.add_epsilon()
		self.set_trigger("EXITALL", 1, [], epsilon_exitall)
		build_exitall(self, epsilon_exitall, epsilon_exitack, composite_node)
		self.set_delta_internal(epsilon_exitack, [], "OUTSCOPE")
		action = "event = DEVSevent('EXITACK')\n"
		action += "event.set_param('address', ['_PARENT_'])\n"
		action += "event.set_param('history_state', '"+composite_node.name+"')\n"
		action += "return event"
		self.set_output_function(epsilon_exitack, action)

	def handle_CSQ(self, composite_node):
		epsilon_relay = self.add_epsilon()
		epsilon_true = self.add_epsilon()
		epsilon_false = self.add_epsilon()
		action = "if len(self.event.get_param('address')) > 0:\n"
		action += "\ttemp = '"+epsilon_relay+"'\n"
		false_action = action + "else: temp = '"+epsilon_false+"'\n"
		true_action = action + "else: temp = '"+epsilon_true+"'\n"
		self.set_trigger("CSQ", 0, [action], "temp", 0)
		self.set_trigger("CSQ", 1, [action], "temp", 0)
		self.set_delta_internal(epsilon_relay, [], "INSCOPE")
		self.set_delta_internal(epsilon_true, [], "INSCOPE")
		self.set_delta_internal(epsilon_false, [], "OUTSCOPE")
		action = "event = DEVSevent('CSR')\n"
		action += "event.set_param('address', self.event.get_param('from_address'))\n"
		action_true = action + "event.set_param('value', 'TRUE')\nreturn event"
		action_false = action + "event.set_param('value', 'FALSE')\nreturn event"
		self.set_output_function(epsilon_true, action_true)
		self.set_output_function(epsilon_false, action_false)
		self.set_output_function(epsilon_relay, "return self.event")

###############################################################################
# class SC2DEVS_TERMINAL
###############################################################################
class SC2DEVS_TERMINAL(SC2DEVS_ATOMIC_DEVS):
	def __init__(self, node):
		SC2DEVS_ATOMIC_DEVS.__init__(self)
		self.scope = node.scope
		node.devs = self
		self.set_name(node.name)
		self.build_terminal(node)

	def build_terminal(self, node):
		self.add_wait("INSCOPE")
		self.add_wait("OUTSCOPE")
		self.add_epsilon("INSCOPE_DQ")
		self.add_epsilon("OUTSCOPE_DQ")
		self.set_delta_int("INSCOPE", ["return self.states['INSCOPE_DQ']"])
		self.set_delta_int("OUTSCOPE", ["return self.states['OUTSCOPE_DQ']"])
		self.default = "OUTSCOPE"
		self.handle_ENTER(node)
		self.handle_CSQ(node)
		self.handle_EXITALL(node)
#		self.hook_exit(node)
		self.handle_transitions(node)

#	def hook_exit(self, node):
#		self.add_epsilon("__exit_hook")
#		self.set_delta_internal("__exit_hook", [], "OUTSCOPE")
#		self.set_output_function("__exit_hook", "return EVENT('EXITACK', [('address', ['_PARENT_'])])")

	def handle_ENTER(self, node):
		epsilon = self.add_epsilon()
		self.set_trigger("ENTER", 0, node.enter_actions, "INSCOPE")

	def handle_CSQ(self, node):
		epsilon_false = self.add_epsilon()
		epsilon_true = self.add_epsilon()
		action = "self.from_address = self.event.get_param('from_address')\n"
		self.set_trigger("CSQ", 0, [action], epsilon_false) # OUTSCOPE
		self.set_trigger("CSQ", 1, [action], epsilon_true) # INSCOPE
		self.set_delta_internal(epsilon_true, [], "INSCOPE")
		self.set_delta_internal(epsilon_false, [], "OUTSCOPE")
		action = "event = DEVSevent('CSR')\n"
		action += "event.set_param('address', self.from_address)\n"
		true_action = action + "event.set_param('value', 'TRUE')\nreturn event"
		false_action = action + "event.set_param('value', 'FALSE')\nreturn event"
		self.set_output_function(epsilon_true, true_action)
		self.set_output_function(epsilon_false, false_action)

	def handle_EXITALL(self, node):
		epsilon = self.add_epsilon()
		guard = "self.state != 'OUTSCOPE'"
		self.set_trigger("EXITALL", 1, [], epsilon)
		self.set_delta_internal(epsilon, node.exit_actions, "OUTSCOPE")
		self.set_output_function(epsilon, exitack(node.name))
		
	def handle_transitions(self, node):
		for t in node.out_transitions:
			if len(t.in_segments) > 1:
				build_transition_hyper(t, self, node)
		for trigger,transition_list in node.transition_groups:
			if len(t.in_segments) == 1:
				build_transition_group(trigger, transition_list, self, node)

###############################################################################
# class SC2DEVS_CONTAINER
###############################################################################
class SC2DEVS_CONTAINER(SC2DEVS_COUPLED_DEVS):
	def __init__(self, node):
		SC2DEVS_COUPLED_DEVS.__init__(self)
		self.set_name(node.name)
		node.devs = self
		self.scope = node.scope
		self.relay = SC2DEVS_RELAY(node)
		self.add_submodel("relay", self.relay)

###############################################################################
# build_devs
# Builds the required devs model from the statechart model.
# PARAMS:
# > statechart: a class of instance SC2DEVS_NODE
# RETURNS: a class of type SC2DEVS_COUPLED_DEVS
###############################################################################
def build_devs(statechart):
	global ROOT
	ROOT = statechart
	def __build_devs(node):
		if is_basic(node):
			return SC2DEVS_TERMINAL(node)
		elif is_composite(node) or is_orthogonal(node):
			container = SC2DEVS_CONTAINER(node)
			for child_node in node.children:
				if is_history(child_node): continue
				subdevs = build_devs(child_node)
				container.add_submodel(subdevs.name, subdevs)
				subdevs.parent = container
			return container
	return __build_devs(statechart)

###############################################################################
# emit_devs
# Writes the devs model to disk in a .py file compatible with pythonDEVS-RT.
# PARAMS:
# > root_devs: a class of instance SC2DEVS_COUPLED_DEVS
###############################################################################
def emit_devs(root_devs):
	def __wl(line, f, depth):
		if line == None or line == "": return
		tabs = ""
		for i in range(0,depth): tabs += '\t'
		f.write(tabs+line+"\n")
	def __write(line, f, depth):
		tabs = ""
		for i in range(0,depth): tabs += '\t'
		f.write(tabs+line)
	def __write_nodepth(line, f):
		f.write(line)
	def __emit_atomic(atomic, f, depth=0):
		__wl("class " + atomic.name + "(AtomicDEVS):", f, depth)
		__wl("def __init__(self):", f, depth+1)
		__wl("AtomicDEVS.__init__(self)", f, depth+2)
		if is_relay(atomic):
			__wl("self.scope = "+str(atomic.scope), f, depth+2)
			__wl("self.is_relay = 1", f, depth+2)
			__wl("self.current_child = None", f, depth+2)
			if not atomic.is_orthogonal:
				__wl("self.history = '"+atomic.history+"'", f, depth+2)
		else:
			__wl("self.scope = "+str(atomic.scope+0.5), f, depth+2)
			__wl("self.is_relay = 0", f, depth+2)
		__wl("self.Q = []", f, depth+2)
		__wl("self.delta_ext = 0", f, depth+2)
		__wl("self.inscope = 0", f, depth+2)
		__wl("self.timeout = 0", f, depth+2)
		__wl("self.elapsed_since_inscope = 0", f, depth+2)
		__wl("self.ports = {}", f, depth+2)
		__wl("self.ports['_IN_'] = self.addInPort('_IN_')", f, depth+2)
		__wl("self.ports['_PARENT_'] = self.addOutPort('_PARENT_')", f, depth+2)
		if is_relay(atomic): __wl("self.ports['_ALL_'] = self.addOutPort('_ALL_')", f, depth+2)
		__wl("self.states = {}", f, depth+2)
		for state in atomic.states:
			__wl("self.states['"+state+"'] = DEVSstate('"+state+"')", f, depth+2)
		__wl("self.state = self.states['"+atomic.default+"']", f, depth+2)
		__emit_delta_ext(atomic, f, depth+1)
		__emit_delta_int(atomic, f, depth+1)
		__emit_time_advance(atomic, f, depth+1)
		__emit_output_function(atomic, f, depth+1)
	def __emit_delta_ext(atomic, f, depth):
		__wl("def extTransition(self):", f, depth)
		__wl("if self.inscope: self.elapsed_since_inscope += self.elapsed", f, depth+1)
		__wl("else: self.elapsed_since_inscope = 0", f, depth+1)
		__wl("event = self.peek(self.ports['_IN_'])", f, depth+1)
		__wl("if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':", f, depth+1)
		__wl("if len(event.get_param('address')) > 0:", f, depth+2)
		__wl("if event.get_param('address')[0] != '_PARENT_':", f, depth+3)
		__wl("if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'", f, depth+4)
		__wl("else: self.restore = self.state.name", f, depth+4)
		__wl("self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'", f, depth+4)
		__wl("self.Q.append(event)", f, depth+1)
		__wl("self.delta_ext = 1", f, depth+1)
		__wl("return self.state", f, depth+1)
	def __emit_delta_int(atomic, f, depth=0):
		__wl("def intTransition(self):", f, depth)
		__wl("if self.inscope: self.elapsed_since_inscope += self.elapsed", f, depth+1)
		__wl("else: self.elapsed_since_inscope = 0", f, depth+1)
		if atomic.transition_after_time != None:
			__wl("if not self.timeout and round(self.elapsed_since_inscope, 6) >= "+str(atomic.transition_after_time)+":", f, depth+1)
			__wl("self.Q.append(EVENT('_TIMEOUT_'))", f, depth+2)
			__wl("self.elapsed_since_inscope = 0", f, depth+2)
			__wl("self.timeout = 1", f, depth+2)
		__wl("def get_new_state():", f, depth+1)
		# INSCOPE_DQ
		__wl("if self.state == 'INSCOPE_DQ':", f, depth+2)
		__wl("while len(self.Q) > 0:", f, depth+3)
		__wl("self.event=self.Q[0];del self.Q[0]", f, depth+4)
		first = 1
		for event,inscope in atomic.triggers:
			action = atomic.triggers[event,inscope]
			if inscope:
				if first: __wl("if self.event == '"+event+"':", f, depth+4); first=0
				else: __wl("elif self.event == '"+event+"':", f, depth+4)
				if action != None:
					action_lines = split(action, '\n')
					for line in action_lines: __wl(line, f, depth+5)
		__wl("elif len(self.event.get_param('address')) == 0:", f, depth+4)
		if atomic.is_relay:
			__wl("if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'", f, depth+5)
		else: __wl("pass", f, depth+5)
		__wl("else: return '__relay_hook'", f, depth+4)
		__wl("return self.states['INSCOPE']", f, depth+3)
		# OUTSCOPE_DQ
		__wl("elif self.state == 'OUTSCOPE_DQ':", f, depth+2)
		__wl("while len(self.Q) > 0:\n", f, depth+3)
		__wl("self.event=self.Q[0];del self.Q[0]", f, depth+4)
		first = 1
		for event,inscope in atomic.triggers:
			action = atomic.triggers[event,inscope]
			if not inscope:
				if first: __wl("if self.event == '"+event+"':", f, depth+4); first=0
				else: __wl("elif self.event == '"+event+"':", f, depth+4)
				if action != None:
					action_lines = split(action, '\n')
					for line in action_lines: __wl(line, f, depth+5)
		__wl("return self.states['OUTSCOPE']", f, depth+3)
		# all other states
		for source in atomic.delta_internal:
			action = atomic.delta_internal[source]
			__wl("elif self.state == '"+source+"':", f, depth+2)
			if action != None:
				action_lines = split(action, '\n')
				for line in action_lines: __wl(line, f, depth+3)
		__wl("else: return self.state", f, depth+2)
		__wl("new_state = get_new_state()", f, depth+1)
		__wl("if new_state == 'INSCOPE':", f, depth+1)
		__wl("self.inscope = 1", f, depth+2)
		__wl("if len(self.Q) == 0: self.timeout = 0", f, depth+2)
		__wl("elif new_state == 'OUTSCOPE':", f, depth+1)
		__wl("self.inscope = 0", f, depth+2)
		__wl("if len(self.Q) == 0: self.timeout = 0", f, depth+2)
		__wl("return new_state", f, depth+1)
	def __emit_time_advance(atomic, f, depth=0):
		__wl("def timeAdvance(self):", f, depth)
		__wl("if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0", f, depth+1)
		__wl("elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0", f, depth+1)
		__wl("elif self.delta_ext: ta = 0;self.delta_ext=0", f, depth+1)
		for source in atomic.time_advance:
			time = atomic.time_advance[source]
			__wl("elif self.state == '"+source+"':", f, depth+1)
			__wl("ta = "+str(time), f, depth+2)
		__wl("else: ta = INFINITY", f, depth+1)
		if atomic.transition_after_time != None:
			__wl("if self.inscope and not self.timeout:", f, depth+1)
			__wl("ta_after = max(0, "+str(atomic.transition_after_time)+"-self.elapsed_since_inscope)", f, depth+2)
			__wl("else:", f, depth+1)
			__wl("ta_after = INFINITY", f, depth+2)
			__wl("return minEx(ta, ta_after)", f, depth+1)
		else: __wl("return ta", f, depth+1)
	def __emit_output_function(atomic, f, depth=0):
		__wl("def outputFnc(self):", f, depth)
		if len(atomic.output_function) <= 0:
			__wl("pass", f, depth+1)
			return
		first = 1
		for source in atomic.output_function:
			broadcast_func = atomic.output_function[source]
			if first: __wl("if self.state == '"+source+"':", f, depth+1)
			else: __wl("elif self.state == '"+source+"':", f, depth+1)
			first = 0
			from string import split
			action_lines = split(broadcast_func, '\n')
			for line in action_lines: __wl(line, f, depth+2)
	def __emit_coupled(coupled, f, depth=0):
		for name,submodel in coupled.submodels:
			__emit_devs(submodel, f, 0)
		__wl("class " + coupled.name + "(CoupledDEVS):", f, depth)
		__wl("def __init__(self):", f, depth+1)
		__wl("CoupledDEVS.__init__(self)", f, depth+2)
		__wl("self.scope = "+str(coupled.scope), f, depth+2)
		__wl("self.ports = {}", f, depth+2)
		__wl("self.ports['_IN_'] = self.addInPort('_IN_')", f, depth+2)
		__wl("self.ports['_PARENT_'] = self.addOutPort('_PARENT_')", f, depth+2)
		__wl("self.ports['_ALL_'] = self.addOutPort('_ALL_')", f, depth+2)
		for submodel_name,submodel in coupled.submodels:
			__wl("self."+submodel_name+"=self.addSubModel("+submodel.name+"())", f, depth+2)
		for submodel_name,submodel in coupled.submodels:
			if is_relay(submodel): continue
			__wl("self.relay.ports['"+submodel.name+"'] = self.relay.addOutPort('"+submodel.name+"')", f, depth+2)
		for submodel_name,submodel in coupled.submodels:
			if is_relay(submodel): continue
			__wl("self.connectPorts(self.relay.ports['"+submodel.name+"'], self."+submodel_name+".ports['_IN_'])", f, depth+2)
			__wl("self.connectPorts(self."+submodel_name+".ports['_PARENT_'], self.relay.ports['_IN_'])", f, depth+2)
			__wl("self.connectPorts(self.relay.ports['_ALL_'], self."+submodel_name+".ports['_IN_'])", f, depth+2)
		__wl("self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])", f, depth+2)
		__wl("self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])", f, depth+2)
		# select
		__wl("def select(self, imm): return choose(self, imm)", f, depth+1)

	def __emit_devs(devs, f, depth=0):
		if is_coupled(devs):
			__emit_coupled(devs, f, 0)
		elif is_atomic(devs):
			__emit_atomic(devs, f, 0)
		else: print "FATAL ERROR"
	def __emit_globals(f):
		depth = 0
		# get_from_Q
		f.write("def get_from_Q(event_Q, event_name):\n")
		f.write("\tfor i in range(0, len(event_Q)):\n")
		f.write("\t\tif event_Q[i] == event_name:\n")
		f.write("\t\t\tevent = event_Q[i];del event_Q[i]\n")
		f.write("\t\t\treturn event\n")
		# choose
		__wl("def choose(coupled, imm):", f, depth)
		__wl("max_scope = 0", f, depth+1)
		__wl("deepest = imm[0]", f, depth+1)
		__wl("for devs in imm:", f, depth+1)
		__wl("if devs.scope > max_scope: deepest = devs; max_scope = devs.scope", f, depth+2)
		__wl("return deepest", f, depth+1)
	f = open("Statecharts/SC2DEVS_MODEL.py", "w")
	f.write("from RT_DEVS import *\n\n")
	f.write("try: import theglobals\nexcept: pass\n")
	__emit_globals(f)
	__emit_devs(root_devs, f, 0)
#	f.write("from threading import Event\n")
#	f.write("globals()['SYNC'] = Event()\n")
#	f.write("globals()['DEVS'] = ROOT()\n")
#	f.write("globals()['EXECUTOR'] = Executor(DEVS, SYNC)\n")
#	f.write("EXECUTOR.run()\n")
	f.close()
