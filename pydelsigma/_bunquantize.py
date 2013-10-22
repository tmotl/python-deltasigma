# -*- coding: utf-8 -*-
# _bunquantize.py
# Module providing the bunquantize function
# Copyright 2013 Giuseppe Venturini
# This file is part of python-deltasigma.
#
# python-deltasigma is a 1:1 Python replacement of Richard Schreier's 
# MATLAB delta sigma toolbox (aka "delsigma"), upon which it is heavily based.
# The delta sigma toolbox is (c) 2009, Richard Schreier.
#
# python-deltasigma is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for the licensing terms.

"""Module providing the bunquantize() function
"""

import numpy as np
from ._utils import carray

def bunquantize(q):
	""" Calculate the value corresponding to a bidirectionally quantized quantity.
	
	q is a (2 n, m) ndarray containing the powers of 2 and their signs for each
	quantized value.
	
	See also bquantize in _bunquantize.py
	"""

	tns = len(q)
	#n = q.shape[0]/2.
	y = []
	for qi in q:
		y += [(qi[1:qi.shape[0]+1:2, :]*2.**qi[:qi.shape[0]:2, :]).sum()]
	return carray(y)

def test_bunquantize():
	"""Unit test for bunquantize()
	"""
	from ._bquantize import bquantize
	x = np.linspace(-10, 10, 101)
	yr = bquantize(x)
	yv = []
	y = []
	for yi in yr:
		y += [yi.csd]
		yv += [yi.val]
	yv = carray(yv)
	xres = bunquantize(y)
	assert np.allclose(xres, yv, atol=1e-8, rtol=1e-5)

if __name__ == '__main__':
	test_bunquantize()
