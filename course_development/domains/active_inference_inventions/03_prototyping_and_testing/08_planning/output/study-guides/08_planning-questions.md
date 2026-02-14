# Study Questions: Test Planning Under Uncertainty

## Analytical Questions

1. Explain how expected free energy combines epistemic value and pragmatic value to determine test priority. Give an example where a high-epistemic-value test differs from a high-pragmatic-value test.

2. What are the essential components of a test protocol? Why must success and failure criteria be specified before testing begins?

3. Describe the "greedy algorithm" approach to resource allocation in testing. Under what conditions might a non-greedy approach be more effective?

4. What is testing debt, and how does it accumulate interest? Give an example of testing debt from the Boeing 787 case.

5. How do regulatory testing requirements interact with invention-specific testing needs? When do they align, and when do they conflict?

6. Explain the difference between parallel and sequential test planning. What determines whether two tests can be run in parallel?

7. What is a critical path in test planning, and why is it important for resource allocation?

8. How does pre-registration of test protocols support the bias mitigation strategies discussed in Module 04?

9. Describe how a comprehensive test plan should be updated as tests are completed and new information emerges. What triggers a re-prioritization?

10. What is the expected free energy rationale for testing cheap hypotheses before expensive ones? Under what conditions should this heuristic be overridden?

## Applied Questions

11. You are developing a wearable health monitor. List five hypotheses that need testing, rank them by expected free energy, and justify your ranking with specific uncertainty and consequence assessments.

12. Design a test protocol for testing whether a new type of bicycle tire reduces rolling resistance compared to a standard tire. Include hypothesis, procedure, measurements, sample size, controls, and success/failure criteria.

13. You have a $5,000 testing budget and 3 months. You have identified 12 hypotheses that need testing, with estimated costs ranging from $100 to $2,000 each. Design a resource allocation plan that maximizes total learning within your constraints.

14. A medical device startup has deferred biocompatibility testing for 6 months because the materials are "probably fine." Analyze this decision using the testing debt framework. What are the potential consequences?

15. Tesla prioritized battery safety testing over interior trim testing. Use the expected free energy framework to explain this choice. Under what conditions would a different prioritization be rational?

16. You are planning user tests for a new cooking appliance. You have access to 20 potential testers. Design a test plan that allocates these testers across three different test protocols (ease of use, safety, cleaning difficulty) to maximize total learning.

17. Your invention must pass both FCC electromagnetic compatibility testing and your own performance tests. The FCC test costs $3,000 and has a 3-week lead time. When should you schedule the FCC test in your overall test plan? What are the trade-offs of testing early vs. late?

18. A hardware project has the following test dependencies: sensor accuracy must pass before integration testing, integration testing must pass before user testing, and user testing must pass before regulatory submission. Draw the critical path. If sensor accuracy testing takes 2 weeks, integration testing takes 3 weeks, and user testing takes 4 weeks, what is the minimum total testing time?

19. You are halfway through your test plan, and an early test has revealed an unexpected issue that makes several later tests irrelevant. Describe how you would re-prioritize your remaining test plan using expected free energy principles.

20. Design a risk register for your testing process itself — not the risks to your invention, but the risks that testing could be disrupted (equipment failure, tester no-shows, supplier delays, scope creep). For each risk, specify likelihood, impact, and mitigation.
