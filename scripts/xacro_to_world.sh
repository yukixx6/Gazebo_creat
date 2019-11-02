#!/bin/bash

DIR=$(cd $(dirname $0); pwd)
rosrun xacro xacro.py $DIR/test_w.xacro > $DIR/../worlds/test.world
