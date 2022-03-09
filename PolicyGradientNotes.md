## notes testing the policy gradient (Chapter 9 and 10)

### Steps to take

1 - run initagent to set up initial (brain dead) bots. I am using 9x9  (WORKS)
2 - Execute self play (selfplay) with the bot to collect experience.-> output experience file (WORKS)
3 - TRAIN the bot on the experience. train_pg.py (WORKS) -> Outputs a new (better?) bot
4 - Check to see if it actually is better. (eval_pg_bot.py)  -> Test old vs new bot 100 runs need 60 wins. 
   for 1000 need 525  (so more precise)  (about 5% sig level, very roughly)

### Experiment log

March 8 2022
* Trying 1028 game batches of self play, batch size 512, lr = .001 
* no measurable improvement  ( i am testing 1000 games, need win rate of 525 to be 'better' at about 5% level )
* toss out that one and try another 1028 games.  Train on both batches, same parameters.
* 519 wins for agent 1, not great but i am going to go with it. 
* round1.h5 self play for 2000 games saved in exp_batch3.h5
* training into round2.h5 complete , tested vs round1.ht: New agent 497/1000....  Shiza!
* Next: retrain with higher learning rate .01 ? just to see how  shitty that is.
* maybe .0005 ? going the other way? Cant really detect any difference
* with .0005 -> round2.h5 bot scored :   vs round1.h5 bot 499/1000
* if fail -> round1.h5 self play 4000 more games saved in exp_batch4.h5  <DONE>

March 9 2022
* train exp 4 and 3 together to round2 again lr= .0001, batch 1024 - score round2 vs round1: 491 for agent new one.
* Try train again with lr =.0005, bs 1024  result:  476. Ok wtf is happening? Why is it worse?
*  Fail again, hmm At local minimum seems unlikely after just one round, but not sure what else to try. T= .01 ? 
* self play 4000 games exp_batch5.h5, with T= .01
* train with both batch4 and batch5,   use lr=.0005, bs 1024.  Note that at one point the loss was .2, but then went down to 0.1 (here high loss is good since we are using cross entropy) Try again with lr = .0001 ? Same kind of result, if anything worse. 
* 100 games round2 vs round1: 48/100.  . 400 games: 191.  It is worse then round 1 bot.
And I am done with that lol. (Note even round2 still beats the random guy, so i guess that is something, however I played it and it is PATHETIC)
 


### Bottom line
* THIS IS SLOW AF.   THe book sites demo uses 84000 games, so not so suprising I suppose!
* Move on to Actor Critic
