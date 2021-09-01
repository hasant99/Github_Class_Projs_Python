###Author: Hasan Taleb
###Class: CSc110
###Description: A program that models the behavior of a ball being dropped
###             from various floors of a building created by the user.

import os

print('--- Welcome to the free fall calculator ---')
stories = int(input('Number of building stories:\n'))
drop_points = int(input('Number of drop points:\n'))
bounce_heights = int(input('Number of bounce heights calculate:\n'))

if drop_points == 0 and bounce_heights == 0:
    print('\n.-------.')
    i=0
    while i < stories:
        print('| # # # |' + '\n' + '|       |')
        i += 1
    print('*********')
    os._exit(0)

if stories%drop_points != 0:
    print('Number of stories required to be a multiple of the drop points.')
    os._exit(0)
elif stories > 50 or drop_points > 50 or bounce_heights > 50:
    print('Input values required to be 50 or less.')
    os._exit(0)

print('\n.-------.')
i=0
story_marker = 1
while i < stories:
    drop_point_location = (stories / drop_points)
    if i % drop_point_location == 0:
        print('| # # # |' + '  <-(' + str(story_marker)  + ')' + '\n' + '|       |')
        story_marker += 1
    else:
        print('| # # # |' + '\n' + '|       |')
    i += 1

print('*********')

i=0
story_marker = 1
drop_height = stories
while i < stories:
    drop_point_location = (stories / drop_points)
    if i % drop_point_location == 0:
        print('\n(' + str(story_marker) + ')' + ' fall time = ' + str(round(((((2*(4*drop_height)))/9.807)**0.5), 2)) + ' seconds', end='')
        i_2=1
        bounce = (4*drop_height)
        while i_2 <= bounce_heights:
            bounce = bounce * .7
            print(',' + ' bounce ' + str(i_2) + ' = ' + str(round(bounce, 2)), end='',)
            i_2 += 1
        drop_height -= 1
        story_marker += 1
    else:
        drop_height -= 1
    i += 1
print()
