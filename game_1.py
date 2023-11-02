import random  # 设置事物刷新位置
import pygame  # 获取图形组
pygame.init()#建立游戏窗口
#定义游戏内颜色
white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)
#设置窗口的尺寸和标题栏
dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('贪吃蛇游戏')
clock=pygame.time.Clock()#定义帧率
#定义蛇的速度与大小
snake_block=10
snake_speed=12
#定义游戏字体与大小
font_style=pygame.font.SysFont("FangSong",25)
score_font=pygame.font.SysFont("FangSong",35)
#计算分数的函数
def Your_score(score):
    value=score_font.render("你的成绩："+str(score),True,black)
    dis.blit(value,[0,0])
#定义蛇的参数
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
#消息显示函数
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#构建游戏
def gameLoop():
    game_over = False#游戏结束
    game_close = False#游戏关闭
#蛇的位置
    x1 = dis_width / 2
    y1 = dis_height / 2
#改变位置参数
    x1_change = 0
    y1_change = 0
#储存蛇的头部与长度
    snake_List = []
    Length_of_snake = 1
#新事物产生的随机位置
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(red)
            message("你失败了！！！",white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
#定义是否继续游戏
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        gameLoop()
#定义游戏操作按键
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
#设置撞到蛇身
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()