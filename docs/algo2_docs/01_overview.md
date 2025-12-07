# 01_overview.md

# Overview — Algo2 for MindMeetingAI (English)

## Purpose
Algo2 defines the end-to-end conversational logic and retrieval-augmented generation (RAG) pipeline that powers MindMeetingAI's chatbot and meeting summarization services. It documents goals, success criteria, assumptions, constraints, and a high-level flow that parties (developers, testers, evaluators) can follow.

## High-level goals
- Robust multi-turn dialogue management with slot-aware tasks.
- Accurate retrieval from internal meeting corpora using semantic embeddings.
- Safe and concise generation of answers and meeting summaries.
- Easy-to-deploy modules with clear interfaces for embeddings, vector store, and LLM.

## Success criteria
- Intent classification F1 ≥ 90% on defined intents.
- Retrieval precision@5 ≥ 80% for meeting Q&A queries.
- End-to-end average latency ≤ 800ms (local infra / acceptable for demo).
- Human evaluator satisfaction score ≥ 4/5 on generated summaries and answers.

---

# Tổng quan — Algo2 cho MindMeetingAI (Tiếng Việt)

## Mục tiêu
Algo2 định nghĩa luồng hội thoại end-to-end và pipeline RAG dùng cho chatbot và chức năng tóm tắt họp của MindMeetingAI. Tài liệu nêu rõ mục tiêu, tiêu chí thành công, giả định và giới hạn, kèm flow để dev/test/giảng viên dễ hiểu.

## Mục tiêu chính
- Quản lý đa lượt hội thoại với hỗ trợ slot (slot filling) cho các nhiệm vụ đa bước.
- Truy xuất chính xác từ kho tư liệu nội bộ bằng embeddings.
- Sinh phản hồi và tóm tắt ngắn gọn, an toàn.
- Mô-đun dễ triển khai, interface rõ ràng cho embeddings, vector store, LLM.

## Tiêu chí thành công
- Intent classifier F1 ≥ 90% (trên tập intent đã định nghĩa).
- Retrieval precision@5 ≥ 80% với các truy vấn Q&A về cuộc họp.
- Latency end-to-end ≤ 800ms (trạng thái demo/local).
- Độ hài lòng (human evaluator) ≥ 4/5 cho tóm tắt và câu trả lời.
