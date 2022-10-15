# Sus-Bot
The sus bot discord bot that connects to tinder API and twitter
as well as other stuff. Named after my discord server, that was created in highschool so.

Most code is within [cogs](cogs) file 
- main files are: 
  - [redit](cogs/redit.py)
    - searches subredit bassed on user input
  - [casino](cogs/casino.py)
    - casino games connected to the bots currency 
      - Blackjack
      - Slots
      - coinflip
      - Dice roll
  - [tinder](cogs/tinder.py)
    - Enter tinder api key through discort or through [config](config.py)
    - Bot connects to the account of who ever tpyes the initial comand. everyone can the respond like or dislike the first tinder recomendation. 
    - User can then message all or spacific matches through discord comand.
  
Each cog is a different file and a different class. They are discords way of grouping things.

Things other then [SusBot.py](SusBot.py) have been converted to a cog format but have not been deleted, but they are unused,
