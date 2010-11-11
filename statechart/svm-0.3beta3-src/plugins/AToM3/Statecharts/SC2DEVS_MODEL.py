from RT_DEVS import *

try: import theglobals
except: pass
def get_from_Q(event_Q, event_name):
	for i in range(0, len(event_Q)):
		if event_Q[i] == event_name:
			event = event_Q[i];del event_Q[i]
			return event
def choose(coupled, imm):
	max_scope = 0
	deepest = imm[0]
	for devs in imm:
		if devs.scope > max_scope: deepest = devs; max_scope = devs.scope
	return deepest
class RELAY_ROOT_ATOMIC_1(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 0
		self.is_relay = 1
		self.current_child = None
		self.history = 'A'
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon1'] = DEVSstate('epsilon1')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon2'] = DEVSstate('epsilon2')
		self.states['epsilon3'] = DEVSstate('epsilon3')
		self.states['epsilon4'] = DEVSstate('epsilon4')
		self.states['epsilon5'] = DEVSstate('epsilon5')
		self.states['epsilon6'] = DEVSstate('epsilon6')
		self.states['wait7'] = DEVSstate('wait7')
		self.states['epsilon8'] = DEVSstate('epsilon8')
		self.states['epsilon9'] = DEVSstate('epsilon9')
		self.states['epsilon10'] = DEVSstate('epsilon10')
		self.state = self.states['__default_hook']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon5']
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon10'
							self.current_child = None
						else:
							temp = 'epsilon9'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon2'
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon8'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon2'
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'wait7':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon6'
				else: temp = self.state.name
				return self.states[temp]
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'epsilon5':
				return self.states['wait7']
			elif self.state == 'epsilon2':
				return self.states['INSCOPE']
			elif self.state == 'epsilon3':
				return self.states['INSCOPE']
			elif self.state == 'epsilon1':
				self.current_child = 'A'
				return self.states['INSCOPE']
			elif self.state == 'epsilon6':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon4':
				return self.states['OUTSCOPE']
			elif self.state == '__default_hook':
				return self.states['epsilon1']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon8':
				return self.states['INSCOPE']
			elif self.state == 'epsilon9':
				return self.states['INSCOPE']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == 'epsilon10':
				return self.states['OUTSCOPE']
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon10':
			ta = 0
		elif self.state == 'wait7':
			ta = INFINITY
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == 'epsilon3':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == 'epsilon5':
			ta = 0
		elif self.state == 'epsilon2':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon1':
			ta = 0
		elif self.state == 'epsilon6':
			ta = 0
		elif self.state == 'epsilon4':
			ta = 0
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon8':
			ta = 0
		elif self.state == 'epsilon9':
			ta = 0
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon10':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon2':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon3':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon1':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['A'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon6':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'ROOT')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon4':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon5':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon8':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon9':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', [self.current_child])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class RELAY_A_ATOMIC_12(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 1
		self.is_relay = 1
		self.current_child = None
		self.history = 'B'
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon12'] = DEVSstate('epsilon12')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon13'] = DEVSstate('epsilon13')
		self.states['epsilon14'] = DEVSstate('epsilon14')
		self.states['epsilon15'] = DEVSstate('epsilon15')
		self.states['epsilon16'] = DEVSstate('epsilon16')
		self.states['epsilon17'] = DEVSstate('epsilon17')
		self.states['wait18'] = DEVSstate('wait18')
		self.states['epsilon19'] = DEVSstate('epsilon19')
		self.states['epsilon20'] = DEVSstate('epsilon20')
		self.states['epsilon21'] = DEVSstate('epsilon21')
		self.states['epsilon22'] = DEVSstate('epsilon22')
		self.states['epsilon23'] = DEVSstate('epsilon23')
		self.states['epsilon24'] = DEVSstate('epsilon24')
		self.states['epsilon25'] = DEVSstate('epsilon25')
		self.states['epsilon26'] = DEVSstate('epsilon26')
		self.states['epsilon27'] = DEVSstate('epsilon27')
		self.states['epsilon28'] = DEVSstate('epsilon28')
		self.states['wait29'] = DEVSstate('wait29')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'to G':
						return self.states['epsilon22']
					elif self.event == 'EXITALL':
						return self.states['epsilon16']
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon13'
						return self.states[temp]
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon21'
							self.current_child = None
						else:
							temp = 'epsilon20'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon13'
						return self.states[temp]
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon19'
							self.current_child = self.event.get_param('address')[0]
						[DUMP("Welcome to A state")]
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == 'wait18':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon17'
				else: temp = self.state.name
				[DUMP("Leave A state")]
				return self.states[temp]
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'epsilon21':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon20':
				return self.states['INSCOPE']
			elif self.state == 'epsilon23':
				[DUMP('Get out from A. Send "to A" or "to HS" to go back.')]
				return self.states['epsilon26']
			elif self.state == 'epsilon22':
				if (1):
					return self.states['epsilon23']
				else: return self.states['epsilon24']
			elif self.state == 'epsilon24':
				return self.states['INSCOPE']
			elif self.state == 'epsilon27':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon26':
				return self.states['wait29']
			elif self.state == 'epsilon28':
				return self.states['epsilon27']
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == 'wait29':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon28'
				else: temp = self.state.name
				[DUMP("Leave A state")]
				return self.states[temp]
			elif self.state == '__default_hook':
				return self.states['epsilon12']
			elif self.state == 'epsilon19':
				return self.states['INSCOPE']
			elif self.state == 'epsilon12':
				self.current_child = 'B'
				return self.states['INSCOPE']
			elif self.state == 'epsilon13':
				return self.states['INSCOPE']
			elif self.state == 'epsilon14':
				return self.states['INSCOPE']
			elif self.state == 'epsilon15':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon16':
				return self.states['wait18']
			elif self.state == 'epsilon17':
				return self.states['OUTSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'wait18':
			ta = INFINITY
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == 'epsilon21':
			ta = 0
		elif self.state == 'epsilon20':
			ta = 0
		elif self.state == 'epsilon23':
			ta = 0
		elif self.state == 'epsilon22':
			ta = 0
		elif self.state == 'epsilon25':
			ta = 0
		elif self.state == 'epsilon24':
			ta = 0
		elif self.state == 'epsilon27':
			ta = 0
		elif self.state == 'epsilon26':
			ta = 0
		elif self.state == 'epsilon28':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'wait29':
			ta = INFINITY
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon19':
			ta = 0
		elif self.state == 'epsilon12':
			ta = 0
		elif self.state == 'epsilon13':
			ta = 0
		elif self.state == 'epsilon14':
			ta = 0
		elif self.state == 'epsilon15':
			ta = 0
		elif self.state == 'epsilon16':
			ta = 0
		elif self.state == 'epsilon17':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon19':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon12':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['B'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon13':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon14':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon15':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon16':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon17':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'A')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon21':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon20':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon27':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'G'])
				event.set_param('return_address', ['_PARENT_', 'A'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon26':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon28':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', [self.current_child])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class RELAY_B_ATOMIC_31(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 2
		self.is_relay = 1
		self.current_child = None
		self.history = 'C'
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon31'] = DEVSstate('epsilon31')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon32'] = DEVSstate('epsilon32')
		self.states['epsilon33'] = DEVSstate('epsilon33')
		self.states['epsilon34'] = DEVSstate('epsilon34')
		self.states['epsilon35'] = DEVSstate('epsilon35')
		self.states['epsilon36'] = DEVSstate('epsilon36')
		self.states['wait37'] = DEVSstate('wait37')
		self.states['epsilon38'] = DEVSstate('epsilon38')
		self.states['epsilon39'] = DEVSstate('epsilon39')
		self.states['epsilon40'] = DEVSstate('epsilon40')
		self.states['epsilon41'] = DEVSstate('epsilon41')
		self.states['epsilon42'] = DEVSstate('epsilon42')
		self.states['epsilon43'] = DEVSstate('epsilon43')
		self.states['epsilon44'] = DEVSstate('epsilon44')
		self.states['epsilon45'] = DEVSstate('epsilon45')
		self.states['epsilon46'] = DEVSstate('epsilon46')
		self.states['epsilon47'] = DEVSstate('epsilon47')
		self.states['wait48'] = DEVSstate('wait48')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'to F':
						return self.states['epsilon41']
					elif self.event == 'EXITALL':
						return self.states['epsilon35']
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon32'
						return self.states[temp]
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon40'
							self.current_child = None
						else:
							temp = 'epsilon39'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon32'
						return self.states[temp]
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon38'
							self.current_child = self.event.get_param('address')[0]
						[DUMP("Welcome to B state")]
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'wait37':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon36'
				else: temp = self.state.name
				[DUMP("Leave B state")]
				return self.states[temp]
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == 'epsilon43':
				return self.states['INSCOPE']
			elif self.state == 'epsilon42':
				return self.states['epsilon45']
			elif self.state == 'epsilon41':
				if (1):
					return self.states['epsilon42']
				else: return self.states['epsilon43']
			elif self.state == 'epsilon40':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon47':
				return self.states['epsilon46']
			elif self.state == 'epsilon46':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon45':
				return self.states['wait48']
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == 'wait48':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon47'
				else: temp = self.state.name
				[DUMP("Leave B state")]
				return self.states[temp]
			elif self.state == '__default_hook':
				return self.states['epsilon31']
			elif self.state == 'epsilon32':
				return self.states['INSCOPE']
			elif self.state == 'epsilon33':
				return self.states['INSCOPE']
			elif self.state == 'epsilon31':
				self.current_child = 'C'
				return self.states['INSCOPE']
			elif self.state == 'epsilon36':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon34':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon35':
				return self.states['wait37']
			elif self.state == 'epsilon38':
				return self.states['INSCOPE']
			elif self.state == 'epsilon39':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'wait37':
			ta = INFINITY
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'epsilon43':
			ta = 0
		elif self.state == 'epsilon42':
			ta = 0
		elif self.state == 'epsilon41':
			ta = 0
		elif self.state == 'epsilon40':
			ta = 0
		elif self.state == 'epsilon47':
			ta = 0
		elif self.state == 'epsilon46':
			ta = 0
		elif self.state == 'epsilon45':
			ta = 0
		elif self.state == 'epsilon44':
			ta = 0
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'wait48':
			ta = INFINITY
		elif self.state == 'epsilon32':
			ta = 0
		elif self.state == 'epsilon33':
			ta = 0
		elif self.state == 'epsilon31':
			ta = 0
		elif self.state == 'epsilon36':
			ta = 0
		elif self.state == 'epsilon34':
			ta = 0
		elif self.state == 'epsilon35':
			ta = 0
		elif self.state == 'epsilon38':
			ta = 0
		elif self.state == 'epsilon39':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon40':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon47':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon45':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon32':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon33':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon31':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['C'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon36':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'B')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon34':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon35':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon46':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'F'])
				event.set_param('return_address', ['_PARENT_', 'B'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon38':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon39':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', [self.current_child])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class E(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 3.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon50'] = DEVSstate('epsilon50')
		self.states['epsilon51'] = DEVSstate('epsilon51')
		self.states['epsilon52'] = DEVSstate('epsilon52')
		self.states['epsilon53'] = DEVSstate('epsilon53')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon53']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon52']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon51']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon51':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon52':
				return self.states['INSCOPE']
			elif self.state == 'epsilon53':
				return self.states['OUTSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon50':
			ta = 0
		elif self.state == 'epsilon51':
			ta = 0
		elif self.state == 'epsilon52':
			ta = 0
		elif self.state == 'epsilon53':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon51':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon52':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon53':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'E')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class C(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 3.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon55'] = DEVSstate('epsilon55')
		self.states['epsilon56'] = DEVSstate('epsilon56')
		self.states['epsilon57'] = DEVSstate('epsilon57')
		self.states['epsilon58'] = DEVSstate('epsilon58')
		self.states['epsilon59'] = DEVSstate('epsilon59')
		self.states['epsilon60'] = DEVSstate('epsilon60')
		self.states['epsilon61'] = DEVSstate('epsilon61')
		self.states['epsilon62'] = DEVSstate('epsilon62')
		self.states['epsilon63'] = DEVSstate('epsilon63')
		self.states['epsilon64'] = DEVSstate('epsilon64')
		self.states['epsilon65'] = DEVSstate('epsilon65')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon58']
					elif self.event == 'to D':
						return self.states['epsilon59']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon57']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon56']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon56':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon57':
				return self.states['INSCOPE']
			elif self.state == 'epsilon61':
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon64':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon58':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon59':
				if (1):
					return self.states['epsilon60']
				else: return self.states['epsilon61']
			elif self.state == 'epsilon63':
				return self.states['epsilon64']
			elif self.state == 'epsilon60':
				[DUMP("Now we are in D")]
				[EVENT("to E")]
				return self.states['epsilon63']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon55':
			ta = 0
		elif self.state == 'epsilon56':
			ta = 0
		elif self.state == 'epsilon57':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon61':
			ta = 0
		elif self.state == 'epsilon65':
			ta = 0
		elif self.state == 'epsilon58':
			ta = 0
		elif self.state == 'epsilon59':
			ta = 0
		elif self.state == 'epsilon63':
			ta = 0
		elif self.state == 'epsilon60':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon64':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon62':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon64':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'D'])
				event.set_param('return_address', ['_PARENT_', 'C'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon56':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon57':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon58':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'C')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon63':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class D(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 3.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon67'] = DEVSstate('epsilon67')
		self.states['epsilon68'] = DEVSstate('epsilon68')
		self.states['epsilon69'] = DEVSstate('epsilon69')
		self.states['epsilon70'] = DEVSstate('epsilon70')
		self.states['epsilon71'] = DEVSstate('epsilon71')
		self.states['epsilon72'] = DEVSstate('epsilon72')
		self.states['epsilon73'] = DEVSstate('epsilon73')
		self.states['epsilon74'] = DEVSstate('epsilon74')
		self.states['epsilon75'] = DEVSstate('epsilon75')
		self.states['epsilon76'] = DEVSstate('epsilon76')
		self.states['epsilon77'] = DEVSstate('epsilon77')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon70']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon69']
					elif self.event == 'to E':
						return self.states['epsilon71']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon68']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon69':
				return self.states['INSCOPE']
			elif self.state == 'epsilon68':
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon75':
				return self.states['epsilon76']
			elif self.state == 'epsilon72':
				[DUMP("Immediately go to E")]
				return self.states['epsilon75']
			elif self.state == 'epsilon73':
				return self.states['INSCOPE']
			elif self.state == 'epsilon70':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon71':
				if (1):
					return self.states['epsilon72']
				else: return self.states['epsilon73']
			elif self.state == 'epsilon76':
				return self.states['OUTSCOPE']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon76':
			ta = 0
		elif self.state == 'epsilon74':
			ta = 0
		elif self.state == 'epsilon69':
			ta = 0
		elif self.state == 'epsilon68':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon77':
			ta = 0
		elif self.state == 'epsilon67':
			ta = 0
		elif self.state == 'epsilon75':
			ta = 0
		elif self.state == 'epsilon72':
			ta = 0
		elif self.state == 'epsilon73':
			ta = 0
		elif self.state == 'epsilon70':
			ta = 0
		elif self.state == 'epsilon71':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon76':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'E'])
				event.set_param('return_address', ['_PARENT_', 'D'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon75':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon69':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon68':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon70':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'D')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class B(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 2
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_B_ATOMIC_31())
		self.E=self.addSubModel(E())
		self.C=self.addSubModel(C())
		self.D=self.addSubModel(D())
		self.relay.ports['E'] = self.relay.addOutPort('E')
		self.relay.ports['C'] = self.relay.addOutPort('C')
		self.relay.ports['D'] = self.relay.addOutPort('D')
		self.connectPorts(self.relay.ports['E'], self.E.ports['_IN_'])
		self.connectPorts(self.E.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.E.ports['_IN_'])
		self.connectPorts(self.relay.ports['C'], self.C.ports['_IN_'])
		self.connectPorts(self.C.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.C.ports['_IN_'])
		self.connectPorts(self.relay.ports['D'], self.D.ports['_IN_'])
		self.connectPorts(self.D.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.D.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
class RELAY_F_ATOMIC_79(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 2
		self.is_relay = 1
		self.current_child = None
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon79'] = DEVSstate('epsilon79')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon80'] = DEVSstate('epsilon80')
		self.states['epsilon81'] = DEVSstate('epsilon81')
		self.states['epsilon82'] = DEVSstate('epsilon82')
		self.states['epsilon83'] = DEVSstate('epsilon83')
		self.states['epsilon84'] = DEVSstate('epsilon84')
		self.states['wait85'] = DEVSstate('wait85')
		self.states['wait86'] = DEVSstate('wait86')
		self.states['epsilon87'] = DEVSstate('epsilon87')
		self.states['epsilon88'] = DEVSstate('epsilon88')
		self.states['epsilon89'] = DEVSstate('epsilon89')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon83']
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon89'
							self.current_child = None
						else:
							temp = 'epsilon88'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon80'
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon87'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon80'
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon84':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon89':
				return self.states['OUTSCOPE']
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'epsilon79':
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'wait86':
				if get_from_Q(self.Q, 'EXITACK') != None: temp = 'epsilon84'
				else: temp = self.state.name
				return self.states[temp]
			elif self.state == 'epsilon83':
				return self.states['wait85']
			elif self.state == 'epsilon82':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon81':
				return self.states['INSCOPE']
			elif self.state == 'epsilon80':
				return self.states['INSCOPE']
			elif self.state == 'wait85':
				if get_from_Q(self.Q, 'EXITACK') != None: return self.states['wait86']
				else: return self.state
			elif self.state == 'epsilon87':
				return self.states['INSCOPE']
			elif self.state == '__default_hook':
				return self.states['epsilon79']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon88':
				return self.states['INSCOPE']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'wait85':
			ta = INFINITY
		elif self.state == 'wait86':
			ta = INFINITY
		elif self.state == 'epsilon89':
			ta = 0
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == 'epsilon79':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == 'epsilon84':
			ta = 0
		elif self.state == 'epsilon83':
			ta = 0
		elif self.state == 'epsilon82':
			ta = 0
		elif self.state == 'epsilon81':
			ta = 0
		elif self.state == 'epsilon80':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon87':
			ta = 0
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon88':
			ta = 0
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon89':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon79':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_ALL_'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon87':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon84':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'F')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon83':
			def __outputFnc(self):
				event = DEVSevent('EXITALL')
				event.set_param('address', ['_ALL_'])
				event.set_param('broadcast', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon82':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon81':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon80':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon88':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', ['_ALL_'])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class RELAY_F1_ATOMIC_91(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 3
		self.is_relay = 1
		self.current_child = None
		self.history = 'F1a'
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon91'] = DEVSstate('epsilon91')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon92'] = DEVSstate('epsilon92')
		self.states['epsilon93'] = DEVSstate('epsilon93')
		self.states['epsilon94'] = DEVSstate('epsilon94')
		self.states['epsilon95'] = DEVSstate('epsilon95')
		self.states['epsilon96'] = DEVSstate('epsilon96')
		self.states['wait97'] = DEVSstate('wait97')
		self.states['epsilon98'] = DEVSstate('epsilon98')
		self.states['epsilon99'] = DEVSstate('epsilon99')
		self.states['epsilon100'] = DEVSstate('epsilon100')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon95']
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon100'
							self.current_child = None
						else:
							temp = 'epsilon99'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon92'
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon98'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon92'
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon91':
				self.current_child = 'F1a'
				return self.states['INSCOPE']
			elif self.state == 'epsilon92':
				return self.states['INSCOPE']
			elif self.state == 'epsilon93':
				return self.states['INSCOPE']
			elif self.state == 'epsilon94':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon95':
				return self.states['wait97']
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'epsilon96':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon98':
				return self.states['INSCOPE']
			elif self.state == 'epsilon99':
				return self.states['INSCOPE']
			elif self.state == 'wait97':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon96'
				else: temp = self.state.name
				return self.states[temp]
			elif self.state == '__default_hook':
				return self.states['epsilon91']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon100':
				return self.states['OUTSCOPE']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon91':
			ta = 0
		elif self.state == 'epsilon92':
			ta = 0
		elif self.state == 'epsilon93':
			ta = 0
		elif self.state == 'epsilon94':
			ta = 0
		elif self.state == 'epsilon95':
			ta = 0
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == 'epsilon96':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon98':
			ta = 0
		elif self.state == 'epsilon99':
			ta = 0
		elif self.state == 'wait97':
			ta = INFINITY
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon100':
			ta = 0
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon91':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['F1a'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon92':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon93':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon94':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon95':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon98':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon96':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'F1')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon99':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon100':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', [self.current_child])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F1a(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 4.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon102'] = DEVSstate('epsilon102')
		self.states['epsilon103'] = DEVSstate('epsilon103')
		self.states['epsilon104'] = DEVSstate('epsilon104')
		self.states['epsilon105'] = DEVSstate('epsilon105')
		self.states['epsilon106'] = DEVSstate('epsilon106')
		self.states['epsilon107'] = DEVSstate('epsilon107')
		self.states['epsilon108'] = DEVSstate('epsilon108')
		self.states['epsilon109'] = DEVSstate('epsilon109')
		self.states['epsilon110'] = DEVSstate('epsilon110')
		self.states['epsilon111'] = DEVSstate('epsilon111')
		self.states['epsilon112'] = DEVSstate('epsilon112')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		if not self.timeout and round(self.elapsed_since_inscope, 6) >= 1.0:
			self.Q.append(EVENT('_TIMEOUT_'))
			self.elapsed_since_inscope = 0
			self.timeout = 1
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == '_TIMEOUT_':
						return self.states['epsilon106']
					elif self.event == 'EXITALL':
						return self.states['epsilon105']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon104']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon103']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon110':
				return self.states['epsilon111']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon108':
				return self.states['INSCOPE']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon103':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon111':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon105':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon104':
				return self.states['INSCOPE']
			elif self.state == 'epsilon107':
				return self.states['epsilon110']
			elif self.state == 'epsilon106':
				if (1):
					return self.states['epsilon107']
				else: return self.states['epsilon108']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon111':
			ta = 0
		elif self.state == 'epsilon110':
			ta = 0
		elif self.state == 'epsilon108':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon112':
			ta = 0
		elif self.state == 'epsilon104':
			ta = 0
		elif self.state == 'epsilon109':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon103':
			ta = 0
		elif self.state == 'epsilon102':
			ta = 0
		elif self.state == 'epsilon105':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon107':
			ta = 0
		elif self.state == 'epsilon106':
			ta = 0
		else: ta = INFINITY
		if self.inscope and not self.timeout:
			ta_after = max(0, 1.0-self.elapsed_since_inscope)
		else:
			ta_after = INFINITY
		return minEx(ta, ta_after)
	def outputFnc(self):
		if self.state == 'epsilon103':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon111':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'F1b'])
				event.set_param('return_address', ['_PARENT_', 'F1a'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon105':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'F1a')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon104':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon110':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F1b(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 4.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon114'] = DEVSstate('epsilon114')
		self.states['epsilon115'] = DEVSstate('epsilon115')
		self.states['epsilon116'] = DEVSstate('epsilon116')
		self.states['epsilon117'] = DEVSstate('epsilon117')
		self.states['epsilon118'] = DEVSstate('epsilon118')
		self.states['epsilon119'] = DEVSstate('epsilon119')
		self.states['epsilon120'] = DEVSstate('epsilon120')
		self.states['epsilon121'] = DEVSstate('epsilon121')
		self.states['epsilon122'] = DEVSstate('epsilon122')
		self.states['epsilon123'] = DEVSstate('epsilon123')
		self.states['epsilon124'] = DEVSstate('epsilon124')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		if not self.timeout and round(self.elapsed_since_inscope, 6) >= 1.0:
			self.Q.append(EVENT('_TIMEOUT_'))
			self.elapsed_since_inscope = 0
			self.timeout = 1
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == '_TIMEOUT_':
						return self.states['epsilon118']
					elif self.event == 'EXITALL':
						return self.states['epsilon117']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon116']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon115']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon120':
				return self.states['INSCOPE']
			elif self.state == 'epsilon123':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon122':
				return self.states['epsilon123']
			elif self.state == 'epsilon118':
				if (1):
					return self.states['epsilon119']
				else: return self.states['epsilon120']
			elif self.state == 'epsilon119':
				return self.states['epsilon122']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon116':
				return self.states['INSCOPE']
			elif self.state == 'epsilon117':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon115':
				return self.states['OUTSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon122':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon120':
			ta = 0
		elif self.state == 'epsilon121':
			ta = 0
		elif self.state == 'epsilon117':
			ta = 0
		elif self.state == 'epsilon123':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon118':
			ta = 0
		elif self.state == 'epsilon119':
			ta = 0
		elif self.state == 'epsilon124':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon116':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon114':
			ta = 0
		elif self.state == 'epsilon115':
			ta = 0
		else: ta = INFINITY
		if self.inscope and not self.timeout:
			ta_after = max(0, 1.0-self.elapsed_since_inscope)
		else:
			ta_after = INFINITY
		return minEx(ta, ta_after)
	def outputFnc(self):
		if self.state == 'epsilon123':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'F1a'])
				event.set_param('return_address', ['_PARENT_', 'F1b'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon122':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon116':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon117':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'F1b')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon115':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F1(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 3
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_F1_ATOMIC_91())
		self.F1a=self.addSubModel(F1a())
		self.F1b=self.addSubModel(F1b())
		self.relay.ports['F1a'] = self.relay.addOutPort('F1a')
		self.relay.ports['F1b'] = self.relay.addOutPort('F1b')
		self.connectPorts(self.relay.ports['F1a'], self.F1a.ports['_IN_'])
		self.connectPorts(self.F1a.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F1a.ports['_IN_'])
		self.connectPorts(self.relay.ports['F1b'], self.F1b.ports['_IN_'])
		self.connectPorts(self.F1b.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F1b.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
class RELAY_F2_ATOMIC_126(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 3
		self.is_relay = 1
		self.current_child = None
		self.history = 'F2a'
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['__default_hook'] = DEVSstate('__default_hook')
		self.states['epsilon126'] = DEVSstate('epsilon126')
		self.states['__history_hook'] = DEVSstate('__history_hook')
		self.states['__history_star_hook'] = DEVSstate('__history_star_hook')
		self.states['__alpha_relay_hook'] = DEVSstate('__alpha_relay_hook')
		self.states['__relay_hook'] = DEVSstate('__relay_hook')
		self.states['__broadcast_hook'] = DEVSstate('__broadcast_hook')
		self.states['epsilon127'] = DEVSstate('epsilon127')
		self.states['epsilon128'] = DEVSstate('epsilon128')
		self.states['epsilon129'] = DEVSstate('epsilon129')
		self.states['epsilon130'] = DEVSstate('epsilon130')
		self.states['epsilon131'] = DEVSstate('epsilon131')
		self.states['wait132'] = DEVSstate('wait132')
		self.states['epsilon133'] = DEVSstate('epsilon133')
		self.states['epsilon134'] = DEVSstate('epsilon134')
		self.states['epsilon135'] = DEVSstate('epsilon135')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'EXITALL':
						return self.states['epsilon130']
					elif self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: temp = 'INSCOPE'
						elif self.event.get_param('address')[0] == '_PARENT_':
							temp = 'epsilon135'
							self.current_child = None
						else:
							temp = 'epsilon134'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon127'
						return self.states[temp]
					elif len(self.event.get_param('address')) == 0:
						if self.event.get_param('broadcast') == 'TRUE': return '__broadcast_hook'
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'ENTER':
						if len(self.event.get_param('address')) == 0: # REACHED DESTINATION
							self.return_address = self.event.get_param('return_address')
							if self.event.get_param('history') == 'TRUE':
								if self.event.get_param('broadcast') == 'TRUE': temp = '__history_star_hook'
								else: temp = '__history_hook'
							else: temp = '__default_hook'
						else:
							temp = 'epsilon133'
							self.current_child = self.event.get_param('address')[0]
						return self.states[temp]
					elif self.event == 'CSQ':
						if len(self.event.get_param('address')) > 0:
							temp = 'epsilon127'
						return self.states[temp]
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon133':
				return self.states['INSCOPE']
			elif self.state == '__history_star_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == '__relay_hook':
				return self.states['INSCOPE']
			elif self.state == '__history_hook':
				self.current_child = self.history
				return self.states['INSCOPE']
			elif self.state == 'epsilon130':
				return self.states['wait132']
			elif self.state == 'wait132':
				event = get_from_Q(self.Q, 'EXITACK')
				if event != None:
					self.history = event.get_param('history_state')
					temp = 'epsilon131'
				else: temp = self.state.name
				return self.states[temp]
			elif self.state == 'epsilon134':
				return self.states['INSCOPE']
			elif self.state == 'epsilon127':
				return self.states['INSCOPE']
			elif self.state == 'epsilon126':
				self.current_child = 'F2a'
				return self.states['INSCOPE']
			elif self.state == '__default_hook':
				return self.states['epsilon126']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon135':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon129':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon128':
				return self.states['INSCOPE']
			elif self.state == '__alpha_relay_hook':
				return self.states[self.restore]
			elif self.state == 'epsilon131':
				return self.states['OUTSCOPE']
			elif self.state == '__broadcast_hook':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon133':
			ta = 0
		elif self.state == '__history_star_hook':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == '__relay_hook':
			ta = 0
		elif self.state == '__history_hook':
			ta = 0
		elif self.state == 'epsilon130':
			ta = 0
		elif self.state == 'wait132':
			ta = INFINITY
		elif self.state == 'epsilon134':
			ta = 0
		elif self.state == 'epsilon131':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon127':
			ta = 0
		elif self.state == 'epsilon126':
			ta = 0
		elif self.state == '__default_hook':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon135':
			ta = 0
		elif self.state == 'epsilon129':
			ta = 0
		elif self.state == 'epsilon128':
			ta = 0
		elif self.state == '__alpha_relay_hook':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == '__broadcast_hook':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon133':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_star_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('broadcast', 'TRUE')
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__history_hook':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', [self.history])
				event.set_param('history', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon130':
			def __outputFnc(self):
				return DEVSevent('EXITALL', [('address', [self.current_child]), ('broadcast', 'TRUE')])
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon127':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon126':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['F2a'])
				event.set_param('return_address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon134':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon135':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon129':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon128':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.event.get_param('from_address'))
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__alpha_relay_hook':
			def __outputFnc(self):
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon131':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('address', ['_PARENT_'])
				event.set_param('history_state', 'F2')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == '__broadcast_hook':
			def __outputFnc(self):
				self.event.set_param('address', [self.current_child])
				self.event.set_param('broadcast', 'TRUE')
				return self.event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F2a(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 4.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon137'] = DEVSstate('epsilon137')
		self.states['epsilon138'] = DEVSstate('epsilon138')
		self.states['epsilon139'] = DEVSstate('epsilon139')
		self.states['epsilon140'] = DEVSstate('epsilon140')
		self.states['epsilon141'] = DEVSstate('epsilon141')
		self.states['epsilon142'] = DEVSstate('epsilon142')
		self.states['epsilon143'] = DEVSstate('epsilon143')
		self.states['epsilon144'] = DEVSstate('epsilon144')
		self.states['epsilon145'] = DEVSstate('epsilon145')
		self.states['epsilon146'] = DEVSstate('epsilon146')
		self.states['epsilon147'] = DEVSstate('epsilon147')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		if not self.timeout and round(self.elapsed_since_inscope, 6) >= 2.0:
			self.Q.append(EVENT('_TIMEOUT_'))
			self.elapsed_since_inscope = 0
			self.timeout = 1
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == '_TIMEOUT_':
						return self.states['epsilon141']
					elif self.event == 'EXITALL':
						return self.states['epsilon140']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon139']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon138']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon145':
				return self.states['epsilon146']
			elif self.state == 'epsilon146':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon141':
				if (1):
					return self.states['epsilon142']
				else: return self.states['epsilon143']
			elif self.state == 'epsilon139':
				return self.states['INSCOPE']
			elif self.state == 'epsilon143':
				return self.states['INSCOPE']
			elif self.state == 'epsilon142':
				return self.states['epsilon145']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon138':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon140':
				return self.states['OUTSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon144':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon145':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon147':
			ta = 0
		elif self.state == 'epsilon146':
			ta = 0
		elif self.state == 'epsilon138':
			ta = 0
		elif self.state == 'epsilon139':
			ta = 0
		elif self.state == 'epsilon143':
			ta = 0
		elif self.state == 'epsilon142':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon141':
			ta = 0
		elif self.state == 'epsilon137':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon140':
			ta = 0
		else: ta = INFINITY
		if self.inscope and not self.timeout:
			ta_after = max(0, 2.0-self.elapsed_since_inscope)
		else:
			ta_after = INFINITY
		return minEx(ta, ta_after)
	def outputFnc(self):
		if self.state == 'epsilon145':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon146':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'F2b'])
				event.set_param('return_address', ['_PARENT_', 'F2a'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon138':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon139':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon140':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'F2a')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F2b(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 4.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon149'] = DEVSstate('epsilon149')
		self.states['epsilon150'] = DEVSstate('epsilon150')
		self.states['epsilon151'] = DEVSstate('epsilon151')
		self.states['epsilon152'] = DEVSstate('epsilon152')
		self.states['epsilon153'] = DEVSstate('epsilon153')
		self.states['epsilon154'] = DEVSstate('epsilon154')
		self.states['epsilon155'] = DEVSstate('epsilon155')
		self.states['epsilon156'] = DEVSstate('epsilon156')
		self.states['epsilon157'] = DEVSstate('epsilon157')
		self.states['epsilon158'] = DEVSstate('epsilon158')
		self.states['epsilon159'] = DEVSstate('epsilon159')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		if not self.timeout and round(self.elapsed_since_inscope, 6) >= 2.0:
			self.Q.append(EVENT('_TIMEOUT_'))
			self.elapsed_since_inscope = 0
			self.timeout = 1
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == '_TIMEOUT_':
						return self.states['epsilon153']
					elif self.event == 'EXITALL':
						return self.states['epsilon152']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon151']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon150']
					elif self.event == 'ENTER':
						return self.states['INSCOPE']
				return self.states['OUTSCOPE']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon157':
				return self.states['epsilon158']
			elif self.state == 'epsilon154':
				return self.states['epsilon157']
			elif self.state == 'epsilon155':
				return self.states['INSCOPE']
			elif self.state == 'epsilon152':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon153':
				if (1):
					return self.states['epsilon154']
				else: return self.states['epsilon155']
			elif self.state == 'epsilon150':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon151':
				return self.states['INSCOPE']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon158':
				return self.states['OUTSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon157':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon156':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon154':
			ta = 0
		elif self.state == 'epsilon155':
			ta = 0
		elif self.state == 'epsilon152':
			ta = 0
		elif self.state == 'epsilon153':
			ta = 0
		elif self.state == 'epsilon150':
			ta = 0
		elif self.state == 'epsilon151':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon149':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		elif self.state == 'epsilon158':
			ta = 0
		elif self.state == 'epsilon159':
			ta = 0
		else: ta = INFINITY
		if self.inscope and not self.timeout:
			ta_after = max(0, 2.0-self.elapsed_since_inscope)
		else:
			ta_after = INFINITY
		return minEx(ta, ta_after)
	def outputFnc(self):
		if self.state == 'epsilon157':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon152':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'F2b')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon158':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'F2a'])
				event.set_param('return_address', ['_PARENT_', 'F2b'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon150':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon151':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class F2(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 3
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_F2_ATOMIC_126())
		self.F2a=self.addSubModel(F2a())
		self.F2b=self.addSubModel(F2b())
		self.relay.ports['F2a'] = self.relay.addOutPort('F2a')
		self.relay.ports['F2b'] = self.relay.addOutPort('F2b')
		self.connectPorts(self.relay.ports['F2a'], self.F2a.ports['_IN_'])
		self.connectPorts(self.F2a.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F2a.ports['_IN_'])
		self.connectPorts(self.relay.ports['F2b'], self.F2b.ports['_IN_'])
		self.connectPorts(self.F2b.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F2b.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
class F(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 2
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_F_ATOMIC_79())
		self.F1=self.addSubModel(F1())
		self.F2=self.addSubModel(F2())
		self.relay.ports['F1'] = self.relay.addOutPort('F1')
		self.relay.ports['F2'] = self.relay.addOutPort('F2')
		self.connectPorts(self.relay.ports['F1'], self.F1.ports['_IN_'])
		self.connectPorts(self.F1.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F1.ports['_IN_'])
		self.connectPorts(self.relay.ports['F2'], self.F2.ports['_IN_'])
		self.connectPorts(self.F2.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F2.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
class A(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 1
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_A_ATOMIC_12())
		self.B=self.addSubModel(B())
		self.F=self.addSubModel(F())
		self.relay.ports['B'] = self.relay.addOutPort('B')
		self.relay.ports['F'] = self.relay.addOutPort('F')
		self.connectPorts(self.relay.ports['B'], self.B.ports['_IN_'])
		self.connectPorts(self.B.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.B.ports['_IN_'])
		self.connectPorts(self.relay.ports['F'], self.F.ports['_IN_'])
		self.connectPorts(self.F.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.F.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
class G(AtomicDEVS):
	def __init__(self):
		AtomicDEVS.__init__(self)
		self.scope = 1.5
		self.is_relay = 0
		self.Q = []
		self.delta_ext = 0
		self.inscope = 0
		self.timeout = 0
		self.elapsed_since_inscope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.states = {}
		self.states['INSCOPE'] = DEVSstate('INSCOPE')
		self.states['OUTSCOPE'] = DEVSstate('OUTSCOPE')
		self.states['INSCOPE_DQ'] = DEVSstate('INSCOPE_DQ')
		self.states['OUTSCOPE_DQ'] = DEVSstate('OUTSCOPE_DQ')
		self.states['epsilon161'] = DEVSstate('epsilon161')
		self.states['epsilon162'] = DEVSstate('epsilon162')
		self.states['epsilon163'] = DEVSstate('epsilon163')
		self.states['epsilon164'] = DEVSstate('epsilon164')
		self.states['epsilon165'] = DEVSstate('epsilon165')
		self.states['epsilon166'] = DEVSstate('epsilon166')
		self.states['epsilon167'] = DEVSstate('epsilon167')
		self.states['epsilon168'] = DEVSstate('epsilon168')
		self.states['epsilon169'] = DEVSstate('epsilon169')
		self.states['epsilon170'] = DEVSstate('epsilon170')
		self.states['epsilon171'] = DEVSstate('epsilon171')
		self.states['epsilon172'] = DEVSstate('epsilon172')
		self.states['epsilon173'] = DEVSstate('epsilon173')
		self.states['epsilon174'] = DEVSstate('epsilon174')
		self.states['epsilon175'] = DEVSstate('epsilon175')
		self.states['epsilon176'] = DEVSstate('epsilon176')
		self.states['epsilon177'] = DEVSstate('epsilon177')
		self.states['epsilon178'] = DEVSstate('epsilon178')
		self.state = self.states['OUTSCOPE']
	def extTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		event = self.peek(self.ports['_IN_'])
		if event == 'ENTER' or event == 'EXITALL' or event == 'EXITACK':
			if len(event.get_param('address')) > 0:
				if event.get_param('address')[0] != '_PARENT_':
					if self.state.name == 'OUTSCOPE': self.restore = 'INSCOPE'
					else: self.restore = self.state.name
					self.event = event; self.current_child = event.get_param('address')[0]; return '__alpha_relay_hook'
		self.Q.append(event)
		self.delta_ext = 1
		return self.state
	def intTransition(self):
		if self.inscope: self.elapsed_since_inscope += self.elapsed
		else: self.elapsed_since_inscope = 0
		def get_new_state():
			if self.state == 'INSCOPE_DQ':
				while len(self.Q) > 0:
					self.event=self.Q[0];del self.Q[0]
					if self.event == 'to HS':
						return self.states['epsilon172']
					elif self.event == 'to A':
						return self.states['epsilon165']
					elif self.event == 'EXITALL':
						return self.states['epsilon164']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon163']
					elif len(self.event.get_param('address')) == 0:
						pass
					else: return '__relay_hook'
				return self.states['INSCOPE']
			elif self.state == 'OUTSCOPE_DQ':
				while len(self.Q) > 0:

					self.event=self.Q[0];del self.Q[0]
					if self.event == 'ENTER':
						return self.states['INSCOPE']
					elif self.event == 'CSQ':
						self.from_address = self.event.get_param('from_address')
						return self.states['epsilon162']
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon173':
				[DUMP("Go back to history state of A")]
				return self.states['epsilon176']
			elif self.state == 'epsilon169':
				return self.states['epsilon170']
			elif self.state == 'OUTSCOPE':
				return self.states['OUTSCOPE_DQ']
			elif self.state == 'epsilon166':
				[DUMP("Go back to default substate of A")]
				return self.states['epsilon169']
			elif self.state == 'epsilon165':
				if (1):
					return self.states['epsilon166']
				else: return self.states['epsilon167']
			elif self.state == 'epsilon164':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon163':
				return self.states['INSCOPE']
			elif self.state == 'epsilon162':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon176':
				return self.states['epsilon177']
			elif self.state == 'epsilon177':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon170':
				return self.states['OUTSCOPE']
			elif self.state == 'epsilon172':
				if (1):
					return self.states['epsilon173']
				else: return self.states['epsilon174']
			elif self.state == 'epsilon174':
				return self.states['INSCOPE']
			elif self.state == 'INSCOPE':
				return self.states['INSCOPE_DQ']
			elif self.state == 'epsilon167':
				return self.states['INSCOPE']
			else: return self.state
		new_state = get_new_state()
		if new_state == 'INSCOPE':
			self.inscope = 1
			if len(self.Q) == 0: self.timeout = 0
		elif new_state == 'OUTSCOPE':
			self.inscope = 0
			if len(self.Q) == 0: self.timeout = 0
		return new_state
	def timeAdvance(self):
		if self.state == 'INSCOPE' and len(self.Q) > 0: ta = 0
		elif self.state == 'OUTSCOPE' and len(self.Q) > 0: ta = 0
		elif self.delta_ext: ta = 0;self.delta_ext=0
		elif self.state == 'epsilon178':
			ta = 0
		elif self.state == 'OUTSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon171':
			ta = 0
		elif self.state == 'epsilon172':
			ta = 0
		elif self.state == 'epsilon173':
			ta = 0
		elif self.state == 'epsilon174':
			ta = 0
		elif self.state == 'epsilon175':
			ta = 0
		elif self.state == 'epsilon176':
			ta = 0
		elif self.state == 'epsilon177':
			ta = 0
		elif self.state == 'INSCOPE':
			ta = INFINITY
		elif self.state == 'epsilon170':
			ta = 0
		elif self.state == 'epsilon169':
			ta = 0
		elif self.state == 'epsilon168':
			ta = 0
		elif self.state == 'epsilon167':
			ta = 0
		elif self.state == 'epsilon166':
			ta = 0
		elif self.state == 'epsilon165':
			ta = 0
		elif self.state == 'epsilon164':
			ta = 0
		elif self.state == 'epsilon163':
			ta = 0
		elif self.state == 'epsilon162':
			ta = 0
		elif self.state == 'epsilon161':
			ta = 0
		elif self.state == 'OUTSCOPE_DQ':
			ta = 0
		elif self.state == 'INSCOPE_DQ':
			ta = 0
		else: ta = INFINITY
		return ta
	def outputFnc(self):
		if self.state == 'epsilon169':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon170':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'A'])
				event.set_param('return_address', ['_PARENT_', 'G'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon164':
			def __outputFnc(self):
				event = DEVSevent('EXITACK')
				event.set_param('history_state', 'G')
				event.set_param('address', ['_PARENT_'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon163':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'TRUE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon162':
			def __outputFnc(self):
				event = DEVSevent('CSR')
				event.set_param('address', self.from_address)
				event.set_param('value', 'FALSE')
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon176':
			def __outputFnc(self):
				# return an instance of DEVSevent or None
				return None
				
				
				
				
				
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
		elif self.state == 'epsilon177':
			def __outputFnc(self):
				event = DEVSevent('ENTER')
				event.set_param('address', ['_PARENT_', 'A'])
				event.set_param('history', 'TRUE')
				event.set_param('broadcast', 'TRUE')
				event.set_param('return_address', ['_PARENT_', 'G'])
				return event
			event = __outputFnc(self)
			if event != None:
				port_name = event.get_param('address')[0]
				del event.get_param('address')[0]
				self.poke(self.ports[port_name], event)
class ROOT(CoupledDEVS):
	def __init__(self):
		CoupledDEVS.__init__(self)
		self.scope = 0
		self.ports = {}
		self.ports['_IN_'] = self.addInPort('_IN_')
		self.ports['_PARENT_'] = self.addOutPort('_PARENT_')
		self.ports['_ALL_'] = self.addOutPort('_ALL_')
		self.relay=self.addSubModel(RELAY_ROOT_ATOMIC_1())
		self.A=self.addSubModel(A())
		self.G=self.addSubModel(G())
		self.relay.ports['A'] = self.relay.addOutPort('A')
		self.relay.ports['G'] = self.relay.addOutPort('G')
		self.connectPorts(self.relay.ports['A'], self.A.ports['_IN_'])
		self.connectPorts(self.A.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.A.ports['_IN_'])
		self.connectPorts(self.relay.ports['G'], self.G.ports['_IN_'])
		self.connectPorts(self.G.ports['_PARENT_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_ALL_'], self.G.ports['_IN_'])
		self.connectPorts(self.ports['_IN_'], self.relay.ports['_IN_'])
		self.connectPorts(self.relay.ports['_PARENT_'], self.ports['_PARENT_'])
	def select(self, imm): return choose(self, imm)
