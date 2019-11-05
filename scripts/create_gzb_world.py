#!/usr/bin/env python
import cv2,glob
import numpy as np

def conf():
  path_w = 'test_w.xacro'
  map_path = ''
  img = []
  size = []
  count = 0

  s = '<?xml version="1.0" ?>\n\
  <sdf version="1.4" xmlns:xacro="http://ros.org/wiki/xacro">\n\
  <xacro:include filename="$(find Gazebo_world_creator)/scripts/sample_wall.wall.xacro" />\n\
  <world name="default">\n\
    <include>\n\
      <uri>model://ground_plane</uri>\n\
    </include>\n\
    <light name=\'sun\' type=\'directional\'>\n\
      <cast_shadows>0</cast_shadows>\n\
      <pose>0 0 5 0 0 0</pose>\n\
      <diffuse>0.8 0.8 0.8 1</diffuse>\n\
      <specular>0.2 0.2 0.2 1</specular>\n\
      <attenuation>\n\
        <range>1000</range>\n\
        <constant>0.9</constant>\n\
        <linear>0.01</linear>\n\
        <quadratic>0.001</quadratic>\n\
      </attenuation>\n\
      <direction>-0.5 0.1 -0.9</direction>\n\
    </light>\n\
    <physics type=\'ode\'>\n\
      <max_step_size>0.001</max_step_size>\n\
      <real_time_factor>1</real_time_factor>\n\
      <real_time_update_rate>1000</real_time_update_rate>\n\
      <gravity>0 0 -9.8</gravity>\n\
    </physics>\n\
    <gui fullscreen=\'0\'>\n\
      <camera name=\'user_camera\'>\n\
        <pose>-0.556842 -0.914575 1.68773 0 1.05964 0.520195</pose>\n\
        <view_controller>orbit</view_controller>\n\
      </camera>\n\
    </gui>\n'

  maze = ' <xacro:wall>\n  <pose>%f %f %f %f %f %f</pose>\n </xacro:wall>\n'
  end = '</world>\n</sdf>\n'

  map_path = glob.glob('./map/*.pgm')
  img = cv2.imread(map_path[0])
  ret,thresh = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
  size = thresh.shape

  with open(path_w, 'w') as f:
    f.write(s)
    for i in range(size[1]):
      for j in range(size[0]):
        if thresh[i,j,0] == np.array([0]):
          if count <= 1000:
            print(i-size[1]/2,j-size[0]/2)
            f.write(maze % ((i-size[1]/2)*0.001,(j-size[0]/2)*0.001,0.025,0,0,0))
            count += 1
    # f.write(maze % (1,1,0.025,0,0,0))
    f.write(end)

if __name__ == '__main__':
 conf()


