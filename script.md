# SoME no. 2: how elliptic curves secure our data

Let's say you've been out with some friends and one of you has paid the entire
bill. You insist on paying back your share of the evening's entertainment, and
so you open your banking app of choice, enter the amount and within seconds, the
money is transferred from your account to your friend's. The day after, you wake
up and (because of your crippling social media addiction) you open Twitter.
Immediately, you get a whole feed full of tweets for you to enjoy. Maybe you
encounter a tweet about Bitcoin or Ethereum, and maybe you've wondered how those
actually work. Surprisingly, the underlying principle of Bitcoin is the same as
that of Twitter and your bank transactions. Their secret lies in a special kind
of curve, called an *elliptic curve*. Let's explore the details behind these
fascinating objects, and how we give rise to new worlds using mathematics itself.

## part 1: what is an elliptic curve?

Imagine you're back in high school. You've just learned about these things
called polynomials, and your English teacher is rambling on and on about iambic
pentameter or something. So, being bored out of your mind, you grab your graphing
calculator and start playing around. Some graphs you might want to draw are the
famous y = x², the most fundamental quadratic equation. Another one might be 
y = x³, a cubic with that distinctive s-shape. After a while, you might want to
start adding terms to these equations, like for example y = x³ + 2x² - 3. But
these are boring, we've all seen shapes like these a thousand times before.
That's when you ask yourself a question: why is it always just "y equals" in the
left hand side? We can add powers to the x without any problems, but poor old y
is always on its own. On most graphing calculators, this actually is set in
stone: you often cannot add anything to the left of the equals sign. This is due
to a limitation in the way those devices work, but you figure that it should
still be possible; after all, say that we write y² = x + 1, that's still a
relation between two variables that we can plot on a piece of paper.
So, underneath the Shakespearean sonnets that your English teacher printed out,
you find a bit of empty space and start doodling away. You'll need a pair of
axes, standard stuff. Now, to solve that equation... Thinking back to your
elemental algebra classes, you know that a plot like this will have a line going
through all the points that satisfy the equation. So, you'll need to find some
points for which the square of the y-coordinate is equal to the x-coordinate
plus one. You think about this for a while, and maybe through stumbling upon the
fact that really, you can just switch around x and y so long as you remember to
switch them back when you're drawing the point. They're just symbols, after all.
Now you're left with x² = y + 1, which you rearrange to y = x² - 1. That's
interesting: that's just a polynomial again, like you've solved countless times.
The parabola you drew earlier comes to mind, and you start thinking about how it
would look with the points flipped around.
If you're particularly clever, you might realise that instead of switching the
points, you could just as well change the names of the axes. After all, that has
the same exact meaning as calling points by their (y, x): the first number
represents the input, the second number represents the output. So, you cross out
the x and y you instinctively drew on your pair of axes from earlier and swap
them around. Now, you can draw the parabola that we usually know as
y = x² - 1 but in these new axes, and the result is equivalent to y² = x + 1.
"Interesting", you think. But your hunger for knowledge hasn't been satiated;
after all, this looks just the same as the graph from earlier. If you hold your
paper so that the y-axis is up again, the x-axis is the wrong way around.
Thankfully your English teacher printed the sonnets on very cheap paper, so you
can kind of see what it would look like when you flip your paper around. Luckily
we have the technology to display it in crisp Full HD quality.

## part 2: how can we shape new maths? (the group law)

## part 3: okay, that's... cool, but how is it useful?
