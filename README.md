# # **MindMeetingAI – Intelligent Meeting Assistant**
---

## ## **1. Overview**

MindMeetingAI is an AI-powered assistant designed to support meeting workflows by providing:

* Automatic meeting summarization
* Key topic extraction
* Action-item recommendations
* A chatbot interface with RAG (Retrieval-Augmented Generation)
* FastAPI backend for API services
* Embedding-based search for internal knowledge

---

## ## **2. Features**

* **FastAPI backend** with modular architecture
* **RAG pipeline** using FAISS or Chroma
* **Sentence-Transformers embeddings**
* **LLM integration** (OpenAI / Groq / others)
* Simple, maintainable structure suitable for academic or production environments

---

## ## **3. Installation**

### Create environment

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate # macOS / Linux
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ## **4. Running the Server**

```bash
uvicorn app.main:app --reload
```

API Documentation will be available at:

```
http://localhost:8000/docs
```

---

## ## **5. Environment Variables**

Create a `.env` file:

```
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## ## **6. Project Structure**

```
app/
 ├── main.py
 ├── api/
 ├── services/
 │     ├── rag_service.py
 │     ├── embedder.py
 │     ├── vector_store.py
 ├── models/
 ├── core/
```

---

## ## **7. Team Roles**

The project is developed collaboratively under a formal team agreement.
Responsibilities include Project Management, AI Design, Backend Development, Testing, and UX/UI.

---

## ## **8. License**

This project is licensed under the MIT License.

---

<br><br>

---

# # **MindMeetingAI – Trợ lý họp thông minh**

*Phiên bản tiếng Việt cho báo cáo và tài liệu học thuật.*

---

## ## **1. Giới thiệu**

MindMeetingAI là hệ thống AI hỗ trợ quá trình họp, bao gồm:

* Tự động tóm tắt nội dung
* Trích xuất chủ đề quan trọng
* Gợi ý hành động sau cuộc họp
* Chatbot dùng RAG để truy vấn kiến thức nội bộ
* Backend được xây dựng bằng FastAPI
* Tìm kiếm dựa trên embeddings để tăng độ chính xác

---

## ## **2. Tính năng**

* Backend FastAPI dễ mở rộng, chuyên nghiệp
* Pipeline RAG dùng FAISS hoặc Chroma
* Embeddings từ Sentence-Transformers
* Tích hợp LLM (OpenAI / Groq)
* Kiến trúc sạch, phù hợp triển khai thực tế hoặc nộp đồ án

---

## ## **3. Cài đặt**

### Tạo môi trường ảo

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# hoặc
source .venv/bin/activate # macOS / Linux
```

### Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## ## **4. Chạy server**

```bash
uvicorn app.main:app --reload
```

Truy cập tài liệu API:

```
http://localhost:8000/docs
```

---

## ## **5. Cấu hình môi trường**

Tạo file `.env`:

```
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## ## **6. Cấu trúc dự án**

```
app/
 ├── main.py
 ├── api/
 ├── services/
 ├── models/
 ├── core/
```

---

## ## **7. Vai trò nhóm**

Dự án được xây dựng theo hợp đồng nhóm, bao gồm:
Project Manager, AI Engineer, Backend Dev, Tester, Frontend Dev.
Trách nhiệm được phân chia rõ ràng, chuyên nghiệp theo tiêu chuẩn quốc tế.

---

## ## **8. Giấy phép**

Dự án sử dụng giấy phép MIT.

---

# ✨ Hoàn tất!

README này đáp ứng:
✔ Chuẩn quốc tế
✔ Song ngữ Anh – Việt
✔ Ngắn gọn, chuyên nghiệp
✔ Phù hợp Academic + Industry
✔ Dễ dùng cho GitHub & báo cáo

---

Phong muốn chị tiếp tục bước nào tiếp theo?

1️⃣ **Tạo cấu trúc backend FastAPI trong repo**
2️⃣ **Tạo branch feature/algo2 và viết thuật toán đầy đủ**
3️⃣ **Viết flowchart Mermaid**
4️⃣ **Viết pseudocode chuẩn Algo 2**

Chị làm tiếp ngay khi em chọn.
