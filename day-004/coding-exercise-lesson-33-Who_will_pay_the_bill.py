# Figure out how to pick a random name from the list of friends.

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# My code begins here:

import random

random_friend = random.randint(0, 4)
print(friends[random_friend])

# The other way to do it, called out by Angela, in addition to the way
# I did it is:

print(random.choice(friends))
