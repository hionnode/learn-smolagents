# Learning smolagents — mini plan

Goal: understand smolagents well enough to build and ship a small real agent, without over-investing if it turns out to be the wrong tool.

## Stage 0 — Baseline (done)
- Minimal `CodeAgent` + `DuckDuckGoSearchTool` + `InferenceClientModel` running (`main.py`).
- **Resources:** [huggingface/smolagents](https://github.com/huggingface/smolagents) (README quickstart), [docs index](https://huggingface.co/docs/smolagents/index)
- **Off-ramp:** if this doesn't run cleanly (auth/model access issues), stop here and fix environment before going further — no point building on a broken base.

## Stage 1 — Core concepts (~1–2 hrs)
- Read smolagents docs on `CodeAgent` vs `ToolCallingAgent` — smolagents' signature idea is agents that write Python code to call tools instead of emitting JSON tool calls.
- Understand the run loop: think → write code → execute in sandbox → observe → repeat until `final_answer`.
- Try swapping the model (e.g. a local/open model via `InferenceClientModel` or `LiteLLMModel`) to see how model-agnostic the abstraction is.
- **Resources:**
  - Blog: [Introducing smolagents](https://huggingface.co/blog/smolagents) (HF, design rationale for "code agents")
  - Docs: [Guided tour](https://huggingface.co/docs/smolagents/guided_tour), [Building good agents](https://huggingface.co/docs/smolagents/tutorials/building_good_agents)
  - Paper-ish background: [Executable Code Actions Elicit Better LLM Agents (CodeAct)](https://arxiv.org/abs/2402.01030) — the research idea smolagents is built on
- **Off-ramp:** if the code-writing-agent paradigm feels like the wrong fit for your use case (e.g. you need strict structured output, not free-form code execution), this is the point to reconsider — that's smolagents' core differentiator, and everything else builds on it.
  - **Explore instead:** [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (typed, structured-output-first agents) or [openai/openai-agents-python](https://github.com/openai/openai-agents-python) (classic tool-calling loop, no code-exec).

## Stage 2 — Tools (~1–2 hrs)
- Build one custom tool with the `@tool` decorator and one with a `Tool` subclass.
- Give the agent 2–3 tools and watch how it plans/chains calls.
- **Resources:** [Tools docs](https://huggingface.co/docs/smolagents/tutorials/tools), [smolagents `examples/`](https://github.com/huggingface/smolagents/tree/main/examples) for real tool implementations
- **Off-ramp:** if writing tools feels clunky compared to alternatives, note why — that's a real signal, not a reason to push through out of sluggishness.
  - **Explore instead:** [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (graph-based control flow, huge tool ecosystem) or [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) (role-based multi-agent framework with a large built-in toolkit).

## Stage 3 — Multi-agent / orchestration (~1–2 hrs)
- Try a manager agent delegating to a sub-agent (`managed_agents`).
- Look at planning steps, memory/step logs, and `agent.logs` for debuggability.
- **Resources:** [Multi-agent systems docs](https://huggingface.co/docs/smolagents/examples/multiagent_web_browser), [smolagents `examples/multiple_tools_and_agent`](https://github.com/huggingface/smolagents/tree/main/examples)
- **Off-ramp:** if you don't have a use case that needs multi-agent delegation, skip this — it's the most complex part of the library and often unnecessary for single-purpose agents.
  - **Explore instead (only if orchestration itself is the interest):** [microsoft/autogen](https://github.com/microsoft/autogen) or [langgraph's multi-agent patterns](https://github.com/langchain-ai/langgraph) — both go deeper on orchestration than smolagents does.

## Stage 4 — Sandbox & safety (~30–60 min)
- Understand how code execution is sandboxed (local Python exec vs Docker/E2B remote executors).
- Decide what's acceptable for your deployment target.
- **Resources:** [Secure code execution docs](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution), [E2B](https://github.com/e2b-dev/e2b) (remote sandbox smolagents can plug into)
- **Off-ramp:** if you need strong sandboxing guarantees smolagents doesn't give out of the box, this is a hard blocker for production use — evaluate before investing further.
  - **Explore instead:** [e2b-dev/e2b](https://github.com/e2b-dev/e2b) or [modal-labs/modal-client](https://github.com/modal-labs/modal-client) directly, and consider a bespoke sandboxed function-calling loop rather than a full agent framework.

## Stage 5 — Build a real small project (~half day)
- Pick one concrete task (e.g. a research assistant, a data-wrangling agent) and build it end-to-end with proper tools, error handling, and a couple of test prompts.
- This is the actual validation step: does smolagents make *this* easier than writing a bespoke loop?
- **Resources:** [Open Deep Research](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research) (HF's own full-scale example built on smolagents; a good template to crib from) and its writeup, [Open-source DeepResearch – Freeing our search agents](https://huggingface.co/blog/open-deep-research)

## Exit criteria
- **Keep using smolagents** if Stage 5's project came together faster/cleaner than expected.
- **Drop it** if you hit repeated friction in Stage 1–2 (paradigm mismatch) or Stage 4 (sandboxing) — better to find out cheaply than after a real build. Use the "explore instead" repos above as the next stop.
