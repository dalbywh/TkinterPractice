"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and William Dalby.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import rosegraphics as rg



def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding = 20)
    frame1.grid()
    # ------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    yes_button = ttk.Button(frame1, text = 'Hi')
    yes_button.grid(row = 0, column = 1)
    # ------------------------------------------------------------------
    # done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    yes_button['command'] = (lambda: print_stuff('Hello'))
    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    is_it_ok = ttk.Label(frame1, text= 'Tests to see if the string is "ok" ')
    is_it_ok.grid(row = 1, column = 0)
    entry_button = ttk.Entry(frame1)
    entry_button.grid(row = 2, column = 0)

    maybe_hello_button = ttk.Button(frame1, text = 'Enter a string, please')
    maybe_hello_button['command'] = lambda: test_for_ok(entry_button)

    maybe_hello_button.grid(row = 3, column = 0)



    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    number_of_times = ttk.Label(frame1, text ='The number of times your '
                                              'other string will be entered')
    number_of_times.grid(row = 1, column = 2)
    n_times = ttk.Entry(frame1)
    n_times.grid(row = 2, column = 2)

    entry_print = ttk.Button(frame1, text = 'Prints the other string')
    entry_print['command'] = lambda: print_n_times(entry_button, n_times)
    entry_print.grid(row=3, column = 2)

    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    circle_color = ttk.Label(frame1, text= 'Enter the color of the circle')
    circle_color.grid(row = 6, column = 0)

    circle_color_entry = ttk.Entry(frame1)
    circle_color_entry.grid(row = 7, column = 0)

    circle_radius = ttk.Label(frame1, text ='Enter the radius of the circle')
    circle_radius.grid(row = 6, column = 2)

    circle_radius_entry = ttk.Entry(frame1)
    circle_radius_entry.grid(row = 7, column = 2)

    circle_make = ttk.Button(frame1, text ='Make the circle')
    circle_make['command'] = lambda: make_circle(circle_radius_entry,
                                                circle_color_entry)

    circle_make.grid(row = 8, column = 1)

    root.mainloop()

def print_stuff(string):
    print(string)

def test_for_ok(string):
    contents = string.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def print_n_times(entry, n):
    contents = entry.get()
    number = int(n.get())
    for k in range (number):
        print(contents)

def make_circle(r, c):
    radius = int(r.get())
    color = c.get()

    window = rg.RoseWindow(400, 400)
    circle = rg.Circle(rg.Point(200, 200), radius)
    circle.fill_color = color
    circle.attach_to(window)

    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
