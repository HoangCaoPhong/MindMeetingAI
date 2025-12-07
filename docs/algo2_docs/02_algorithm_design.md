# 02_algorithm_design.md

# Algorithm Design — Algo2 (English)

## 1. Problem definition
Design a conversational AI that:
- Accepts user utterances (text/ASR).
- Detects intent and entities.
- If factual or document-based, retrieves context via embeddings+vector DB.
- Uses retrieved context + dialogue state to generate safe responses via LLM.
- Handles multi-turn tasks (slot filling), clarifications, and handovers.

## 2. High-level components
1. Ingestion
   - Text normalization, optional ASR (for voice).
2. NLU
   - Intent classifier + NER + slot filler.
3. Dialogue Manager (DM)
   - Maintains session state, policy engine (rules + ML fallback).
4. Retrieval (Vector DB)
   - Embed queries, nearest-neighbor search, candidate scoring.
5. Generator (NLG)
   - LLM prompt that conditions on retrieved context + system instructions.
6. Safety & Postprocessing
   - Filters, de-duplication, personalization tokens.
7. Logging & Feedback
   - Turn logs, confidence scores, human-in-the-loop metric collection.

## 3. Key algorithms & choices
- Embeddings: sentence-transformers/all-MiniLM-L6-v2 for small footprint / or larger models if infra allows.
- Vector store: FAISS for local demo, Chroma/Pinecone for managed hosting.
- Intent classification: DistilBERT (fine-tuned) or logistic-regression baseline + regex fallback.
- Dialogue policy: Rule-first policy (clarify if low confidence) with optional RL/ML policy later.
- Reranking: BM25 or cross-encoder re-ranker (if compute allowed) for top-K refinement.

## 4. Session & state model
- Session ID → conversation history (list of turns), slots map, last_action, user_profile (optional).
- Slot schema per intent: required/optional/defaults.
- State transitions: IDLE → ACTIVE TASK → WAIT_SLOT → API_CALL → COMPLETED/HANDOVER.

## 5. Failure modes & mitigations
- Low intent confidence → ask clarification.
- No good retrieval → fallback to "I don't know" + offer search/upload doc.
- Hallucination risk → cite retrieved passages or abstain.
- Sensitive data leakage → redact PII pre/post.

---

# Thiết kế Thuật toán — Algo2 (Tiếng Việt)

## 1. Định nghĩa bài toán
Thiết kế chatbot:
- Nhận input text/voice.
- Xác định intent và entity.
- Nếu câu hỏi cần tư liệu, truy xuất ngữ cảnh bằng embeddings + vector DB.
- Dùng context + state để tạo câu trả lời an toàn bằng LLM.
- Hỗ trợ multi-turn, slot filling, hỏi làm rõ và chuyển human khi cần.

## 2. Các thành phần chính
1. Ingestion: chuẩn hoá text, ASR nếu voice.
2. NLU: intent classifier + NER + slot filler.
3. Dialogue Manager: quản lý state, policy (quy tắc + ML).
4. Retrieval: encode query, tìm nearest neighbors.
5. Generator: prompt LLM với context.
6. Safety & Postprocess: lọc, loại trùng, cá nhân hoá.
7. Logging & Feedback: lưu turn, score, thu thập feedback.

## 3. Lựa chọn thuật toán chính
- Embeddings: all-MiniLM-L6-v2 (light) — nâng cấp nếu có infra.
- Vector store: FAISS (local), Chroma/Pinecone (managed).
- Intent: DistilBERT fine-tune hoặc baseline logistic + regex.
- Policy: Rule-first (hỏi khi low-confidence), mở rộng ML policy.
- Reranking: cross-encoder nếu có tài nguyên.

## 4. Mô hình Session & State
- Session ID → history, slots, last_action, user_profile.
- Slot schema: required/optional/default.
- Trạng thái: IDLE → ACTIVE → WAIT_SLOT → CALL_API → COMPLETED/HANDOVER.

## 5. Rủi ro & giảm thiểu
- Low confidence → hỏi làm rõ.
- No retrieval hit → trả lời thành thật và offer upload.
- Hallucination → trích dẫn passages hoặc abstain.
- PII → redact trước/sau.
