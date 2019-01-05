% Modify by Hoang Van Loc
:- dynamic on/2.

% How to use
% swipl box.pl
% do[()()]. to excute algorithm
% example: do[on(a,table),on(b,a),on(c,b),on(d,c)]
% listing(on). to check last state of box
% listing(move). to check all move in last do

% Initial state
on(a,table).    
on(b,table).    
on(c,table).
on(d,table).

% Put block on other block
put_on(A,B) :-
     A \== table,
     A \== B,
     on(A,X),
     clear(A),
     clear(B),
     retract(on(A,X)),
     assert(on(A,B)),
     assert(move(A,X,B)).

% assume that table always clear
clear(table).

% Clear block
clear(B) :- 
     not(on(_X,B)).

r_put_on(A,B) :-
     on(A,B).
r_put_on(A,B) :-
     not(on(A,B)),
     A \== table,
     A \== B,
     clear_off(A),        
     clear_off(B),
     on(A,X),
     retract(on(A,X)),
     assert(on(A,B)),
     assert(move(A,X,B)).

clear_off(table).    
clear_off(A) :-      
     not(on(_X,A)).

% clear recursion
clear_off(A) :-
     A \== table,
     on(X,A),
     clear_off(X),      
     retract(on(X,A)),
     assert(on(X,table)),
     assert(move(X,A,table)).

% Do with final state
do(Glist) :- 
      valid(Glist), 
      do_all(Glist,Glist). 

valid(_).                          
   
% recursion until empty stack
do_all([G|R],Allgoals) :-          /* already true now */
     call(G),
     do_all(R,Allgoals),!.         /* continue with rest of goals */

do_all([G|_],Allgoals) :-          /* must do work to achieve */
     achieve(G),
     do_all(Allgoals,Allgoals).    /* go back and check previous goals */
do_all([],_Allgoals).              /* finished */

achieve(on(A,B)) :-
     r_put_on(A,B).