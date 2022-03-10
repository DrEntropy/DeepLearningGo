# Ok lets see if I can get the actor critic to work.... 
# SEE PAGE 258 for the process

## March 9
* set up inital agent random weights, as initac.h5.
* Run 5000 self play using self_play.py - output: ac_exp_1.h5 
* using defailt loss weights [1.0,0.5]
* train with lr .01, bs 1024 note this is a learning rate way bigger then what i was using for pg.. oh well ;)
* diverged with 0.01 trying 0.005 still diverges.  0.001 doesnt diverge but win rate 50% is result.
* loss_weights=[1.0, 0.2] , .002 lr  still 51% result
* .004 same loss weights -- diverges. I guess i could try 0.003 ? Instead i am going to try this with official repo and see if it works there. 