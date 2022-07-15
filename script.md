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

I could just very plainly give you the definition of an elliptic curve: it is a
smooth, non-singular curve in the projective plane of genus one. But that
doesn't mean anything to the vast majority of people and for our purposes it's
not a useful definition. That's why, instead, ...

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
plus one. You think about this for a while, and maybe you stumble upon the
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
them around. Now, you can draw the parabola that we usually know as y = x² - 1
but in these new axes, and the result is equivalent to y² = x + 1.
"Interesting", you think. If you hold your paper so that the y-axis is up again,
the x-axis is the wrong way around. Thankfully your English teacher printed the
sonnets on very cheap paper, so you can kind of see what it would look like when
you flip your paper around. Luckily we have the technology to display it in
crisp Full HD quality. But your hunger for knowledge hasn't been satiated; after
all, this looks just the same as the graph from earlier. 
And so, you start experimenting with other relations between those two variables
x and y. One thing you might try is using higher powers than just one and two.

## part 2: how can we shape new maths? (the group law)

So. We now have some set of curvy lines. I'm going to go through some
properties, and I want you to make little mental notes of them. By the time I'm
done, you'll see that we'll have gathered enough information to invent some new
mathematics of our own. This upcoming bit might not be the easiest to follow at
all times, so as our lord and saviour 3blue1brown always says: feel free to
pause and ponder to verify that the properties we're about to discuss are, in
fact, true.
Something to keep in mind throughout all of this is the fact that curves are
just a whole bunch of points grouped together. When we want to test if a given
point is on the curve (which, by the way, we notate like this: x \in C) we
simply check if those coordinates satisfy this equation. If, for example, we're
working with the curve y² = x³ + x, so that's with a = 1 and b = 0, and we want
to test if the point (2, 3) is on that curve, we test the equation:
x³ + x =? y² <=> 2³ + 2 =? 3² <=> 8 + 2 =? 9 <=> 10 =/= 9.
Well, ten isn't equal to nine, so this point isn't on the curve.

