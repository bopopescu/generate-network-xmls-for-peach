
'''
Test Monitors

@author: Michael Eddington
@version: $Id: test.py 780 2008-03-23 02:58:49Z meddingt $
'''

#
# Copyright (c) 2007 Michael Eddington
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in	
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

# Authors:
#   Michael Eddington (mike@phed.org)

# $Id: test.py 780 2008-03-23 02:58:49Z meddingt $

import sys, random
from Peach.agent import Monitor

class Test(Monitor):
	pass

class TestFault(Monitor):
	
	def DetectedFault(self):
		'''
		Check if a fault was detected.
		'''
		ret = random.choice([False, False, False, True])
		
		if ret:
			print "TestFault: Returning True"
		else:
			print "TestFault: Returning False"
		
		#return ret
		return False
	
	def StopRun(self):
		ret = random.choice([False, False, False, True])
		
		if ret:
			print "TestFault: StopRun: Returning True"
		else:
			print "TestFault: StopRun: Returning False"
		
		return ret
	
class TestStopOnFirst(Monitor):
	'''
	Will force a stop after 1 test case
	'''
	
	def StopRun(self):
		return True
	

# end
