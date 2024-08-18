# Concepts
- Forces
	- "Push and pull"
	- Forces are vectors
	- Forces add together when multiple are applied to the same object
- Newton's 1st Law
	- A body at rest remains at rest, and a body in motion remains in constant velocity unless acted upon by a net external force.
	-  Basically, objects tend to remain in whatever state they're currently in -- inertia.
	- Newton's laws hold true in Inertial Reference Frames
		- Basically, an inertial reference frame is one in which there aren't any fictitious forces -- non-existent forces that still cause an object to accelerate.
		- Any reference frame accelerating relative to an inertial reference frame is non-inertial.
		- Stars are pretty close to inertial reference frames, and technically the earth accelerates relative to them (because it spins), but it's slow enough that we usually consider experiments relative to earth to be inertial.
	- constant v if F inertial
- Newton's 2nd Law
	- force is proportional to acceleration
	- acceleration is inversely proportional to mass
	- F-net = ma
	- Because it's a vector, we can solve for each component independently (independent motion).
- Mass and weight
	- Remember that earlier we said that for human-sized objects near the surface of the earth, acceleration is roughly constant.
	- So if we want the force of gravity, all we have to do is multiply it by the object's mass.
- Newton's Third Law
	- Whenever one body exerts a force on a second body, the first body experiences a force equal in magnitude and opposite in direction to the force that it exerts. 
	- $\vec{F}_{AB} = -\vec{F}_{BA}$
	- This is when choosing the system becomes very important
- Example: object pushes other object

- Free-body diagrams
	- Reduce the system of interest to a point so that the forces on the system can be easily worked with.
- Common forces
	- Normal force, weight force, friction, tension
- Hooke's law (F = -kx)
- Friction:
	- (when you zoom in far enough, there are tiny forces you have to fight to get something moving -- friction at a larger scale)
	- Friction is proportional to the normal force - the more you push something into an object, the more friction.
	- Specifically between two objects you have the coefficient of friction which tells you how much friction there is.
	- Friction will only exert enough force to oppose motion, so $f_s \leq \mu_s N$ .
	- Once the applied force exceeds $f_s = \mu_s N$, the object moves
	- Once the object is moving, the kinetic friction force is given by $f_k = \mu_k N$.
		- It's easier to keep pushing something than to get it moving in the first place
- (inclined plane problem?)

- Centripetal force:
	- We already saw centripetal acceleration (a = v^2/r) when moving objects rotate in a circle
	- This means that we have the required centripetal force mv^2/r whenever an object goes in a circle
- coriolis force

# Script

In the previous video, we learned how to model the motion of objects given their initial positions, velocities, and accelerations. And in each example we kind of just, assumed that we would know what these values were. But how do we know them? Where does motion come from?

This is where we'll have to broaden our scope from kinematics to dynamics, which includes where motion comes from.

So what causes something to move? Let's say I have a simple sphere floating in space, in order to get it to move, well, I could push it, I could pull it. Maybe I could attract it with gravity. But in all cases I'm getting it to move by applying a force to the object, which can be loosely defined as a push or a pull on our object.

Forces have a magnitude -- how much you push on something -- and also a direction -- what way you push it in, so it makes sense to describe them with vectors. If multiple things are pushing on our object, then we get find the net force by adding each of the force vectors on our object.

So we've already shown that when you apply a force on an object, you change its velocity. What happens if I stop applying the force? Well, it's velocity wouldn't change, and it would just keep on drifting in the direction it was going in. With no other forces impeding its motion, it would keep moving like that.

## Newton's 1st Law

This is the basis of Newton's 1st law of motion: A body at rest remains at rest, and a body in motion remains in constant velocity unless acted upon by a net external force.

Now there's one more caveat to this, and that's that the velocity has to be measured from an *inertial frame of reference.* Basically, the reference frame we're measuring from has to be moving at a constant velocity, it can't be accelerating. How can we tell if that's true? One way is to look at the acceleration of other objects. If we ever see an object accelerating without an apparent force creating that acceleration, it's called a fictitious force and it means that our reference frame is accelerating.

One example of this is a rotating reference frame.
Let's say we have an observer standing on a spinning centrifuge like this. If the observer is holding a ball, and lets go of it, we know that the ball will continue to move in the same direction it was going in, because its velocity doesn't change with no net external force.
But from the perspective of the person on the centrifuge, it looks like the ball accelerated downward, and so they would conclude that there's an outward force on the ball, even when there isn't.

Scientists have figured out that a lot of the stars we can see are, within experimental error, inertial reference frames. Since the earth spins relative to them, it's technically not an inertial reference frame, but it's spinning slow enough that we'll generally assume that the earth is close enough to an inertial reference frame when solving for things.

## Newton's 2nd Law

Newton's second law gives us a way to relate forces to acceleration. Specifically, the net external forces acting on a system are equal to that system's mass times its acceleration. Notice that we said the forces have to be external to the system.
If we put a person in a box and let our system be both the person and the box, then even if the person it pushing on the box, we don't count that as a force because it's internal to a system. We would need something originating from outside our system, like someone outside the box pushing on it, to count it as a force.

## Newton's 3rd Law

The reason we can ignore the internal forces of a system is because they end up cancelling out with each other, due to Newton's 3rd law:

