# Field Dictionary

## 一、来源与证据

| 字段 | 含义 |
|---|---|
| source_id | 材料唯一编号，如 SRC-001 |
| source_type | interview、policy、process、system、data、feedback、other |
| source_title | 文件、访谈或会议名称 |
| source_date | 材料日期 |
| source_version | 文件或规则版本 |
| locator | 页码、章节、段落、表格或时间点 |
| excerpt | 支撑结论的必要原文 |
| evidence_type | direct、cross_validated、inferred |
| evidence_confidence | high、medium、low |

## 二、用户与场景

| 字段 | 含义 |
|---|---|
| user_role | 用户角色或责任主体 |
| business_stage | 所处业务阶段 |
| scenario | 具体业务场景 |
| user_goal | 用户希望完成的任务 |
| current_behavior | 当前操作方式 |
| pain_point | 用户遇到的具体困难 |
| problem_type | 问题类型 |
| frequency | high、medium、low、unknown |
| impact_scope | 受影响的用户、部门或业务 |
| severity | high、medium、low |

## 三、流程、系统与数据

| 字段 | 含义 |
|---|---|
| process_node | 痛点所在流程节点 |
| business_rule | 条件、材料、审批或判断规则 |
| involved_systems | 涉及系统或端 |
| data_dependencies | 所需数据、来源及责任主体 |
| system_dependencies | 所需接口、权限或系统改造 |
| root_cause | 流程、机制、系统、数据或组织层原因 |
| business_impact | 对效率、体验、监管或决策的影响 |

## 四、AI与产品

| 字段 | 含义 |
|---|---|
| ai_fit | high、medium、low、not_recommended |
| ai_capability | llm_qa、rag、information_extraction、classification、content_generation、workflow_assistance、rules_engine、analytics、none |
| ai_rationale | 为什么适合或不适合AI |
| product_form | 办事助手、审批工作台、看板、驾驶舱等 |
| product_description | 方案如何解决问题 |
| alternative_non_ai | 流程、规则或普通功能替代方案 |
| human_review_points | 必须人工确认的位置 |
| risks | 准确性、权限、隐私、合规、可解释性等 |

## 五、需求管理

| 字段 | 含义 |
|---|---|
| requirement_id | 需求唯一编号，如 REQ-001 |
| title | 简短需求名称 |
| priority | P0、P1、P2、P3、defer |
| confidence | high、medium、low |
| validation_status | validated、partially_validated、pending、conflicted |
| open_questions | 进入设计或开发前需确认的问题 |

## 问题类型枚举

- `process_efficiency`：流程耗时、重复操作
- `information_access`：信息分散、查询困难
- `system_usability`：系统交互与操作问题
- `cross_department_collaboration`：跨部门协同
- `data_quality`：数据缺失、不一致、不可追溯
- `risk_supervision`：异常识别与监管
- `decision_support`：统计与决策支持不足
- `other`：其他

## 证据置信度

- `high`：存在清晰直接证据，且材料有效性明确
- `medium`：存在单一证据，或需要业务人员确认
- `low`：主要基于间接描述或材料版本不明

## 优先级建议

- `P0`：阻断核心业务、重大合规或安全风险
- `P1`：高频高影响，具备明确价值和实施条件
- `P2`：中等价值，依赖条件尚需补充
- `P3`：低频、局部体验优化
- `defer`：证据不足、风险过高或当前不具备条件
