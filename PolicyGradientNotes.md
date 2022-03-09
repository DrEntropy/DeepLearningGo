## notes testing the policy gradient (Chapter 9 and 10)

### Steps to take

1 - run initagent to set up initial (brain dead) bots. I am using 9x9  (WORKS)
2 - Execute self play (selfplay) with the bot to collect experience.-> output experience file (WORKS)
3 - TRAIN the bot on the experience. train_pg.py (WORKS) -> Outputs a new (better?) bot
4 - Check to see if it actually is better. (eval_pg_bot.py)  -> Test old vs new bot

March 8 2022
* Trying 1028 game batches of self play, batch size 512, lr = .001 
* no measurable improvement  ( i am testing 1000 games, need win rate of 525 to be 'better' at about 5% level )
* toss out that one and try another 1028 games.  Train on both batches, same parameters.
* 519 wins for agent 1, not great but i am going to go with it. 
* round1.h5 self play for 2000 games saved in exp_batch3.h5
* training into round2.h5 complete , tested vs round1.ht: New agent 497/1000....  Shiza!
* Next: retrain with higher learning rate .01 ? just to see how  shitty that is.
* maybe .0005 ? going the other way? Cant really detect any difference
* with .005 -> round2.h5 bot scored :   vs round1.h5 bot 499/1000
* if fail -> round1.h5 self play 2000 more games saved in exp_batch4.h5

** CONSIDER MAKING T>0 to get more variation? except this should not matter until later **


### Bottom line
* THIS IS SLOW AF.   THe book sites demo uses 84000 games.
* I think i will stop when i see any improvement at all and move on to next chapter ;)
