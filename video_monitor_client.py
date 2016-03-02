 1 # -*- coding: UTF-8 -*-
 2 
 3 import socket, time
 4 import pygame
 5 from pygame.locals import *
 6 from sys import exit
 7 
 8 # 服务器地址，初始化socket
 9 ser_address = ('localhost', 10218)
10 cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
11 
12 # 设置超时
13 cli_socket.settimeout(5)
14 
15 # 向服务器发送消息，并判断接收时是否超时，若超时则重发
16 while 1:
17     cli_socket.sendto('startCam', ser_address)
18     try:
19         message, address = cli_socket.recvfrom(2048)
20         if message == 'startRcv':
21             print message
22             break
23     except socket.timeout:
24         continue
25 
26 # 此句无用。。防止窗口初始化后等待数据
27 cli_socket.recvfrom(65536)
28 
29 # 初始化视频窗口
30 pygame.init()
31 screen = pygame.display.set_mode((640,480))
32 pygame.display.set_caption('Web Camera')
33 pygame.display.flip()
34 
35 # 设置时间，可以用来控制帧率
36 clock = pygame.time.Clock()
37 
38 # 主循环，显示视频信息
39 while 1:
40     try:
41         data, address = cli_socket.recvfrom(65536)
42     except socket.timeout:
43         continue
44     camshot = pygame.image.frombuffer(data, (160,120), 'RGB')
45     camshot = pygame.transform.scale(camshot, (640, 480))
46     for event in pygame.event.get():
47         if event.type == pygame.QUIT:
48             cli_socket.sendto('quitCam', ser_address)
49             cli_socket.close()
50             pygame.quit()
51             exit()
52     screen.blit(camshot, (0,0))
53     pygame.display.update() 
54     clock.tick(20)
