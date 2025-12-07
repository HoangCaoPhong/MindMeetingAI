````
# 04_flowchart_mermaid.md

# Flowcharts (Mermaid) — Algo2 (English)

## Main pipeline (simple)
```mermaid
flowchart LR
  U[User Input\n(text / voice)] --> Ingest[Ingestion\n(ASR if voice)]
  Ingest --> NLU[NLU\nNormalization → Intent → Entities → Slots]
  NLU --> DM[Dialogue Manager\n(State + Policy)]
  DM -->|ASK_CLARIFY| Clarify[Ask Clarifying Q]
  Clarify --> U
  DM -->|CALL_API| API[Call External API / Action]
  API --> NLG1[NLG / Template]
  DM -->|RETRIEVE| RAG[RAG: VectorDB → TopK → LLM]
  RAG --> NLG2[NLG / LLM Synthesis]
  DM -->|SMALL_TALK| ST[SmallTalk Module]
  ST --> NLG3[NLG / Template]
  NLG1 --> Post[Post-process\nFilter & Personalize]
  NLG2 --> Post
  NLG3 --> Post
  Post --> Output[Send Response to User]
  Output --> Session[Update Session State & Log]
  Session --> DM
````

## Retrieval detail (Mermaid)

```mermaid
flowchart TD
  Q[User Query] --> E[Embedder\n(sentence-transformers)]
  E --> V[VectorDB Search\n(FAISS / Chroma)]
  V --> R[Top-K Candidates]
  R --> RC[Optional Re-ranker\n(cross-encoder)]
  RC --> LLM[LLM Prompt + Synthesis]
  LLM --> RESP[Final Response]
```

