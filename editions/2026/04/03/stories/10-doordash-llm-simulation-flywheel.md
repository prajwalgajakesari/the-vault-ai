# DoorDash Engineers Build Simulation Flywheel to Test LLM Customer Support at Scale

DoorDash engineers tackled a critical challenge in deploying LLM-based support systems: how do you validate a system that never produces identical responses twice? Their solution is a simulation and evaluation flywheel that enables rapid iteration on chatbots before production deployment.

The framework uses an LLM-as-customer to play against the production chatbot, creating realistic multi-turn exchanges. Engineers can validate improvements through hundreds of simulated conversations in minutes versus weeks of live A/B testing.

## Engineering Results

DoorDash implemented a case state layer that reduced hallucination rates by approximately 90 percent. Guardrail systems achieved a 99% reduction in potentially severe compliance issues. Using Claude 3 Haiku on Amazon Bedrock, the system achieves 2.5-second response latency.

Amazon SageMaker's testing framework enabled a 50x increase in automated test capacity. The company uses Promptfoo to treat prompt engineering akin to unit testing in software development.

## Closed-Loop System

The real value emerges from treating the flywheel as a closed loop: identify failures, create LLM-as-judge evaluators calibrated against human judgment, generate simulated conversations, identify failures, and iterate until acceptable thresholds are met.

## What Comes Next

DoorDash's architecture—simulation-driven validation, LLM-as-judge evaluation, human feedback loops, and continuous improvement—will likely become standard practice as LLMs become more integral to customer support workflows.