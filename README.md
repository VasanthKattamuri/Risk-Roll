# Risk-Roll

This project is a console-based implementation of the Pig game, a simple dice game where players compete to reach a target score first. Each player rolls a die multiple times, adding up points as they go, with a twist: rolling a 1 instantly ends the turn and sets the turn's score to zero! Players must decide when to stop and "bank" their points to avoid losing them.

## Game Rules
- **Objective**: Be the first player to reach the maximum score (default is 50).
- **Players**: 2 to 4 players can play.

### Rolling the Die:
- Players roll a die and add the result to their current turn score.
- Players can keep rolling or choose to stop and add their current turn score to their total score.

### Penalty for Rolling a 1:
- If a player rolls a 1, their current turn score is reset to 0, and their turn ends.
- Their total score remains unchanged from before that turn.

### Winning the Game:
- The first player to reach or exceed the target score (50) wins.

## Code Highlights
- **Player Turn Logic**: Each player rolls until they decide to stop or roll a 1, with all scores tracked throughout.
- **Multiplayer Support**: Allows between 2 to 4 players, and alternates turns until someone wins.

Enjoy the game and challenge your friends to a dice-rolling showdown!
