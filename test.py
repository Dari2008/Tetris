i = 0;

x = 10;
y = 15;

width = 10;
height = 15;

if y % 2 == 0:
    i = x + (y * width);
else:
    i = width - x + (y * width);

print(i)