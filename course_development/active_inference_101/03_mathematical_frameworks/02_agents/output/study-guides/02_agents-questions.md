# Mathematical Frameworks — Module 02: Agents — Study Questions

1. Why is exact Bayesian inference usually intractable?
2. How many state combinations exist if you have 100 binary hidden states? Why is this a problem?
3. What is the recognition model q(s)? How does it relate to the true posterior P(s | o)?
4. What is variational inference? How does it turn inference into optimization?
5. Define KL divergence in words. What does it measure?
6. Write the formula for KL divergence D_KL[q(s) || P(s | o)].
7. What are the three key properties of KL divergence?
8. Why is KL divergence not a true "distance" metric? (Hint: symmetry)
9. What is the ELBO? What does it stand for?
10. Write the ELBO decomposition: ELBO = accuracy - complexity. What does each term mean?
11. Why can't we minimize D_KL[q || P(s|o)] directly?
12. What is variational free energy F? How does it relate to the ELBO?
13. Show that minimizing F is equivalent to minimizing KL divergence.
14. What happens to F when q(s) = P(s | o)? What is the value of F in that case?
15. How does the accuracy-complexity trade-off in the ELBO relate to Occam's razor?
16. In what sense is the brain performing variational inference?
17. What is the "mean-field approximation"? How does it simplify q(s)?
18. How does variational free energy relate to the prediction error minimization from the Cognitive Science unit?
19. Can variational inference be exact? Under what conditions?
20. Why is variational inference important for understanding both biological brains and artificial intelligence?