One thing you might have noticed in all of these animations is the fact that no
matter how I tweak these parameters, the top half of this curve is the mirror
image of the bottom half (or, as you probably will have heard this property
being called, it's symmetric about the x-axis). And this makes logical sense if
you think about it: we're looking for a number y, so that its square is equal to
that right hand side, whatever it may be. Let's say we work this out and it
turns out to be 36. Then we know that 6² = 36, and so 6 is a valid solution, but
-6 is a valid solution too, since (-6)² = 36. Every time a value checks out for
the top half of the y-axis, the negative of that value will by definition also
check out. That's the first property to keep in mind: for every point on the
curve (x, y), we can guarantee that (x, -y) will also be on the curve.
A little side note here: in a minute, it'll be useful to have visual
representations of these properties, or to put it another way: we want to have a
way of finding those derived points by thinking in terms of lines and graphs
instead of numbers. On a graph, to get from point A to the mirrored point B, all
we need to do is draw a line perpendicular to the x-axis through the point A.
The only other point where this line crosses the curve is in the point we want
to get to, B.
There is one thing to keep in mind with this property, though: if the point of
interest is on the x-axis (like, for example, here), then those two mirror
points coincide; after all, (x, 0) is the same point as (x, -0).

Okay, here comes the most advanced bit of mathematics in this video. We have a
collection of points right now. We can collect all of these points together in a
*set*, because every one of these points is unique. If we equip a set with an
operations and if that operation satisfies a bunch of properties, we can call it
a *group*. Those properties are:

 * **Associativity**: the order of the same operation shouldn't matter.
 * **Inclusivity**: every time we apply the operation, the result should still
                    be an element of the set we're working with.
 * **Neutral element**: there should exist an element which doesn't affect the
                        result of the operation.
 * **Inverse element**: for every element, we should be able to perform some
                        procedure to get out a new element which, when combined
                        with the original element returns the identity element.
Whew. That was the abstracts maths. A textbook example of a group is the whole
numbers equipped with addition. We can verify that (Z, +) as it's notated
satisfies these properties: we know that (a + b) + c = a + (b + c), so
associativity is satisfied. Every time you add two whole numbers you get another
whole number; you can't get a fraction, for example. The identity element is 0,
because adding zero to something doesn't change it, and the inverse element of
a is simply -a. In this specific case, we can even go a step further and say
that (Z, +) is an *abelian* group. This means that on top of those four
requirements for being a group, it also is commutative, i. e, a + b is the same
as b + a. You might think that that's a very obvious thing, but if we take a
look at (Z, -) for example, we can see that 4 - 3 is not the same as 3 - 4 and
as a result (Z, -) is a group, but just not an abelian one.

So, equipped with this knowledge, we can *define* addition for the points of an
elliptic curves. We'll get started with the absolute basics: addition takes in
two points on the curve and outputs another point on the curve. As long as we
stick to that principle, inclusivity will hold. We're sort of aiming for an
operation that forms a group together with the set of points on the curve. We
denote that set with E, by the way. Figured I should mention that.
Anyway, we need three points. On the curve. We also need it to be true that if
we only know two points, we can guarantee that there's a third which is "related"
to it. Maybe that rings a bell to earlier: we saw the property that a line that
intersects two points necessarily also intersects a third. Aha! So that's quite
a good start. Let's get started on making our vague idea concrete.

We'll take an elliptic curve and a line that intersects three points on it.
Let's label them, that makes things a lot more practical. We can now say that
A + B = C, in a way. Does that make rigorous mathematical sense? Not really, but
that's okay; we're just experimenting and playing around. We might have to make
some changes to our definition of addition here, but we'll get there in the end.
The reason that we're aiming for a group, incidentally, is because if you can
prove that some mathematical structure is a group, you suddenly unlock a whole
heap of extra maths that you can then do with that structure, and you can
guarantee that that all makes sense.
So, to recap: inclusivity is satisfied, because we know that the intersection
points are by definition on both graphs. That's one down. Let's test for
associativity next. We'll take two points A and B and call the result of their
addition C. Then we'll take another random point D, and call the result of their
addition E. *If and only if* associativity holds, we can say that (A + B) + D
will always result in the same point as A + (B + D). However, it's not difficult
to see that this isn't true at all here. Look: C will lie here, so then drawing
the line through C and D results in E. Sure, okay, but if we now draw the line
through B and D and call the resulting point F, then add A to that, we can see
that these points aren't equal.
Some tinkering needs to be done, then. We need to find some method that won't
leave us with this problem of associativity not holding, and we might need to 
be more clever about it than mere intuition. Let's put some thought into this.
One approach we might take is to start with adding a bunch of points and
setting them equal to the identity element. In that case we... hold on. We don't
have a identity element yet. That's a problem to be urgently solved: we really
do need one, and there's not really a clear answer for what it should be.
It can't be (0, 0): that point sometimes lies on the curve, but often doesn't,
and we need to keep inclusivity in mind. The solution to this problem lies in
the fact that I've lied to you. There's no special case in which the curve
intersects the line only twice, or only once. In fact, there's a solution to
this problem of having no identity element which will at once fix our 
associativity problem *and* take care of having an inverse element at the same
time.
The secret magical ingredient is a *point at infinity*. This is where the
"projective" bit comes into play from way in the beginning of this video.
If you look at a picture of railroads, you can clearly see that the two rails
*seem* to converge, way off in the distance. But you know, intuitively, that
rails need to remain parallel everywhere. Infinititely parallel lines versus
intersecting somewhere way off in the distance. Hmm. The reason the lines
look like they intersect is because of the perspective projection that our
eyes use. This is where the projective plane gets its name: it's a regular
Euclidian plane with a little extra: points that are infinitely far off in the
distance, which form an intersection point for any two parallel lines.
In a projective plane, *every* pair of lines intersects.
You might ask yourself how this is going to help our problems. However, things
fall into place quite nicely when we incorporate these points at infinity into
our elliptic curve problems. Say that we take E to mean all of the points of
the curve, *plus* a point at infinity called *O*. If we then say that the
identity element for the group is that O point, we can suddenly solve our
problems. Let's go over how addition works with this point under our belt.

If P and Q are two points on the curve, we can say that pretty often, the line
between them will intersect the curve at a third point. Instead of saying that
P + Q = R like we did before, we can incorporate the identity now. We can try
P + Q + R = O, or in other words P + Q = -R. Remember that negating a point is
equivalent to drawing a vertical line through that point and seeing where else
it intersects the curve.

We can verify that this new method of addition satisfies associativity, just by
doing it visually. A rigorous proof for this is beyond the scope of this video
and it's important to remember that in maths, "it works for these three cases so
it generally holds for all cases" is very much not a valid way of reasoning, but
for these purposes, it'll do fine.

Associativity: check. Identity element, well, we defined one, so that's one we
get for free. Inverse element: hmm. Let's think about that. We need a way to get
from one point to another so that if we add them, we don't get a point on the
curve but instead the identity element. I mean, let's just try it out, eh?
If we grab a random point on the curve, it can only intersect the curve once
again. If it intersects in two other places, it's just regular addition.
Supposing we have a point P. We'll pretend that this is fixed in place: we want
to find the inverse point for it, let's call that P prime for now. We need to
make sure that the line between P and P prime intersects the curve nowhere else;
that's the whole purpose of the property that we're trying to satisfy. And in
almost every possible position for P prime that's not the case. You might notice
however that as the line gets steeper, the other intersection point gets higher
very quickly. And, if we take the point -P, that line's slope becomes infinite.
In this case (and only in this case), there's no third point. Or, rather, the
third point *is* the point at infinity, which is also the identity. That's
like saying that you can get nine by adding three numbers: 4, 5 and 0.
And if you think about it symbolically it makes sense too: P + -P = O.
So we've got associativity, inverse elements, an identity element and because
we've only ever used lines to get new points, everything's inclusive.

Dear viewer, it seems that we've got ourselves a group on our hands. Now we can
get some interesting stuff going on.

## part 3: okay, that's... cool, but how is it useful?

One of the most useful applications of elliptic curves is in cryptography. To
make a long story short: the most used type of cryptography is *public-key*
cryptography, which relies on the fact that some bits of maths are very easy
to calculate one way but incredibly difficult to reverse. The classic
example is multiplying two prime numbers: if I give you 673 and 977 it's trivial
to take out a calculator and multiply them, but if I instead give you 783451 and
tell you "two prime numbers divide that number, which ones?" you basically have
no better option but to go through the primes and try to divide 783451 by each
one of them. That'll take you a very long time, believe me. And in the world of
computers we don't use prime numbers that are three digits long; think 512 bits.
