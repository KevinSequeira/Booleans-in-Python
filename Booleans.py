# Hey people. Welcome to the second session of Python Programming.
# In the last session, we started our journey with Python by exploring Numbers, one of
# Python's built-in data types. We took the first sub-type of Numbers, Integers, and 
# saw how they work.

# In this session, let's look at the next sub-type, called 'Booleans'.

# If you're an engineer, or from the STEM background, you'll know what Booleans are.
# Boolean entities, in the most basic definition, cater to truth values: True or False.
# As a sub-class of Integers, they can also be represented as 1 or 0. Or more simply as
# any non-zero number and a zero number.

# In Python, every object can be respresented in the Boolean form using the 'bool' function.

# Let's look at some quick, simple examples on how Boolean values work.

a = True;       # Here, we have assigned the variable 'a' with a Boolean value 'True'. Here, you can also find Python demonstrating dynamic-typing
                # which means that Python assigns data types to variables by itself, simply by recognizing the value assigned to it.
print('Boolean A: ' + str(a));
print('Integer equivalent of A: ' + str(int(a)) + '\n');  # Here, we print the Integer equivalent of 'a = True', which is '1'.

b = False;
print('Boolean B: ' + str(b));
print('Integer equivalent of B: ' + str(int(b)) + '\n');  # Here, we print the Integer equivalent of 'b = False', which is '0'.

# The above examples also show us the working of the 'int(variable)' function. This is an example
# of dynamic 'type casting'. Which changes the value of 'a' from Boolean to Integer. Same for the variable 'b'.
# The example goes deeper in itself, where we see the result being further type-casted into a string variable
# for the purpose of printing. This is because the components being printed within the print() statements must
# share the same data type.

c = 1;      # Here, we assign Integer values to the variables 'c' and 'd'.
d = 0;

print('Integer C: ' + str(c));
print('Boolean equivalent of C: ' + str(bool(c)) + '\n');   # I believe by now, you'll have understood what's happening here.
                                                            # This print() statement outputs the Boolean equivalent of the the variable 'c = 1'.

print('Integer D: ' + str(d));
print('Boolean equivalent of D: ' + str(bool(d)) + '\n');

# So what are the Boolean equivalents of non-zero Integers. Have a look at the code below:
e = -1;
print('Integer E: ' + str(e));
print('Boolean equivalent of E: ' + str(bool(e)) + '\n');   # You'll find that the Boolean equivalent of any non-zero Integer, be it positive
                                                            # or negative, will always be True.

# Note this: The Boolean equivalent of any non-zero Integer is always True.
# But, the Integer equivalent of a Boolean 'True' can only be '1'. This, in a way, brings us to the conclusion
# that Booleans are a sub-class of Integers. This nature of Booleans allows us to add and subtract them with Integer values.
# Let's look at the next example:

f = 3;      # Here, 'f' is an Integer value.
print('Integer equivalent of F: ' + str(f));
g = f + True;       # Let's have another Integer value 'g', which is nothing but the addition of an Integer and a Boolean value.
print('G = F + True = ' + str(g));  # On printing the value of 'g', we get an Integer output 'g = 4'.

h = g - True;       # This one here is an example of how Boolean True values can be subtracted from Integers.
print('H = G - True = ' + str(h));

i = False + f;      # This one here is an example of how Boolean True values can be subtracted from Integers.
print('I = False + F = ' + str(i) + '\n');

# I hope the couple of examples demonstrated above have provided you with a clear understanding
# of how Integer values interact with Boolean values.

# Now, let's look into some Boolean type specific operators. Just as we saw type-specific operators
# for Integers, Python provides us with type specific operators for working on Boolean values.
# The three Boolean operators are 'not', 'or', and 'and'.

# The Boolean NOT:
j = True;
print('Boolean J: ' + str(j));
k = not True;
print('K = NOT J = ' + str(k) + '\n');

# The Boolean OR:
l = True;
m = False;
print('J: ' + str(j));     # The value of 'j' is True.
print('K: ' + str(k));     # The value of 'k' is False.
print('L: ' + str(l));     # The vlaue of 'l' is True.
print('M: ' + str(m) + '\n');   # The value of 'm' is False.

n = j or l;     # True OR True is True.
print('N = J OR L = ' + str(n));
o = j or m;     # True OR False is True.
print('O = J OR M = ' + str(o));
p = k or m;     # False OR False is False.
print('P = K OR M = ' + str(p) + '\n');

# The Boolean AND:
print('J: ' + str(j));     # The value of 'j' is True.
print('K: ' + str(k));     # The value of 'k' is False.
print('L: ' + str(l));     # The vlaue of 'l' is True.
print('M: ' + str(m) + '\n');   # The value of 'm' is False.

q = j and l;     # True AND True is True.
print('Q = J AND L = ' + str(q));
r = j and m;     # True AND False is False.
print('R = J AND M = ' + str(r));
s = k and m;     # False AND False is False.
print('S = K AND M = ' + str(s) + '\n');

# Well, I guess that covers how Boolean operators work on Boolean values. It's pretty simple, isn't it.
# Here's some extra, fun stuff that Python allows us to do with Boolean values.

t = True + True;   # This is an example of how Integer operators affect Boolean operands.
print('T = True + True = ' + str(t));   # In this case, the variable 't' is taken to be of Integer type.
                                        # However, you see that 't = True + True = 1'. Shouldn't the variable 't' be
# of type Boolean according to dynamic typing and give us the value 'True'?
# Fun isn't it?

# Let's look at a couple of more examples given below:.
u = True * False;       # Here, the value of 'u = True * False = 0', and not 'False'.
print('U = True x False = ' + str(u));

v = True + True + True;     # Here, we get 'v = True + True + True = 3', and not True.
print('V = True + True + True = ' + str(v) + '\n');

# Now, let's go a bit further with the fun stuff that shows us how Boolean operators affect Integer operands:
x = 1 and 1;
print('X = 1 AND 1 = ' + str(x));

y = 1 or 0;
print('Y = 1 OR 0 = ' + str(y));

z = 1 and 0;
print('Z = 1 AND 0 = ' + str(z) + '\n');
