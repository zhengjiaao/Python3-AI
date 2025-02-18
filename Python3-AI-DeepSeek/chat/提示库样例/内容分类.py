from openai import OpenAI

# 对文本内容进行分析，并对齐进行自动归类
client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="<YOUR_API_KEY>"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "system",
                "content": "#### 定位\n- 智能助手名称 ：新闻分类专家\n- 主要任务 ：对输入的新闻文本进行自动分类，识别其所属的新闻种类。\n\n#### 能力\n- 文本分析 ：能够准确分析新闻文本的内容和结构。\n- 分类识别 ：根据分析结果，将新闻文本分类到预定义的种类中。\n\n#### 知识储备\n- 新闻种类 ：\n  - 政治\n  - 经济\n  - 科技\n  - 娱乐\n  - 体育\n  - 教育\n  - 健康\n  - 国际\n  - 国内\n  - 社会\n\n#### 使用说明\n- 输入 ：一段新闻文本。\n- 输出 ：只输出新闻文本所属的种类，不需要额外解释。"
        },
        {
                "role": "user",
                "content": "美国太空探索技术公司（SpaceX）的猎鹰9号运载火箭（Falcon 9）在经历美国联邦航空管理局（Federal Aviation Administration，FAA）短暂叫停发射后，于当地时间8月31日凌晨重启了发射任务。"
        }
    ]
)

print(completion.choices[0].message.content)