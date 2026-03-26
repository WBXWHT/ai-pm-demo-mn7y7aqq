#!/usr/bin/env python3
"""
AI产品助手 Demo
我曾主导“AI智能职位匹配助手”项目，旨在提升求职平台的匹配效率。我们基于用户历史行为与简历，利用大模型构建了动态岗位推荐模型，并设计了交互式问答界面引导用户细化需求。上线后，核心用户的平均投递转化率提升了18%，页面停留时长增加了25%。
"""
import json
from datetime import datetime

class AIProductAssistant:
    def __init__(self):
        self.queries = 0
        self.start_time = datetime.now().isoformat()

    def analyze_intent(self, text):
        keywords = {"分析": "analyze", "推荐": "recommend", "查询": "query", "帮我": "assist"}
        for kw, intent in keywords.items():
            if kw in text:
                return {"intent": intent, "confidence": 0.88}
        return {"intent": "general", "confidence": 0.75}

    def respond(self, user_input):
        self.queries += 1
        result = self.analyze_intent(user_input)
        return f"[{result['intent']}] 已处理：{user_input}"

def main():
    print("=== AI产品助手 Demo ===")
    bot = AIProductAssistant()
    demos = ["帮我分析用户增长数据", "推荐AI功能方向", "查询本月活跃用户"]
    for q in demos:
        print(f"用户: {q}")
        print(f"AI: {bot.respond(q)}\n")
    print(json.dumps({"queries": bot.queries, "uptime": bot.start_time}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
