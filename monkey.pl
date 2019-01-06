% adapted from Bratko, I. (1986) "Prolog: Programming for Artificial Intelligene." Addison-Wesley. 
% Modify by Hoang Van Loc
% initial state: Monkey is at door, 
%                Monkey is on floor, 
%                Box is at window, 
%                Monkey doesnxt have banana,
%                Banana at the middle
%

% How to use
% ?- canget(state(atdoor, onfloor, atwindow, hasnot), Plan).
% Plan = [walk(atdoor, atwindow), push(atwindow, middle), climb, grasp] 
% Yes

% ?- canget(state(atwindow, onbox, atwindow, hasnot), Plan ).
% No

% ?- canget(state(Monkey, onfloor, atwindow, hasnot), Plan).
% Monkey = atwindow
% Plan = [push(atwindow, middle), climb, grasp] 
% Yes
% prolog structure: structName(val1, val2, ... )

% state(Monkey location in the room, Monkey onbox/onfloor, box location, has/hasnot banana)


% legal actions

do( state(middle, onbox, middle, hasnot),   % grab banana at the middle
    grab,
    state(middle, onbox, middle, has) ). 

do( state(L, onfloor, L, Banana),           % Climb to the box 
    climb,
    state(L, onbox, L, Banana)).

do( state(L, onbox, L, Banana),
	drop,
	state(L, onfloor, L, Banana)).				% come down the box

do( state(L1, onfloor, L1, Banana),         % push box from L1 to L2
    push(L1, L2),  
    state(L2, onfloor, L2, Banana) ).

do( state(L1, onfloor, Box, Banana),        % walk from L1 to L2
    walk(L1, L2),
    state(L2, onfloor, Box, Banana) ).


% canget(State): monkey can get banana in State

canget(state(_, _, _, has)).                % Monkey already has it, goal state

canget(State1) :-                           % not goal state, do some work to get it
	do(State1, Action, State2),           % do something (grab, climb, push, walk) 
	canget(State2).                       % canget from State2
% get plan = list of actions 

canget(state(_, _, _, has), []).            % Monkey already has it, goal state

canget(State1, Plan) :-                     % not goal state, do some work to get it
      do(State1, Action, State2),           % do something (grab, climb, push, walk) 
      canget(State2, PartialPlan),          % canget from State2
      add(Action, PartialPlan, Plan).       % add action to Plan

add(X,L,[X|L]).