Whenever one body exerts a force on a second body, the first body experiences a force equal in magnitude and opposite in direction to the force that it exerts. 

In math terms, the force from object A onto object B is equal and opposite to the force from object B onto object A.

Thinking back to the box example, when the person pushes on the box, both the person and the box experience the same force in opposite directions. Even though the box and the person might move, they'll do so in a way such that the center of mass of the system is still in the same location, so the object hasn't moved from the system's point of view.

## Box on table

Let's look at an example:
A box, resting on a table, resting on the ground.

The first system we'll look at is the box.
Remember from the previous video that human-sized objects near earth have near-constant acceleration: g. So we can get the force of gravity by multiplying it by the box's mass, which we'll call the weight force from the earth on the box -- W-Eb. Now when rigid objects come into contact with each other, they have to push away from each other, otherwise they wouldn't be rigid, or, they would pass through each other. We call it the normal force and it acts perpendicular to the object's surface, so in this case we get an upward normal force from the table onto the box.
The second system is the table. It also has a weight force, but now it feels two normal forces: one from the ground and one from the table. If we combine these two systems into one big system, then the internal normal forces cancel out, since they're no longer external, and we just have the two weight forces and the normal force from the ground.

## Incline / friction
%% read this part slowly theres a lot of animation to do  %%
Now let's put this box on an incline.
The weight force from the box still points downwards, but now the normal force points at an angle like this, which means our net force is going this way, *unless* we have friction. Friction acts in the direction opposite the direction the objects would slide if they were to move, parallel to the surface. So in this case it goes this way. 
The reason friction is there is because if you zoom in far enough to the two surfaces, you would see that they're actually pretty bumpy, and so it takes energy to get them to slide past each other.

Now friction is proportional to the normal force at that contact point. The proportionality between the normal force and friction is called the coefficient of friction. But, the friction force is only going to work as hard as it needs to in order to stop the object from moving, so we say that it's actually less than or equal to the normal force times mu-s. The s here stands for static. And that's because if the opposing force exceeds mu-s times the normal force, then static friction can't hold the object anymore, and it starts sliding.

If you've ever pushed something heavy before, you might have noticed that once you get it moving, it's easier to push than when you were trying to start moving it. This is because each contact point actually has two coefficients of friction: the static one, and the kinetic one. Once you get an object moving, the amount of force needed to keep it moving drops because the kinetic coefficient of friction is lower than the static coefficient of friction.

So in order to figure out which one we're working with, we first have to solve for the normal force. In this case, it's easier to use slanted axes. 

Summing the forces in the y-direction, we get the normal force minus the y-component of the weight force, which is equal to W_Eb times the cosine of theta. We don't include friction in this calculation since it has no y-component.
Since the block isn't accelerating in the y-direction, because the normal force can hold up the block, we can set the y-acceleration equal to zero.
Doing this allows us to solve for the normal force.

Now when we sum the forces in the x-direction, we'll have the x-component of the weight force minus friction. Make sure that your signs line up with the axes. Since the positive x-direction is down the hill, the weight force is positive and the friction force is negative.

Now we have to determine if the force of friction is strong enough to keep the block from sliding. We'll start by assuming that this is the case, in which case the acceleration equals zero. This means that the static friction force must equal at least this quantity; so, if we compute the maximum friction force, mu-static times the normal force, which we got earlier, and it's less than the x-component of the weight force, then we know that the box will be sliding, and so the friction force becomes the mu-kinetic times the normal force, otherwise, the forces balance and the static friction force is exactly equal to W_EB times the sine of theta.

## Springs

Another kind of force that you'll see a lot is the spring force. For most of classical mechanics, we assume that the force of a spring obeys Hooke's Law, which says that the spring force is proportional to the length you displace it or pull it, where the spring constant is K, and this negative sign means that it's in the opposite direction.

So let's say our spring constant is 5 Newtons per meter, where Newtons are the SI unit for force. If I pull this spring two meters to the right, then it's going to pull back with 10 Newtons of force in the opposite direction -- to the left.

## Ropes

One last kind of force you'll see a lot is the tension in ropes. Usually, we'll assume that ropes have zero weight and that they don't break, so they can hold an infinite amount of force.

Let's say we hang two blocks from the ceiling by ropes, A and B. Let's start with the forces on B. It has a weight force pointing downward, as well as a tension force on the rope from A to B, pointing upward. Since this rope can hold infinite weight, we assume that the object B is not moving, which means we can set the y-acceleration equal to zero and solve for the tension force. We'll say that up is the positive y-direction, so the tension is positive and the weight is negative.

Now block A will also have a weight force, and a tension force up from the ceiling, but it will also have a tension force down from block B onto block A.
This force right here is the Newton's 3rd law pair to the tension force upward on block B, which means that it has the same magnitude as the one we calculated earlier.

In general, ropes are always going to hold tension on both sides of them.
If you have a pulley with a rope across it like this, then the forces on each side will have the same magnitude, because the rope holds the same tension, but it might be exerted in different directions.

## Centripetal
If you have a rope, or some other force, like friction, constraining the object to a circular motion, then we already know the centripetal acceleration from earlier: v^2 over r. It follows then that the centripetal force must be equal to mass times acceleration -- m v^2 over r. So if I have a 5 kg block moving at 10 meters per second in a circle with a radius of 2 meters, then the force required to hold the block in is 250 Newtons.

