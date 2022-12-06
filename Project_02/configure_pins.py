#!/bin/bash
# --------------------------------------------------------------------------
# Light Table - Configure Pins
# --------------------------------------------------------------------------
# License:   
# Copyright 2022 Singrhu Poltanawasit
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------
# 
# Configure pins for Light Table:
#   - Photodiode
# 	- Button
#   - LEDs (Red / Green)
# 
# --------------------------------------------------------------------------
# Photodiodes
config-pin P1_08 gpio #SPI CLK
config-pin P1_10 gpio #SPI MISO
config-pin P1_12 gpio #SPI MOSI

config-pin P1_29 gpio #ADC 1
config-pin P1_31 gpio #ADC 2
config-pin P1_33 gpio #ADC 3
config-pin P1_35 gpio #ADC 4
config-pin P1_02 gpio #ADC 5


# Button
config-pin P2_02 gpio

# 25 LEDs
config-pin P2_04 gpio #LED 1x1
config-pin P2_06 gpio #LED 1x2
config-pin P2_08 gpio #LED 1x3
config-pin P2_10 gpio #LED 1x4
config-pin P2_18 gpio #LED 1x5

config-pin P2_20 gpio #LED 2x1
config-pin P2_22 gpio #LED 2x2
config-pin P2_24 gpio #LED 2x3
config-pin P2_28 gpio #LED 2x4
config-pin P2_30 gpio #LED 2x5

config-pin P2_32 gpio #LED 3x1
config-pin P2_34 gpio #LED 3x2
config-pin P2_17 gpio #LED 3x3
config-pin P2_19 gpio #LED 3x4
config-pin P2_25 gpio #LED 3x5

config-pin P2_27 gpio #LED 4x1
config-pin P2_29 gpio #LED 4x2
config-pin P2_31 gpio #LED 4x3
config-pin P2_33 gpio #LED 4x4
config-pin P2_35 gpio #LED 4x5

config-pin P1_26 gpio #LED 5x1
config-pin P1_28 gpio #LED 5x2
config-pin P1_30 gpio #LED 5x3
config-pin P1_32 gpio #LED 5x4
config-pin P1_34 gpio #LED 5x5



