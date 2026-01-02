from gtts import gTTS
from pathlib import Path

# Nội dung cuộc họp (tiếng Việt)
MEETING_TEXT = """
Xin chào mọi người, chúng ta bắt đầu cuộc họp hôm nay.
Nội dung chính gồm ba phần: tiến độ dự án, các vấn đề tồn đọng và kế hoạch tuần tới.
Anh A phụ trách backend, chị B phụ trách frontend.
Hạn demo là cuối tuần.
Cảm ơn mọi người đã tham gia.
"""

# Thư mục output
output_dir = Path("data/audio")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "meeting_test.mp3"

tts = gTTS(text=MEETING_TEXT, lang="vi")
tts.save(output_file)

print(f"✅ Test audio generated at: {output_file}")
