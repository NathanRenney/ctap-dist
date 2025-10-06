# Learning Unit 1: Task 2

## Boolean Algebra

In this task we will use boolean algebra to check the eligibility of travel for aliens. Below you will find a set of conditions that prohibit travel. You should implement logic in the file `alien_travel_pass.py` so that you can run the code and get a result more quickly. Level one is fairly easy but level 2 and 3 are much easier to do programmatically.

> Do not let anyone marked wanted travel

> Any alien with a temperature over 75 cannot travel unless they are a Morbax

> There are transits to Gorvax Prime permitted at this time

> Skeelos is locked down, only Skeel can travel to Skeelos at this time

> Due to a newly formed black hole, no travel between Nublith Core and Morbos

> warp beacons cannot be taken to Braxil

> In addition here is a list of banned items:
```python
"neurotoxin", "black crystal", "plasma grenade", "dark matter vial", "antimatter core",
"phase disruptor", "xeno spores", "mind crystal", "telepathy enhancer", "dimensional anchor",
"psi amplifier", "plasma torch", "dark crystal", "reactive gel", "nano drone",
"psi crystal", "neural dampener", "temporal crystal", "plasma net", "dark shard",
"psi disruptor", "plasma blade", "plasma bomb", "dark vial", "quantum crystal",
"psi lens", "warp stabilizer", "neural interface", "bio enhancer", "alien egg"
```

## Add your own travel conditions by first writing them out and then implementing them
Write some of your own travel conditions using a similar style to above and implement them in code. Try not to just add conditions on top of each other - simplify expressions where possible.

## Form small groups and share your travel conditions with each other

Share your travel conditions with others and as a group explore simplifying the boolean algebra to minimise the lines of code required.

## Creating data and extending the system with more features

Use what you have explored in the last two sessions to further explore this concept, building a more complex system.

You can get the alien data generator using the following update script:
```python .scripts/update.py alien```