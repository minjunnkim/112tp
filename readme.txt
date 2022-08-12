Complex Beauti.py - Julia Visualization
This program accepts user input for "c", in the function f(z) = z^2 + c, widely known due to the sets it creates through repeated iterations.
The most famous may be the Mandelbrot Set, but I took more interest in the Julia Set. The value "c" is a complex number, with format x+yi.
Given such value, this program will calculate the Julia Set corresponding to it, by iterating through all pixels in 480x360, and getting 
the color based on the number of iterations the specific "z"th pixel in the 480x360 screen goes through. This concept is better understood
looking at the visualization, rather than try to do the calculation in your head :)

------------------------------------------------------------------------------------------------------------------
Here is a definition of Julia Set from Wikipedia if you would like.

In the context of complex dynamics, a branch of mathematics, 
the Julia set and the Fatou set are two complementary sets (Julia "laces" and Fatou "dusts") 
defined from a function. Informally, the Fatou set of the function consists of values with the 
property that all nearby values behave similarly under repeated iteration of the function, 
and the Julia set consists of values such that an arbitrarily small perturbation can cause 
drastic changes in the sequence of iterated function values. Thus the behavior of the 
function on the Fatou set is "regular", while on the Julia set its behavior is "chaotic".
------------------------------------------------------------------------------------------------------------------

To run this project, you need the cmu_112_graphics, which is already included, numpy, and matplotlib.

Now let's go through the project functions.

First, if you would like to use the animation function, you must run the "juliaAni.py" first and follow the instruction
on the console. This will take a while as it needs to render all the frames before creating the .gif file and saving it to your computer.
However, lowering the number of frames on juliaAni.py may lower the time. 
Then, run the "Complex Beauti.py" file and click on the animate button to see the animation you created in "juliaAni.py".

You may want to start the animation processing first, try out the regular Julia Set visualization, and then come back to animation.
If you do not want to wait for the entire process, you can simply try the pre-input gif's version of the animation. 
(No need to run "juliaAni.py" for this. Simply click on the animate button on "Complex Beauti.py")

If you would like to use the regular Julia Set visualization function, simply run the "Complex Beauti.py" file without having to run 
"juliaAni.py" prior. Then, click on the julia button to enter your custom "c" value. Make sure the value is between -1 and 1! The
instructions will also be on the screen. If you would like to try out some of the coolest looking ones, try clicking on the Presets button found on the
bottom left of the main screen!

Shortly, the Julia Set Visualization screen will show up along with the back button, zoom in/out button,
and increase/decrease maximum iteration button. Using the arrow keys on the keyboard, you can move the visualization in the four directions.

Notice that increasing the maximum iteration will decrease the amount of "layers" on the visualization,
but increase the sharpness of the white regions and that decreasing it will increase the amount of "layers" on the visualization, making the visualization
seem more "pretty" if you would say so. Note that higher maximum iteration is a more accurate version.

Using the To recursive/To normal button, you can change between the calculation algorithms, one recursive and one a regular iteration until fail.

Using the change color button, you can change the color of the visualization with your input rgb value!

There are no shortcut commands.