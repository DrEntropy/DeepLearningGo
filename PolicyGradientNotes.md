## notes testing the policy gradient (Chapter 9 and 10)

### Steps to take

1 - run initagent to set up initial (brain dead) bots. I am using 9x9  (WORKS)
2 - Execute self play (selfplay) with the bot to collect experience.-> output experience file (WORKS)
3 - TRAIN the bot on the experience. train_pg.py (WORKS) -> Outputs a new (better?) bot
4 - Check to see if it actually is better. (eval_pg_bot.py)  -> Test old vs new bot


* Trying 1024 game batches of self play, batch size 512, lr = .001 
* no measurable improvement  ( i am testing 1000 games, need win rate of 525 to be 'better' at about 5% level )
