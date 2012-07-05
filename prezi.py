# down 1-12
# home 13
# up   14-28

# zoomlevel from home to down 12
# home 13
# to up 14

import sys
import time
import math
from Quartz.CoreGraphics import *

class UI:
  def __init__( self, wait = 1 ):
    self.wait = wait

  def event(self,type, x, y):
    theEvent = CGEventCreateMouseEvent(None, type, (x,y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

  def move(self,x,y):
    self.event(kCGEventMouseMoved, x,y)
    time.sleep( self.wait )

  def clickdn(self,x,y):
    self.event(kCGEventLeftMouseDown, x,y)

  def clickup(self,x,y):
    self.event(kCGEventLeftMouseUp, x,y)

  def click(self,x,y,n=1):
    for i in range( 0, n ):
      self.clickdn(x,y)
      self.clickup(x,y)
      time.sleep( self.wait )

  def drag(self,x,y):
    self.event(kCGEventLeftMouseDragged, x,y)

  def shift(self,x1,y1,x2,y2):
    self.clickdn(x1,y1)
    self.drag(x2,y2)
    self.clickup(x2,y2)
    time.sleep( self.wait )

  def position( self ):
    return CGEventGetLocation(CGEventCreate(None))

# end class

class ZUI:
  def __init__( self, ui = None ):
    self.ui = ui

  def back( self, n = 1 ):
    for i in range( 0, n ):
      self.ui.click( 151, 101 )

  def show( self ):
    self.ui.click( 1254, 716 )

  def insert( self ):
    self.ui.click( 306, 148 )

  def shapes( self, wait = 0 ):
    self.insert()
    self.ui.click( 303, 135, 2 )
    if wait > 0:
      time.sleep( wait )

  def home( self ):
    self.ui.click( 164, 371 )

  def zoomin( self ):
    self.ui.click( 164, 407 )

  def zoomin( self ):
    self.ui.click( 164, 446 )
    time.sleep( self.wait )

# end class

class EyeOfProvidence:
  def __init__( self, origo, r ):
    self.origo = origo
    h = 3 * r
    a = 3.464 * r
    h23 = 2.0 / 3.0 * h
    h13 = 1.0 / 3.0 * h
    a12 = 0.5 * a
    e = 0.01 * h
    # +-->
    # |
    # V
    #          A
    #        a1 a2
    #       /     \
    #      c2      b1
    #     C c1 -- b2 B
    #
    #        x                   y
    self.A = ( origo[0],      origo[1] - h23 )
    self.B = ( origo[0] + a12 , origo[1] + h13 )
    self.C = ( origo[0] - a12 , origo[1] + h13 )

    self.a1 = ( self.A[0] - e, self.A[1] + e )
    self.a2 = ( self.A[0] + e, self.A[1] + e )

    self.b1 = ( self.B[0] - e, self.B[1] - e )
    self.b2 = ( self.B[0] - e, self.B[1] + e )

    self.c1 = ( self.C[0] + e, self.C[1] + e )
    self.c2 = ( self.C[0] + e, self.C[1] - e )

  def draw(self,zui):
    zui.shapes()

    zui.ui.click(289,131,2)
    zui.ui.click(self.a2[0],self.a2[1])
    zui.ui.click(self.b1[0],self.b1[1])

    zui.ui.click(289,131)
    zui.ui.click(self.b2[0],self.b2[1])
    zui.ui.click(self.c1[0],self.c1[1])

    zui.ui.click(289,131)
    zui.ui.click(self.c2[0],self.c2[1])
    zui.ui.click(self.a1[0],self.a1[1])

    zui.ui.click(311,235)
    zui.ui.click( self.origo[0], self.origo[1] )
    zui.ui.click( self.origo[0], self.origo[1] )

    zui.back(2)

# end class


class Giotto:
  def __init__( self, origo, r ):
    self.origo = origo
    self.r = r

  def draw( self, zui ):
    a = (self.origo[0] + self.r * math.cos(0),self.origo[1] - self.r * math.sin(0))
    zui.shapes(1)

    zui.ui.click(214,277,2)
    zui.ui.clickdn(a[0],a[1])
    for i in range(0,400,10):
      a1 = self.origo[0] + self.r * math.cos(i/360.0*6.28)
      a2 = self.origo[1] - self.r * math.sin(i/360.0*6.28)
      zui.ui.move(a1,a2)
    zui.ui.clickup(a1,a2)

    zui.ui.click(311,235)
    zui.ui.click( self.origo[0], self.origo[1] )
    zui.ui.click( self.origo[0], self.origo[1] )

    zui.back(2)

# end class

