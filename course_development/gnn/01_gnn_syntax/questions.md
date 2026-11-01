# GNN Syntax Track — GNN Syntax — Study Questions

1. What problem does Generalized Notation Notation (GNN) solve that prose descriptions of generative models do not?
2. What are the three forms in the "triple play," and what does moving between them require?
3. Name the required sections of a GNN file in the order the exemplar corpus uses them, and state what each one declares.
4. Why does the GNN state space block separate variable declarations (`A[2,2,type=float]`) from numeric values (`InitialParameterization`)?
5. In the Static Perception Model, what does the connection list `D>s`, `s-A`, `A-o`, `s-B`, `B>u`, `u>s` assert about the model?
6. What convention fixes the orientation of the likelihood matrix in the exemplar, and what are the rows and columns?
7. For the exemplar's matrix `A`, what is `P(o = 1 | s = 0)`, and how do you know?
8. Compute `q(s)` after observing `o = 1` with the uniform prior `D = (0.5, 0.5)`. Show the numerator, denominator, and final values.
9. Why does the exemplar state that "A is a likelihood, not a posterior Q(s|o)"?
10. What is the purpose of the `ActInfOntologyAnnotation` section, and how does it differ from the state space block?
11. The exemplar's footer notes a "minimal action/transition component." Why does a perception model include a transition tensor at all?
12. In the transition tensor `B[next_state, previous_state, action]`, what does each index mean, and what does "column-stochastic per action slice" mean?
13. Which pipeline steps parse, type-check, render, and execute a GNN specification?
14. Why do steps 3 and 5 work without any simulation framework installed, while steps 11 and 12 may report `unsupported`?
15. What does it mean that a framework reports a model as `unsupported` rather than failing to render it?
16. Which exemplar in this track adds action selection to perception, and which adds parameter learning?
17. Why are no exemplar models shipped for the Elementary and Family levels of the curriculum?
18. How would you verify that a shipped exemplar is an unmodified copy of the GNN corpus file?
19. Pick one variable in the Static Perception Model and explain how the ontology annotation makes localization (for example, a Spanish-language annotation) possible without changing the model.
20. In your own words: what does a student gain from seeing the same model as text, as a graph, and as executable code?
