## notes testing the policy gradient (Chapter 9 and 10)

### Steps to take

1 - run initagent to set up initial (brain dead) bots. I am using 9x9  (WORKS)
2 - Execute self play (selfplay) with the bot to collect experience.  (WORKS)
3 - TRAIN the bot on the experience. train_pg.py (WORKS)
4 - Check to see if it actually is better. (eval_pg_bot.py)