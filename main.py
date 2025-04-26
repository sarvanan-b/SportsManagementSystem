"""Sports Management System

Design a database to keep track of the teams and games of a sport league. 
A team has a number of players, not all of whom participate in each game.
It is desired to keep track of the players participating in each game of each team and the result of the game"""


from website import create_app

app=create_app()

if __name__ =='__main__':
    app.run(debug=True)