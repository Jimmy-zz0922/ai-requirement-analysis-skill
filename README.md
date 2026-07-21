# AI Requirement Analysis Skill

一个面向政务与企业数字化场景的 AI 辅助需求分析 Skill。它把访谈纪要、政策文件、业务流程、系统说明和数据接口材料，转换为可追溯的用户场景、平台问题、AI应用机会与标准需求卡片。

## 能解决什么问题

- 从访谈纪要中提取用户角色、场景、目标和痛点
- 从政策与业务文件中抽取流程、规则和异常分支
- 诊断跨系统、跨部门、流程与数据协同问题
- 判断问题是否适合使用大模型、RAG、规则引擎或传统功能
- 生成带原文证据、风险和人工复核点的需求卡片
- 沉淀统一字段、Prompt模板和质量控制流程

## 仓库结构

```text
ai-requirement-analysis-skill/
├── SKILL.md                         # Skill主说明
├── references/
│   ├── prompt-library.md            # 5类可复用Prompt
│   ├── field-dictionary.md          # 结构化字段与枚举
│   └── quality-rules.md             # 证据与质量规则
├── schemas/
│   └── requirement-analysis.schema.json
├── scripts/
│   ├── validate_output.py           # 校验JSON输出
│   └── export_csv.py                # 将需求卡片导出CSV
├── templates/
│   ├── analysis-request.md
│   ├── material-register.csv
│   └── requirement-card.json
├── examples/
│   ├── real-estate-input.md
│   └── real-estate-output.json
├── evals/
│   ├── evals.json
│   └── rubric.md
└── tests/
    └── test_examples.py
```

## 快速使用

将整个文件夹或打包后的 `.skill` 文件导入支持 Agent Skills 标准的产品，然后提供业务材料，例如：

```text
请使用 AI Requirement Analysis Skill 分析这些访谈纪要和系统资料，
输出用户场景、平台问题、AI应用机会和需求卡片。
所有结论需附原文证据，并标记待确认事项。
```

也可以只执行单个任务：

```text
根据这份访谈纪要提取用户痛点，不要直接给解决方案。
```

```text
评估这份问题清单中哪些适合使用大模型，哪些应使用规则引擎或普通功能。
```

## 本地校验

```bash
python -m pip install -r requirements.txt
python scripts/validate_output.py examples/real-estate-output.json
python scripts/export_csv.py examples/real-estate-output.json /tmp/requirements.csv
python -m unittest discover -s tests -v
```

## 上传到 GitHub

```bash
git init
git add .
git commit -m "feat: add AI requirement analysis skill"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-requirement-analysis-skill.git
git push -u origin main
```

## 简历表述

> 搭建 AI 辅助需求分析 Skill，沉淀5类可复用Prompt、30项结构化字段及标准化分析流程，实现从业务材料解析、用户痛点识别、平台诊断到AI适配评估和需求卡片生成的可复用处理。

## 使用边界

本 Skill 用于辅助产品分析，不替代业务、法律、审批、产权、资金和合规相关专业判断。高影响结论必须由业务负责人复核。

## License

MIT
