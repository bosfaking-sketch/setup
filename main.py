import datetime
import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101! - [{now}]")
