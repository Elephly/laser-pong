# laser-pong
COMP1405 Assignment 7 - An arcade survival style game of Pong!

### Prerequisites
- Python 3.5
- tkinter

### Controls
| Key   | Action                              | Availability (gun / paddle / both) |
| ----- | ----------------------------------- | ---------------------------------- |
| w     | Move paddle up                      | both                               |
| s     | Move paddle down                    | both                               |
| SPACE | Transform (toggle gun/paddle state) | both                               |
| o     | Fire green laser                    | gun                                |
| p     | Fire power shot                     | gun                                |

### Objective
You play as the left (red outlined) paddle in a game of pong. The basic
rules of pong are followed but there are some twists. Use 'w' to move your
paddle up and 's' to move your paddle down. As you're playing you'll notice
that every 3 seconds or so, a black box will appear with random dimension
and location. You may choose to dismiss it as unimportant, or you may
obliterate it. Press the space bar to change into your gun form, but be
carful, in gun form your paddle can no longer deflect the ball; it can only
deflect the ball once it is fully transformed back into its paddle form (it
will turn black). So now that you're in your gun form, you can press 'o' to
fire green lasers. These lasers do not affect the other paddle or the ball,
so do not waste time trying to shoot at them. If you shoot at a black box
ten times, it will be destroyed. Awesome, but what do you get out of doing
that? Well, firstly, you get one point for every black box you destroy.
Next, you restart the timer counting down to your death (that's right, you
HAVE to destroy these boxes if you want to live). Lastly, you will get
either a power shot or a nurf every time you destroy a box. If you get a
power shot, you can press 'p' to release it (in gun form), but this time,
you're aiming for the other paddle. If you hit him with the yellow power
shot, you will slow his speed by less than half. If you hit him with the
orange power shot, he will be stopped dead. Both of these effects only last
for a limited time however. Now for the nurfs, there are three possible
outcomes. You may be slowed by less than half, you may be stopped dead, or
your controls may be reversed. These also only last for a couple seconds.
Now that you know how to play, I should tell you exactly what the point is.
All you really want to do is last as long as you can and get as many
points as possible. Scoring on the other paddle gets you 5 points. The goal
is the high score man. As a last note, you have 3 lives to start out, and
obviously whenever you are scored on, you lose a live. The game ends when
you get to zero lives.
