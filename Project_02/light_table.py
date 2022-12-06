"""
-----------------------------------------------------------------
---------
Light Table
-----------------------------------------------------------------
---------
License:   
Copyright 2022 Singrhu Poltanawasit

Redistribution and use in source and binary forms, with or 
without 
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this 
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above 
copyright notice, 
this list of conditions and the following disclaimer in the 
documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its 
contributors 
may be used to endorse or promote products derived from this 
software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY 
OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH 
DAMAGE.
-----------------------------------------------------------------
---------
Use the following hardware components to make a programmable 
combination lock:  
 - WS2812B Addressable RGB LED Strip
 - 25 Photodiodes (for a 5x5 table)

Requirements:
 - When there is no light detected on a photodiode, the LED in the area of
   the photodiode turns on. 
"""
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM


class lighttable()
	button		= None
	led_1x1 	= None
	led_1x2 	= None
	led_1x3 	= None
	led_1x4 	= None
	led_1x5 	= None
	led_2x1 	= None
	led_2x2 	= None
	led_2x3 	= None
	led_2x4 	= None
	led_2x5 	= None
	led_3x1 	= None
	led_3x2 	= None
	led_3x3 	= None
	led_3x4 	= None
	led_3x5 	= None
	led_4x1 	= None
	led_4x2 	= None
	led_4x3 	= None
	led_4x4 	= None
	led_4x5 	= None
	led_5x1 	= None
	led_5x2 	= None
	led_5x3 	= None
	led_5x4 	= None
	led_5x5 	= None
	ADC1 		= None
	ADC2		= None
	ADC3		= None
	ADC4		= None
	ADC5		= None


	def __initself__(self,	button="P2_2",
					 led_1x1="P2_4", led_1x2="P2_6",led_1x3="P2_8", led_1x4="P2_10",led_1x5="P2_18",
					 led_2x1="P2_20", led_2x2="P2_22",led_2x3="P2_24", led_2x4="P2_28",led_2x5="P2_30",
					 led_3x1="P2_32", led_3x2="P2_34",led_3x3="P2_17", led_3x4="P2_19",led_3x5="P2_25",
					 led_4x1="P2_27", led_4x2="P2_29",led_4x3="P2_31", led_4x4="P2_33",led_4x5="P2_35",
					 led_5x1="P1_26", led_5x2="P1_28",led_5x3="P1_30", led_5x4="P1_32",led_5x5="P1_34",
					 ACD1="P1_29",ACD2="P1_31",ACD3="P1_33",ACD4="P1_35",ACD5="P1_02")

		#Initialize variables

		self.button	= button

		self.led_1x1 = led_1x1
		self.led_1x2 = led_1x2
		self.led_1x3 = led_1x3
		self.led_1x4 = led_1x4
		self.led_1x5 = led_1x5

		self.led_2x1 = led_2x1
		self.led_2x2 = led_2x2
		self.led_2x3 = led_2x3
		self.led_2x4 = led_2x4
		self.led_2x5 = led_2x5

		self.led_3x1 = led_3x1
		self.led_3x2 = led_3x2
		self.led_3x3 = led_3x3
		self.led_3x4 = led_3x4
		self.led_3x5 = led_3x5

		self.led_4x1 = led_4x1
		self.led_4x2 = led_4x2
		self.led_4x3 = led_4x3
		self.led_4x4 = led_4x4
		self.led_4x5 = led_4x5

		self.led_5x1 = led_5x1
		self.led_5x2 = led_5x2
		self.led_5x3 = led_5x3
		self.led_5x4 = led_5x4
		self.led_5x5 = led_5x5

		self.ADC1 	= ADC1
		self.ADC2	= ADC2
		self.ADC3	= ADC3
		self.ADC4	= ADC4
		self.ADC5	= ADC5

		self._setup()


	#end def

def _setup(self):
	#set up hardware components

	#initialize button
	GPIO.setup(self.button, GPIO.IN)

	#initialize LEDS
	GPIO.setup(self.led_1x1, GPIO.OUT)
  GPIO.setup(self.led_1x2, GPIO.OUT)
  GPIO.setup(self.led_1x3, GPIO.OUT)
  GPIO.setup(self.led_1x4, GPIO.OUT)
  GPIO.setup(self.led_1x5, GPIO.OUT)

  GPIO.setup(self.led_2x1, GPIO.OUT)
  GPIO.setup(self.led_2x2, GPIO.OUT)
  GPIO.setup(self.led_2x3, GPIO.OUT)
  GPIO.setup(self.led_2x4, GPIO.OUT)
  GPIO.setup(self.led_2x5, GPIO.OUT)

  GPIO.setup(self.led_3x1, GPIO.OUT)
  GPIO.setup(self.led_3x2, GPIO.OUT)
  GPIO.setup(self.led_3x3, GPIO.OUT)
  GPIO.setup(self.led_3x4, GPIO.OUT)
  GPIO.setup(self.led_3x5, GPIO.OUT)

  GPIO.setup(self.led_4x1, GPIO.OUT)
  GPIO.setup(self.led_4x2, GPIO.OUT)
  GPIO.setup(self.led_4x3, GPIO.OUT)
  GPIO.setup(self.led_4x4, GPIO.OUT)
  GPIO.setup(self.led_4x5, GPIO.OUT)

  GPIO.setup(self.led_5x1, GPIO.OUT)
  GPIO.setup(self.led_5x2, GPIO.OUT)
  GPIO.setup(self.led_5x3, GPIO.OUT)
  GPIO.setup(self.led_5x4, GPIO.OUT)
  GPIO.setup(self.led_5x5, GPIO.OUT)

	#initialize ADCs
	GPIO.setup(self.ADC1, GPIO.OUT)
  GPIO.setup(self.ADC2, GPIO.OUT)
  GPIO.setup(self.ADC3, GPIO.OUT)
  GPIO.setup(self.ADC4, GPIO.OUT)
  GPIO.setup(self.ADC5, GPIO.OUT)

#end def

#when button is ON, turn on program
#every 1 second read all 5 ADCs (by turning the one you want to read on HIGH and the rest low)
#when the photodiode changes, turn on corresponding LED
