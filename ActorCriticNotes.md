# Ok lets see if I can get the actor critic to work.... 
# SEE PAGE 258 for the process

## March 9
* set up inital agent random weights, as initac.h5.
* Run 5000 self play using self_play.py - output: ac_exp_1.h5 
* train with lr .01, bs 1024 note this is a learning rate way bigger then what i was using for pg.. oh well ;)