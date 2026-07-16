# Learning smolagents — mini plan

Goal: understand smolagents well enough to build and ship a small real agent, without over-investing if it turns out to be the wrong tool.

*Links below were checked live on 2026-07-16 (repo at v1.26.0, ~27.8k stars).*

## Stage 0 — Baseline (done)
- Minimal `CodeAgent` + `DuckDuckGoSearchTool` + `InferenceClientModel` running (`main.py`).
- **Resources:**
  - [huggingface/smolagents](https://github.com/huggingface/smolagents) — README quickstart
  - [Docs index](https://huggingface.co/docs/smolagents/en/index)
- **Off-ramp:** if this doesn't run cleanly (auth/model access issues), stop here and fix environment before going further — no point building on a broken base.

## Stage 1 — Core concepts (~1–2 hrs)
- Read up on `CodeAgent` vs `ToolCallingAgent` — smolagents' signature idea is agents that write Python code to call tools (composable via loops/conditionals) instead of emitting JSON tool calls, which `ToolCallingAgent` still supports for when that's preferred.
- Understand the run loop: think → write code → execute in sandbox → observe → repeat until `final_answer`.
- Try swapping the model (local `transformers`/`ollama`, a Hub inference provider, or OpenAI/Anthropic via the LiteLLM integration) to see how model-agnostic the abstraction is.
- **Resources:**
  - Blog: [Introducing smolagents: simple agents that write actions in code](https://huggingface.co/blog/smolagents)
  - Docs: [Guided tour](https://huggingface.co/docs/smolagents/en/guided_tour)
  - Free course: [HF Agents Course, Unit 2 — smolagents](https://huggingface.co/learn/agents-course/en/unit2/smolagents/introduction) (~3–4 hrs, has a certificate track)
  - Video course: [DeepLearning.AI — Building Code Agents with Hugging Face smolagents](https://www.deeplearning.ai/courses/building-code-agents-with-hugging-face-smolagents)
  - Background research: [Executable Code Actions Elicit Better LLM Agents (CodeAct), arXiv 2402.01030](https://arxiv.org/abs/2402.01030) — the paper smolagents' "code agent" design is built on
- **Off-ramp:** if the code-writing-agent paradigm feels like the wrong fit for your use case (e.g. you need strict structured/validated output, not free-form code execution), this is the point to reconsider — that's smolagents' core differentiator, and everything else builds on it.
  - **Explore instead:** [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (type-safe, validated structured output; same validation layer used by several other agent SDKs) or [openai/openai-agents-python](https://github.com/openai/openai-agents-python) (minimal classic tool-calling/handoff loop, no code-exec).

## Stage 2 — Tools (~1–2 hrs)
- Build one custom tool with the `@tool` decorator (name + type hints + docstring `Args:` section — the LLM reads these directly) and one with a `Tool` subclass for a case needing extra state/methods.
- Give the agent 2–3 tools and watch how it plans/chains calls across steps.
- **Resources:**
  - [Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools)
  - [smolagents `examples/`](https://github.com/huggingface/smolagents/tree/main/examples) — real tool implementations to crib from
- **Off-ramp:** if writing tools feels clunky compared to alternatives, note *why* — that's a real signal, not a reason to push through out of sluggishness.
  - **Explore instead:** [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (graph-based control flow, checkpointing, huge tool ecosystem — pick this if you want deterministic, auditable state transitions) or [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) (52k+ stars, role-based multi-agent framework with a large built-in toolkit and the fastest idea-to-prototype path).

## Stage 3 — Multi-agent / orchestration (~1–2 hrs)
- Build a manager agent with 1–2 sub-agents passed via `managed_agents` — from the manager's perspective, calling a sub-agent looks just like calling any other tool.
- Look at planning steps, memory/step logs, and agent run logs for debuggability.
- **Resources:**
  - [Orchestrate a multi-agent system](https://huggingface.co/docs/smolagents/en/examples/multiagents)
  - [HF Agents Course — Multi-Agent Systems](https://huggingface.co/learn/agents-course/en/unit2/smolagents/multi_agent_systems)
- **Off-ramp:** if you don't have a use case that needs multi-agent delegation, skip this — it's the most complex part of the library and often unnecessary for single-purpose agents.
  - **Explore instead (only if orchestration itself is the interest):** [microsoft/autogen](https://github.com/microsoft/autogen) or LangGraph's multi-agent patterns — both go deeper on orchestration primitives than smolagents does.

## Stage 4 — Sandbox & safety (~30–60 min)
- Understand execution options: the default `LocalPythonExecutor` is **not** a security boundary and can be bypassed — it's fine for local experimentation only.
- For anything untrusted/production, use a remote sandbox via `executor_type="e2b"`, `"docker"`, `"modal"`, or `"blaxel"`.
- Decide what's acceptable for your deployment target.
- **Resources:**
  - [Secure code execution](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution)
  - [e2b-dev/E2B](https://github.com/e2b-dev/E2B) — one of the sandbox backends smolagents plugs into directly
- **Off-ramp:** if you need strong sandboxing guarantees smolagents doesn't give out of the box, this is a hard blocker for production use — evaluate before investing further.
  - **Explore instead:** [e2b-dev/E2B](https://github.com/e2b-dev/E2B) directly, or a bespoke sandboxed function-calling loop rather than a full agent framework.

## Stage 5 — Build a real small project (~half day)
- Pick one concrete task (e.g. a research assistant, a data-wrangling agent) and build it end-to-end with proper tools, error handling, and a couple of test prompts.
- This is the actual validation step: does smolagents make *this* easier than writing a bespoke loop?
- **Resources:**
  - [Open Deep Research](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research) — HF's full-scale open replication of OpenAI's Deep Research, built on smolagents (55% pass@1 on GAIA validation); a strong template to crib from
  - Blog: [Open-source DeepResearch – Freeing our search agents](https://huggingface.co/blog/open-deep-research)

## Exit criteria
- **Keep using smolagents** if Stage 5's project came together faster/cleaner than expected.
- **Drop it** if you hit repeated friction in Stage 1–2 (paradigm mismatch) or Stage 4 (sandboxing) — better to find out cheaply than after a real build. Use the "explore instead" repos above as the next stop.
