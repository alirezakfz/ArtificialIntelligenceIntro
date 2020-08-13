<div>
  <h2 id="-starting-to-code-minimax">## Starting to Code Minimax</h2>
<p>Now that we have a complete game class, and the lectures have introduced the core concept of minimax while walking through the basic procedure in the quizzes, the next step is to do it all with code. In this exercise you're going to implement the two helper functions required by the minimax algorithm.</p>
<h3 id="the-minimax-algorithm">The Minimax Algorithm:</h3>
<p>Recall the minimax algorithm originally presented at the beginning of this lesson (shown below). We will start by coding helper functions: a terminal state test, the min-value function, and the max-value function. Notice that the <code>min-value()</code> and <code>max-value()</code> functions only need to return a single number -- a "utility value" -- which is the score of the current branch; the function for selecting a move based on those scores will come in a later quiz.</p>
</div>
