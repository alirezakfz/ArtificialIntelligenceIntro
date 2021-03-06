# Minimax

https://en.wikipedia.org/wiki/Bitboard

Minimax (sometimes MinMax, MM[1] or saddle point[2]) is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as "maximin"—to maximize the minimum gain. Originally formulated for two-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.

# Negamax
https://en.wikipedia.org/wiki/Negamax#Negamax_base_algorithm

Negamax search is a variant form of minimax search that relies on the zero-sum property of a two-player game.

This algorithm relies on the fact that {\displaystyle \max(a,b)=-\min(-a,-b)}{\displaystyle \max(a,b)=-\min(-a,-b)} to simplify the implementation of the minimax algorithm. More precisely, the value of a position to player A in such a game is the negation of the value to player B. Thus, the player on move looks for a move that maximizes the negation of the value resulting from the move: this successor position must by definition have been valued by the opponent. The reasoning of the previous sentence works regardless of whether A or B is on move. This means that a single procedure can be used to value both positions. This is a coding simplification over minimax, which requires that A selects the move with the maximum-valued successor while B selects the move with the minimum-valued successor.

It should not be confused with negascout, an algorithm to compute the minimax or negamax value quickly by clever use of alpha-beta pruning discovered in the 1980s. Note that alpha-beta pruning is itself a way to compute the minimax or negamax value of a position quickly by avoiding the search of certain uninteresting positions.

# Bitboard
https://en.wikipedia.org/wiki/Bitboard

A bitboard is a specialized bit array data structure commonly used in computer systems that play board games, where each bit corresponds to a game board space or piece. This allows parallel bitwise operations to set or query the game state, or determine moves or plays in the game.

Bits in the same bitboard relate to each other by the rules of the game, often forming a game position when taken together. Other bitboards are commonly used as masks to transform or answer queries about positions. Bitboards are applicable to any game whose progress is represented by the state of, or presence of pieces on, discrete spaces of a gameboard, by mapping of the space states to bits in the data structure. Bitboards are a more efficient alternative board representation to the traditional mailbox representation, where each piece or space on the board is an array element.

Bitboards are especially effective when the associated bits of various related states on the board fit into a single word or double word of the CPU architecture, so that single bitwise operators like AND and OR can be used to build or query game states.

Among the computer game implementations that use bitboards are chess, checkers, othello and word games. The scheme was first employed in checkers programs in the 1950s, and since the mid-1970s has been the de facto standard for game board representation in computer automatons.


<div>
  <h2 id="-adding-functionality-to-the-game-class">## Adding Functionality to the Game Class</h2>
<p>Your class only needs to define two additional methods before we can get started with the MiniMax algorithm: <code>get_legal_moves()</code> and <code>forecast_move()</code>. Finding legal moves uses the rules of the game to determine where each agent can go, then the forecast function can be used to expand the game tree along the branch corresponding to a legal move.</p>
<h3 id="finding-legal-moves">Finding Legal Moves</h3>
<p>The first function, <code>get_legal_moves()</code> takes no arguments and returns a <code>list</code> (the tests will fail for any other type of collection) of moves available to the active player in the current state. The "active" player is the agent with initiative to move (e.g., on an empty board player 1 is the active player, and initiative alternates after each move played). According to the game rules, each player can move to any open square for their first move, and then to any open square along a row, column, or diagonal from their current position. (Note that players cannot jump or pass through blocked squares.)</p>
<h3 id="forecasting-moves">Forecasting Moves</h3>
<p>The second function, <code>forecast_move()</code> takes a move (a pair of coordinates <code>(x, y)</code> of the desired endpoint of the player) and return a <strong>new</strong> game state object (you should not mutate game state objects). Treating the game state as immutable makes it trivial to roll out and unwind each branch of the game tree (children nodes will simply be garbage collected when the caller returns). (<em>Hint:</em> check out the <code>copy.deepcopy</code> module from the standard library to copy your board state.)</p>

</div>

</div>
