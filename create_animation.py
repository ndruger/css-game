#!/bin/python
from string import Template
import random
import sys

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
ENEMY_WIDTH_MAX = 100

straightLine = """
@-webkit-keyframes ${name} {
  0% {
    top: ${first_top}px;
    left: ${first_left}px;
	-webkit-transform: scale(${first_scale});
  }
  100% {
    top: ${last_top}px;
    left: ${last_left}px;
	-webkit-transform: scale(${last_scale});
  }
}
input#${name}{
	background-image: url('${image_url}');
	-webkit-animation-name: ${name};
	-webkit-animation-duration: ${duration}s;
	-webkit-animation-delay: ${start_time}s;
}
"""

bounce = """
@-webkit-keyframes ${name} {
  0% {
    top: ${low0_top}px;
    left: ${low0_left}px;
  }
  20% {
    top: ${high0_top}px;
    left: ${high0_left}px;
  }
  40% {
    top: ${low1_top}px;
    left: ${low1_left}px;
  }
  60% {
    top: ${high1_top}px;
    left: ${high1_left}px;
  }
  80% {
    top: ${low2_top}px;
    left: ${low2_left}px;
  }
  100% {
    top: ${high2_top}px;
    left: ${high2_left}px;
  }
}
input#${name}{
	background-image: url('${image_url}');
	-webkit-animation-name: ${name};
	-webkit-animation-duration: ${duration}s;
	-webkit-animation-delay: ${start_time}s;
}
"""

straightLineTmp = Template(straightLine)
bounceTmp = Template(bounce)

ENEMY_TYPE_HORIZONTAL_COW = 0
ENEMY_TYPE_BOUNDING_COW = 1
ENEMY_TYPE_FRONT_AND_BACK_COW = 2
ENEMY_TYPE_MAX = ENEMY_TYPE_FRONT_AND_BACK_COW

def calcLefts(num):
	lefts = []
	for k in range(num):
		lefts.append(-ENEMY_WIDTH_MAX + (SCREEN_WIDTH + ENEMY_WIDTH_MAX * 2) / (num - 1) * k)
	return lefts

def calcRandomEnemyScale():	
	return (2.0 + random.random() * 1)

time_sum = 0;
for i in range(101):
	name = 'enemy' + str(i)
	type = random.randint(0, ENEMY_TYPE_MAX)
	if type == ENEMY_TYPE_HORIZONTAL_COW:
		duration = random.randint(4, 8)
		lefts = calcLefts(2)
		if random.randint(0, 1) == 0:
			imageUrl = 'images/cow_right.png'
		else:
			lefts.reverse()
			imageUrl = 'images/cow_left.png'
		print straightLineTmp.substitute(
			name=name,
	        duration = duration,
	        start_time = time_sum,
	        image_url = imageUrl,
			first_left = lefts[0], last_left = lefts[1],
			first_top = random.randint(0, SCREEN_HEIGHT),
			last_top = random.randint(0, SCREEN_HEIGHT),
			first_scale = calcRandomEnemyScale(),
			last_scale = calcRandomEnemyScale()
		)
	elif type == ENEMY_TYPE_BOUNDING_COW:
		duration = random.randint(4, 8)
		highTopBase = random.randint(0, SCREEN_HEIGHT / 2)
		lowTopBase = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
		lefts = calcLefts(6)
		if random.randint(0, 1) == 0:
			imageUrl = 'images/black_cow_right.png'
		else:
			lefts.reverse()
			imageUrl = 'images/black_cow_left.png'
		print bounceTmp.substitute(
			name=name,
	        duration = duration,
	        start_time = time_sum,
	        image_url = imageUrl,
			low0_left = lefts[0], high0_left = lefts[1], low1_left = lefts[2], high1_left = lefts[3], low2_left = lefts[4], high2_left = lefts[5], 
			low0_top = lowTopBase, low1_top = lowTopBase, low2_top = lowTopBase,
			high0_top = highTopBase, high1_top = highTopBase, high2_top = highTopBase,
		)
	elif type == ENEMY_TYPE_FRONT_AND_BACK_COW:
		duration = random.randint(2, 3)
		if random.randint(0, 1) == 0:
			firstScale = 0.0
			lastScale = 4.0
			imageUrl = 'images/cow_front.png'
		else:
			firstScale = 4.0
			lastScale = 0.0
			imageUrl = 'images/cow_back.png'
		print straightLineTmp.substitute(
			name=name,
	        duration = duration,
	        start_time = time_sum,
	        image_url = imageUrl,
	        first_top = random.random() * SCREEN_HEIGHT,
	        first_left = random.random() * SCREEN_WIDTH,
	        last_top = random.random() * SCREEN_HEIGHT,
	        last_left = random.random() * SCREEN_WIDTH,
			first_scale = firstScale,
			last_scale = lastScale,
		)
	time_sum += duration / 3


