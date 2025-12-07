# Data Flow & Schemas — Algo2 (English)

## Overview

This file defines the data movement and JSON schemas used between modules. It clarifies which fields are required for integration and testing.

## Key entities

* Session: { "session_id": str, "history": [Turn], "slots": {name:value}, "user_profile": {...} }
* Turn: { "speaker": "user"|"system", "text": str, "timestamp": iso8601, "meta": {} }
* EmbedRequest: { "text": str }
* EmbedResponse: { "embedding": [float], "model": str }
* SearchRequest: { "embedding": [float], "top_k": int }
* SearchResponse: { "docs": [ { "id": str, "text": str, "score": float } ] }
* LLMRequest: { "system_prompt": str, "user_prompt": str, "context_docs": [str], "max_tokens": int }
* LLMResponse: { "text": str, "references": [ { "doc_id": str, "span": str } ] }

## Example Turn JSON

```
{
  "session_id": "sess_abc123",
  "turn": {
    "speaker": "user",
    "text": "Summarize last meeting about project scope",
    "timestamp": "2025-12-06T09:21:34Z",
    "meta": { "source": "web" }
  }
}
```

## Flow (short)

1. Ingestion converts input → Turn JSON.
2. NLU annotates → produces intent + entities.
3. If retrieval needed → Embedder.encode(query) → VectorDB.search → returns docs.
4. LLMRequest built with system prompt + docs → LLMResponse.
5. Postprocess → Output JSON with `text` + `references`.

---

# Dòng dữ liệu & Schema — Algo2 (Tiếng Việt)

## Tổng quan

Định nghĩa các schema JSON giữa các module để dev/test dễ tích hợp.

## Các thực thể chính

* Session: { "session_id": str, "history": [Turn], "slots": {...} }
* Turn: { "speaker": "user"|"system", "text": str, "timestamp": iso8601, "meta": {} }
* EmbedRequest/Response...
* SearchRequest/Response...
* LLMRequest/Response...

## Ví dụ Turn JSON (Tiếng Việt)

```
{
  "session_id": "sess_abc123",
  "turn": {
    "speaker": "user",
    "text": "Tóm tắt cuộc họp trước về phạm vi dự án",
    "timestamp": "2025-12-06T09:21:34Z",
    "meta": { "source": "web" }
  }
}
```

## Luồng ngắn

1. Ingestion → Turn JSON
2. NLU → intent + entities
3. Nếu cần truy xuất → Embedder.encode → VectorDB.search → docs
4. Gọi LLM với context → nhận LLMResponse
5. Postprocess → trả Output JSON gồm `text` và `references`

```


