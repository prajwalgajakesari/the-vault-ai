On September 5, the SGLang project shipped v0.5.19: 786 pull requests from 214 contributors, beam search, a new DeepEP engine, ROCm 10 images. Six days later, VicOne researcher Reuel Magistrado published the details of an unauthenticated remote code execution bug he had reported to the maintainers on July 2 — and that they had acknowledged, and then not fixed. Nothing in the v0.5.19 highlights addresses it. As of disclosure, there is still no patch.

CVE-2026-86793, published September 11, bypasses SGLang's SafeUnpickler: the guard rail the project built specifically to stop this class of attack. It affects SGLang through 0.5.18, is classified CWE-94, and carries no CVSS score — NVD analysis is still pending, a small indictment of how fast the paperwork moves relative to the code.

It is the fourth critical CVE to hit AI inference and agent infrastructure in a very short window. Eighteen days, precisely, from August 25 to September 11.

## The allowlist that allowed everything

SGLang, the LMSYS-developed serving framework used across research labs and production GPU clusters, exposes an HTTP endpoint called `/update_weights_from_tensor` for hot-swapping model weights. It accepts pickled Python objects. That was already a problem once: CVE-2025-10164 covered the same endpoint, and the fix was SafeUnpickler, which restricts which modules a pickle stream may resolve.

SafeUnpickler works off two lists — `ALLOWED_MODULE_PREFIXES` and `DENY_CLASSES`. The allowlist includes the prefix `builtins.`, which permits any name in Python's builtins module unless the denylist explicitly blocks it. The denylist blocks the obvious ones: `eval`, `exec`, `compile`, `open`. It does not block `__import__` or `getattr`.

That gap is the whole vulnerability. An attacker need not reach a forbidden function directly; they need only reach two permitted ones and let those fetch the rest. Because SafeUnpickler inspects only the module and name handed to `find_class()`, it never observes the dangerous pair being assembled at runtime. The restrictions are bypassed not by breaking the rules but by staying within them.

The endpoint is marked `AuthLevel.ADMIN_OPTIONAL`. When no API key is configured — the default for a great many internal deployments — it accepts requests from anyone who can reach the port. Network access is the entire prerequisite.

"Secure deserialization cannot rely only on blocking known dangerous functions," Magistrado's research concluded. Unglamorous, and correct.

## This has happened to SGLang before. Repeatedly.

The uncomfortable detail is that CVE-2026-86793 is not even the first SafeUnpickler denylist bypass disclosed this year. On July 30, CERT/CC published VU#281278, documenting six SGLang vulnerabilities reported by researcher Apoorv Dayal. The first, CVE-2026-15969, is unauthenticated RCE in `/load_lora_adapter_from_tensors` — via, in CERT/CC's words, "bypass of SafeUnpickler's incomplete denylist." Same guard rail, different endpoint, six weeks earlier. The note's summary line: "no patches are available from the project maintainers, and coordination attempts have been unsuccessful."

Before that, in March, CERT/CC published VU#665416 on three more pickle bugs found by Orca Security's Igor Stepansky and CERT/CC's Christopher Cullen — two of them CVSS 9.8, both unauthenticated network RCE through ZeroMQ brokers bound to `tcp://*`. Orca's timeline runs February 4 to March 11 and records no vendor response at any point, including after CERT/CC escalated to CISA. Cullen wrote a patch himself — localhost binding plus msgpack — and filed it as GHSA-wxjp-55q2-vg27. It was not merged.

Counting this week's disclosure, SGLang has accumulated at least a dozen CVEs in 2026. Orca's audit found more than 20 unsafe deserialization calls still in the codebase.

## Why pickle keeps eating ML infrastructure

Python's own documentation has warned for years that pickle is not secure against maliciously constructed data. The reason is structural: a pickle stream does not encode data, it encodes instructions for rebuilding objects, and the `__reduce__` protocol lets those instructions name any callable at all. Stepansky's formulation is the one worth memorizing: "every `pickle.loads()` call on untrusted input is an implicit `eval()`."

He also names why the industry cannot quit it. "Unsafe pickle deserialization is arguably the most prevalent vulnerability class in the Python AI/ML ecosystem," he wrote. "The reason is understandable: pickle is convenient. It serializes arbitrary Python objects with zero schema definition." Msgpack and Protocol Buffers require you to define what you are sending; pickle does not. For a framework optimizing tokens per second across 214 contributors, schema discipline is friction, and friction loses.

CERT/CC's guidance in VU#665416 is blunter than most vendor advisories get: "It is recommended that project maintainers avoid implementing Pickle functions due to the inherent security risks."

SafeUnpickler is what happens when a project declines that advice and tries to make pickle safe instead. Allowlists over a language with runtime reflection are a losing proposition — you are enumerating badness in a system explicitly designed to let you reach anything from anywhere.

## The default-open problem

The other three CVEs in the eighteen-day cluster share a shape. NemoClaw (CVE-2026-65105, CVSS 8.1), disclosed August 25 by Oasis Security and Cyera, exploited an Ollama backend bound to all interfaces with Host header validation off: "A single visit to an attacker-controlled webpage is all it takes to give the attacker these capabilities." DeepSeek Harness (CVE-2026-82533, CVSS 9.4) exposed an unauthenticated local API that let a sandboxed agent disable its own confinement — OX Security reported the escalation to `danger-full-access` took one command "on the shipped default configuration." IBM Langflow (CVE-2026-81204, CVSS 9.8) passed return-type annotation source to `eval` past an incomplete denylist.

Incomplete denylists, unauthenticated control planes, permissive default bindings. These are not novel attacks. They are 2005 attacks, shipped inside frameworks written in 2025.

## What to watch

Whether SGLang merges anything. There are now four CERT/CC notes against the project and at least two externally written patches sitting unmerged; "no vendor statement" has appeared in three consecutive advisories. Watch for `SGLANG_USE_PICKLE_IPC` flipping to `false` by default, and for `AuthLevel.ADMIN_OPTIONAL` becoming mandatory — either would signal a posture change. Until then the practical control is segmentation: treat every inference control endpoint as internet-facing until proven otherwise, and audit which GPU nodes currently accept a weight update from anyone who can route to port 30000.
