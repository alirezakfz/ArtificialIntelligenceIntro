<div>
  <h2 id="-starting-to-code-minimax">## Starting to Code Minimax</h2>
<p>Now that we have a complete game class, and the lectures have introduced the core concept of minimax while walking through the basic procedure in the quizzes, the next step is to do it all with code. In this exercise you're going to implement the two helper functions required by the minimax algorithm.</p>
<h3 id="the-minimax-algorithm">The Minimax Algorithm:</h3>
<p>Recall the minimax algorithm originally presented at the beginning of this lesson (shown below). We will start by coding helper functions: a terminal state test, the min-value function, and the max-value function. Notice that the <code>min-value()</code> and <code>max-value()</code> functions only need to return a single number -- a "utility value" -- which is the score of the current branch; the function for selecting a move based on those scores will come in a later quiz.</p>
</div>
div>
  <h2 id="simplifying-assumptions">Simplifying Assumptions:</h2>
<p>We will also make two simplifying assumptions in order to adhere to the conventions of Thad's quizzes:</p>
<ul>
<li>Assumption 1: a state is terminal if the active player has no remaining moves</li>
<li>Assumption 2: the board utility is -1 if it terminates at a max level, and +1 if it terminates at a min level</li>
</ul>
<p>The first assumption is only required to support the second assumption. In general, we can determine that a game is terminal if <em>either</em> player has no remaining moves, but that would require terminal nodes at both min and max levels to support returning +1 or -1 depending on which player is the winner.  Restricting the terminal condition to the active player means that there is only one possible return value at min or max nodes, but the consequence is that the search will sometimes go one layer deeper in the tree than absolutely necessary.</p>
<p>The second assumption is specified in the lecture quizzes. Technically, any pair of values can be used to indicate wins and losses so long as they admit an ordering such that the score for winning is greater than the score for losing; e.g., instead of -1 &amp; +1 you could you use -π &amp; π/2, or 100.99 &amp; 101.0, or -∞ &amp; +∞. It is common to use -∞ &amp; +∞ when a heuristic function is used (which we'll do in another project for this module) because every possible heuristic estimate lies between those bounds, which avoids a possible bug where your agent prefers a non-terminal state scored by the heuristic to a terminal state with a "true" win or loss score.</p>
<p><strong>Important Note:</strong> Notice that the value does not depend on which player is "active" on the board. A win for the searching player (the player that initiated the search from the root of the game tree) is always worth +1 and a loss is always worth -1. One <em>very</em> common mistake is to "flip" the utility between min and max nodes, but the score should be relative to the desirability of the outcome for the searching player.</p>
</div>

<div>
  <h2 id="-minimax-decision-choosing-the-best-branch">## Minimax Decision: Choosing the Best Branch</h2>
<p>Now it's time to bring it all together to complete the minimax algorithm.  The <code>minimax_decision()</code> function in the quiz below should implement the eponymous procedure from the pseudocode. It should loop over the legal moves from the current state and return the move that has the highest score. The scores are determined by mutually recursive calls between the min and max value helper functions until a terminal state is reached, and propagated back up the tree as the call stack unwinds. </p>
<p>Just like in the previous quiz, the root node of the tree is itself a "max" node, so we call <code>min_value()</code> first on each legal move. </p>
<p><strong>Hints:</strong> </p>
<ul>
<li>One way to implement this function has a body that looks very similar to the <code>max_value()</code> function, except that you must keep track of both the best score and best move (and return only the best move)</li>
<li>There are also clever ways to do it using the built-in <a href="https://docs.python.org/2/library/functions.html#max" target="_blank">max</a> function and the optional keyword argument <code>key</code>.</li>
</ul>
</div>
