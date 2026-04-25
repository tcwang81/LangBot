import sys
import os

# 1. 確保 Vercel 能找到 src 資料夾裡的程式碼
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import langbot.__main__

# 2. 執行原本的初始化 (讀取設定檔等)
# 注意：在 Vercel 環境下，有些初始化可能會失敗，這裡我們先照原廠邏輯走
try:
    langbot.__main__.main()
except Exception as e:
    print(f"Init warning: {e}")

# 3. 關鍵：暴露出的 app 物件供 Vercel 呼叫
# 根據 LangBot 的 FastAPI 慣例，我們從實例中抓取 app
from langbot.core.app import app
