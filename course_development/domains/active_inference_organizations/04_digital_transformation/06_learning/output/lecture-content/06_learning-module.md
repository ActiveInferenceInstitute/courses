# Machine Learning and Organizational Adaptation: How Digital Systems Learn

## Executive Summary

Machine learning gives organizations the ability to build systems that **update their own models from data** — automating the learning process itself. Under Active Inference, ML is formalized model updating: algorithms that revise their generative models based on new evidence. This module covers ML deployment in organizations, the model lifecycle, data feedback loops, and the challenge of maintaining ML systems as the world changes.

---

## Learning Objectives

1. Frame **machine learning** as automated model updating within the Active Inference framework
2. Understand the **ML lifecycle** — from data collection through model deployment and monitoring
3. Design **feedback loops** that keep ML models aligned with organizational objectives
4. Address **model drift** — when models degrade because the world changes
5. Navigate **MLOps** — the operational infrastructure for managing ML at scale

---

## Key Concepts

### 1. ML as Automated Inference

| ML Function | Active Inference Translation | Organizational Application |
|------------|----------------------------|---------------------------|
| **Supervised learning** | Learning the mapping from observations to hidden states | Customer churn prediction, fraud detection |
| **Unsupervised learning** | Discovering structure in observations without labeled states | Customer segmentation, anomaly detection |
| **Reinforcement learning** | Learning optimal policies through action-outcome feedback | Dynamic pricing, resource allocation |
| **Deep learning** | Hierarchical generative models with many layers | Image recognition, NLP, recommendation |

### 2. The ML Model Lifecycle

```
Data Collection → Data Preparation → Model Training → Evaluation → Deployment → Monitoring → Retraining
```

Each stage introduces potential failure:

- **Data collection**: Biased or incomplete data
- **Training**: Overfitting, wrong objectives
- **Deployment**: Integration failures, latency issues
- **Monitoring**: Undetected drift, silent failures

### 3. Model Drift and Retraining

**Case Study — Zillow's iBuying Algorithm**: Zillow's "Zestimate" algorithm, which predicted home prices, worked well in stable markets but failed catastrophically when the 2021 housing market shifted rapidly. The model was trained on historical patterns that no longer held — a textbook case of model drift. Zillow lost $381M and shut down the iBuying division. The lesson: ML models are not "set and forget" — they require continuous monitoring and retraining as the world changes.

### 4. Organizational ML Maturity

| Level | Characteristics | Challenge |
|-------|----------------|-----------|
| **Ad hoc** | Individual data scientists build models | No standards, no reproducibility |
| **Repeatable** | Standard processes for model development | Limited scale, manual deployment |
| **Managed** | MLOps infrastructure, automated pipelines | Organizational integration |
| **Optimized** | ML embedded in core business processes | Maintaining alignment as scale increases |

---

## Cross-References

- For organizational learning, see [Organizational Systems: Learning](../../01_organizational_systems/06_learning/module.md)
- For collective memory, see [Collective Intelligence: Learning](../../02_collective_intelligence/06_learning/module.md)
- For adaptive strategy, see [Strategic Modeling: Learning](../../03_strategic_modeling/06_learning/module.md)

---

## Summary

| Concept | Digital Transformation Meaning |
|---------|-------------------------------|
| Machine learning | Automated model updating from data |
| ML lifecycle | Data → training → deployment → monitoring → retraining |
| Model drift | Model degradation as the world changes |
| MLOps | Operational infrastructure for managing ML at scale |
| Feedback loops | Mechanisms for keeping ML models aligned with objectives |

---

## References

- Sculley, D. et al. (2015). Hidden technical debt in machine learning systems. *NeurIPS*.
- Paleyes, A. et al. (2022). Challenges in deploying machine learning. *ACM Computing Surveys*, 55(6).
