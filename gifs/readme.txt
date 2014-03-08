microban-default-1.gif
----------------------
	Original Rules:
		89: [ > player | crate ] -> [ > player | > crate ]

	Solution:
		[2, 1, 0, 3, 3, 3, 2, 1, 0, 1, 1, 2, 2, 3, 0, 1, 0, 3, 0, 0, 1, 2, 3, 2, 2, 3, 3, 0, 1, 2, 1, 0, 0]

	Iterations:
		1067	

microban-evolve-1.gif
---------------------
	Original Rules:
		89: [ > player | crate ] -> [ > player | > crate ]

	Mutators:
		1) RuleDirectionMutator

	New Rules:
		89: [ ^ player | crate ] -> [ ^ player | ^ crate ]

	Solution:
		[0, 1, 3, 1, 2, 0, 2, 2, 3, 0, 1, 3, 0, 0, 1, 3, 1, 2, 0, 2, 2, 3, 2, 3, 1, 1]

	Iterations:
		187

	Description:
		Mechanic here seems to describe the act of pull/tugging object blocks, but only when the player is on the side of said block.


