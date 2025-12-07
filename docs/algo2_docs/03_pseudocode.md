# 03_pseudocode.md

# Pseudocode — Algo2 (English)

## Notation
- session := session store object
- text := raw user text
- intent, score := output of IntentClassifier.predict(text)
- entities := NER.extract(text)
- slots := session.slots
- top_docs := retrieved docs list

### Main turn handler
function handle_turn(session_id, raw_input, input_type):
# 1. Ingestion
if input_type == "voice":
text = ASR.transcribe(raw_input)
else:
text = normalize(raw_input)

# 2. NLU
intent, score = IntentClassifier.predict(text)
entities = NER.extract(text)
slots = SlotFiller.fill(session_id, entities)

# 3. Dialogue Manager Decision
state = SessionStore.get(session_id)
action = DialoguePolicy.decide(state, intent, score, slots)

if action == "ASK_CLARIFY":
    reply = TemplateEngine.render("clarify", slots.missing)
    SessionStore.update(session_id, last_action="ASK_CLARIFY")
    return reply

if action == "CALL_API":
    api_result = ExternalAPI.call(intent, slots)
    SessionStore.update(session_id, last_action="CALL_API")
    reply = NLG.generate_from_template(intent, api_result)
    Logger.log_turn(...)
    return reply

if action == "RETRIEVE_AND_ANSWER":
    query = build_query(text, state.context)
    emb = Embedder.encode(query)
    top_docs = VectorDB.search(emb, top_k=K)
    if top_docs.score_mean < RETRIEVAL_THRESHOLD:
        return TemplateEngine.render("no_relevant_docs")
    answer = LLM.synthesize(query, top_docs, system_prompt=SYS_PROMPT)
    reply = PostProcess(answer)
    SessionStore.update(session_id, last_action="RETRIEVE_AND_ANSWER")
    Logger.log_turn(...)
    return reply

if action == "SMALL_TALK":
    reply = SmallTalkModule.respond(text)
    return reply

if action == "HANDOVER":
    notify_human_agent(session_id, text)
    return TemplateEngine.render("handover_ack")


## Supporting functions


function DialoguePolicy.decide(state, intent, score, slots):
if score < INTENT_THRESHOLD:
return "ASK_CLARIFY"
if intent in ["qa", "policy_query", "doc_query"]:
if requires_slots(intent) and slots.missing:
return "ASK_CLARIFY"
else:
return "RETRIEVE_AND_ANSWER"
if intent in small_talk_list:
return "SMALL_TALK"
return "RETRIEVE_AND_ANSWER"


# Pseudocode — Algo2 (Tiếng Việt)

### Notation tương tự (session, text, intent, entities, slots)

### Xử lý 1 lượt hội thoại


hàm handle_turn(session_id, raw_input, input_type):
nếu input_type là voice:
text = ASR.transcribe(raw_input)
khác:
text = normalize(raw_input)

intent, score = IntentClassifier.predict(text)
entities = NER.extract(text)
slots = SlotFiller.fill(session_id, entities)

state = SessionStore.get(session_id)
action = DialoguePolicy.decide(state, intent, score, slots)

nếu action == "ASK_CLARIFY":
    trả về câu hỏi làm rõ

nếu action == "CALL_API":
    gọi API ngoài, cập nhật state, trả về template

nếu action == "RETRIEVE_AND_ANSWER":
    build query, emb = Embedder.encode(query)
    top_docs = VectorDB.search(emb, top_k=K)
    nếu không có doc phù hợp:
        trả về "không tìm thấy thông tin"
    answer = LLM.synthesize(query, top_docs)
    postprocess và trả về

nếu action == "SMALL_TALK":
    trả về SmallTalkModule.respond(text)

nếu action == "HANDOVER":
    notify human và trả về ack
