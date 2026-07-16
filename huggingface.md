# Hugging Face & smolagents

## What is Hugging Face?

Hugging Face is an AI company and open-source platform best known for the **Hub** — a central repository (like GitHub, but for ML) hosting hundreds of thousands of pre-trained **models**, **datasets**, and **Spaces** (hosted demo apps). It started with the `transformers` library for NLP and has since expanded into a broad ecosystem: `datasets`, `diffusers` (image/audio generation), `accelerate` (distributed training), `peft` (fine-tuning), `tokenizers`, and — most relevant here — **`smolagents`**, a lightweight library for building AI agents.

The Hub also provides:
- **Inference Providers** — hosted APIs to run models (including as a `Model` backend for smolagents).
- **`huggingface_hub`** — the Python client for pushing/pulling models, datasets, and Spaces.
- Free hosting for demos via **Spaces** (Gradio/Streamlit apps), useful for showcasing an agent you build.

## What is smolagents?

`smolagents` is Hugging Face's minimal, "barebones" agent framework (~1,000 lines of core logic). Its defining idea: **agents write their actions as Python code** rather than JSON tool calls (a `CodeAgent`), which tends to make multi-step tool orchestration more reliable and composable (loops, conditionals, function nesting come for free). It also offers a `ToolCallingAgent` for classic JSON-based tool calling.

Key properties:
- **Model-agnostic** — works with local `transformers`/`ollama` models, Hugging Face Inference Providers, or OpenAI/Anthropic/etc. via LiteLLM.
- **Tool-agnostic** — plug in your own Python functions as tools, or pull tools from the Hub / MCP servers / LangChain.
- **Sandboxed code execution** — supports safer code execution backends (E2B, Docker, local) since the agent is literally executing generated Python.
- **Minimal surface area** — designed to be read and understood in one sitting, unlike heavier frameworks.

### Quick start

```bash
pip install 'smolagents[toolkit]'
```

```python
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel()  # uses HF Inference Providers by default
agent = CodeAgent(tools=[], model=model)
agent.run("What is the 118th number in the Fibonacci sequence?")
```

## Official documentation

- [smolagents docs (index)](https://huggingface.co/docs/smolagents/index) — main documentation hub
- [Guided tour](https://huggingface.co/docs/smolagents/en/guided_tour) — walkthrough of core concepts after installation
- [Agents API reference](https://huggingface.co/docs/smolagents/reference/agents) — `CodeAgent`, `ToolCallingAgent`, etc.
- [GitHub repo](https://github.com/huggingface/smolagents) — source code, issues, examples folder
- [smolagents.org](https://smolagents.org/) — companion docs/examples site

## Official blog & course

- [Introducing smolagents: simple agents that write actions in code](https://huggingface.co/blog/smolagents) — the original launch post, explains the "code agents" philosophy and design rationale
- [Hugging Face Agents Course – Unit 2: Introduction to smolagents](https://huggingface.co/learn/agents-course/unit2/smolagents/introduction)
- [Agents Course – Let's Create Our First Agent Using smolagents](https://huggingface.co/learn/agents-course/en/unit1/tutorial) — hands-on first-agent tutorial

## Third-party tutorials & blogs

- [DataCamp — Hugging Face's Smolagents: A Guide With Examples](https://www.datacamp.com/tutorial/smolagents) — builds an agent that fetches the top-upvoted paper from HF Daily Papers, custom tools walkthrough
- [Analytics Vidhya — SmolAgents by Hugging Face: Build AI Agents in Less than 30 Lines](https://www.analyticsvidhya.com/blog/2025/01/smolagents/)
- [Cohorte Engineering — Unpacking SmolAgents: A Beginner-Friendly Guide to Agentic Systems](https://cohorte.co/blog/unpacking-smolagents-a-beginner-friendly-guide-to-agentic-systems) — simple Fibonacci `CodeAgent` example
- [Medium (Ali Khalaji) — Getting Started with Hugging Face Smolagents](https://medium.com/@alikhalaji/getting-started-with-hugging-face-smolagents-ce8bee9e2d61)
- [Medium (Anoop Maurya) — Introduction to Smolagents: A Hugging Face Agentic Framework](https://medium.com/@mauryaanoop3/introduction-to-smolagents-a-hugging-face-agentic-framework-190169b424f4)
- [Medium (DhanushKumar) — Exploring SmolAgents: Building Intelligent Agents with Hugging Face](https://medium.com/@danushidk507/exploring-smolagents-building-intelligent-agents-with-hugging-face-983969ec99a9)
- [samwit/smolagents_examples (GitHub)](https://github.com/samwit/smolagents_examples) — example code from a video tutorial series, including multi-agent setups

## Suggested reading order

1. Official launch blog post (concept/motivation)
2. Guided tour (core API)
3. Agents Course Unit 1 tutorial (hands-on first agent)
4. DataCamp or Cohorte tutorial (a full worked example)
5. Agents API reference (as you need specifics)
