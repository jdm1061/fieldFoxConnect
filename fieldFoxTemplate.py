# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:59:46 2019

@author: MARTIJ

template script for connecting to field fox
"""

import pyvisa

#### =============================================================================
#### Input Parameters
#### =============================================================================

### leave all values as strings
### e3 for kHz, e6 for MHz
ff_ip = '10.169.7.49'   ###IP address
ff_cf = '10e6'          ### center frequency 
ff_span = '10e6'       ### span 
ff_res = '300e3'        ### resolution bandwidth manual setting
ff_vbw = '100e3'        ### video bandwidth



#### =============================================================================
#### Transmit commands to the Field Fox
#### =============================================================================

### opens connection to field fox and enters parameters from above
ffsa = pyvisa.ResourceManager() 
SA = ffsa.open_resource('TCPIP0::'+ff_ip+'::inst0::INSTR')
SA.timeout = 5000
SA.write('FREQuency:CENTer '+ff_cf)
SA.write('FREQ:SPAN '+ff_span)
SA.write('BAND '+ff_res)
SA.write('BAND:VID '+ff_vbw)

### closes connection to field fox at completion of program
SA.close()
ffsa.close()
