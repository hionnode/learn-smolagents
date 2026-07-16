# Learning smolagents — mini plan

Goal: understand smolagents well enough to build and ship a small real agent, without over-investing if it turns out to be the wrong tool.

## Stage 0 — Baseline (done)
- Minimal `CodeAgent` + `DuckDuckGoSearchTool` + `InferenceClientModel` running (`main.py`).
- **Off-ramp:** if this doesn't run cleanly (auth/model access issues), stop here and fix environment before going further — no point building on a broken base.

## Stage 1 — Core concepts (~1–2 hrs)
- Read smolagents docs on `CodeAgent` vs `ToolCallingAgent` — smolagents' signature idea is agents that write Python code to call tools instead of emitting JSON tool calls.
- Understand the run loop: think → write code → execute in sandbox → observe → repeat until `final_answer`.
- Try swapping the model (e.g. a local/open model via `InferenceClientModel` or `LiteLLMModel`) to see how model-agnostic the abstraction is.
- **Off-ramp:** if the code-writing-agent paradigm feels like the wrong fit for your use case (e.g. you need strict structured output, not free-form code execution), this is the point to reconsider — that's smolagents' core differentiator, and everything else builds on it.

## Stage 2 — Tools (~1–2 hrs)
- Build one custom tool with the `@tool` decorator and one with a `Tool` subclass.
- Give the agent 2–3 tools and watch how it plans/chains calls.
- **Off-ramp:** if writing tools feels clunky compared to alternatives (LangChain, OpenAI function calling, plain function-calling loop), note why — that's a real signal, not a reason to push through out of sluggishness.

## Stage 3 — Multi-agent / orchestration (~1–2 hrs)
- Try a manager agent delegating to a sub-agent (`managed_agents`).
- Look at planning steps, memory/step logs, and `agent.logs` for debuggability.
- **Off-ramp:** if you don't have a use case that needs multi-agent delegation, skip this — it's the most complex part of the library and often unnecessary for single-purpose agents.

## Stage 4 — Sandbox & safety (~30–60 min)
- Understand how code execution is sandboxed (local Python exec vs Docker/E2B remote executors).
- Decide what's acceptable for your deployment target.
- **Off-ramp:** if you need strong sandboxing guarantees smolagents doesn't give out of the box, this is a hard blocker for production use — evaluate before investing further.

## Stage 5 — Build a real small project (~half day)
- Pick one concrete task (e.g. a research assistant, a data-wrangling agent) and build it end-to-end with proper tools, error handling, and a couple of test prompts.
- This is the actual validation step: does smolagents make *this* easier than writing a bespoke loop?

## Exit criteria
- **Keep using smolagents** if Stage 5's project came together faster/cleaner than expected.
- **Drop it** if you hit repeated friction in Stage 1–2 (paradigm mismatch) or Stage 4 (sandboxing) — better to find out cheaply than after a real build.
