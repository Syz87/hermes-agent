# 中文化 PR 策略计划

> 审查日期: 2026-05-22
> 状态: 规划中

## 1. 目标

将 Hermes 网关后端的硬编码英文消息转为 i18n `t()` 调用，使中文用户获得本地化体验，同时不影响英文用户。

## 2. 现有社区 PR 审查

### PR #27395（gaoang0802）— ⚠️ 高度重叠

| 维度 | 详情 |
|------|------|
| 标题 | i18n: add zh-CN translation for gateway and agent runtime status messages |
| 状态 | Open（5/17 创建，5/19 最后更新） |
| 覆盖 | gateway/run.py（10 个 key）+ run_agent.py（29 个 key）+ 15 语言 locale 文件 |
| 独有价值 | **run_agent.py 运行时消息**（12000+ 行），这是他最大的贡献 |

**与我们的重叠（gateway/run.py）：**

| 功能 | 他的 key | 我们的 key | 重叠？ |
|------|----------|-----------|--------|
| 重启通知 | `gateway.restart_notice` | `gateway.restart.restarting_hint` | ⚠️ 同一代码段 |
| 关闭通知 | `gateway.shutdown_notice` | `gateway.restart.shutting_down` | ⚠️ 同一代码段 |
| 排队消息 | `gateway.queued_next_turn` | — | ❌ 他独有 |
| 打断消息 | `gateway.interrupting_current_task` | — | ❌ 他独有 |
| 模型空响应 | `gateway.model_no_response` | — | ❌ 他独有 |
| 审批文本 | `gateway.approval_text_prompt` | — | ❌ 他独有 |
| 进度消息 | `gateway.still_working` | — | ❌ 他独有 |
| 状态信息 | `gateway.status_elapsed/iteration/running` | — | ❌ 他独有 |
| 重启成功 | — | `gateway.restart.success` | ❌ 我们独有 |
| 在线通知 | — | `gateway.online` | ❌ 我们独有 |

**冲突行号区域：** ~3081 vs ~2704/2810、~14079 vs ~16484、~16593 vs ~16021

### PR #28853（ayhanmalkoc）— 无冲突

Web Dashboard 前端 i18n（React/TypeScript），完全不同的模块，零重叠。

### 其他相关 PR/Issue

| 编号 | 内容 | 关联度 |
|------|------|--------|
| #23574 | 扩展中文覆盖范围 | 间接相关 |
| #24252 | 中文社区补丁集 | 可能重叠 |
| #27848 | BLOCKED 提示未本地化 | 我们未覆盖 |
| #23943 | Nix 包缺失 locale 文件（P1 bug） | 不影响我们 |

## 3. 我们当前改动审查

### 已改动文件（9 个，已 apply 到 working tree）

| 文件 | 改动量 | 与 #27395 重叠 | 价值 |
|------|--------|---------------|------|
| `gateway/run.py` | +67/-20 | ⚠️ 部分重叠 | 中（仅 4 个新 key） |
| `locales/en.yaml` | +4 | ⚠️ 不重复但 key 名不同 | 低（#27395 用不同 key 名） |
| `locales/zh.yaml` | +4 | ⚠️ 同上 | 低 |
| `gateway/platforms/telegram.py` | +6/-6 | ✅ 无重叠 | **高** |
| `gateway/platforms/qqbot/adapter.py` | +1/-1 | ✅ 无重叠 | **高** |
| `gateway/platforms/feishu.py` | +4/-4 | ✅ 无重叠 | **高** |
| `gateway/platforms/slack.py` | +3/-3 | ✅ 无重叠 | **高** |
| `gateway/platforms/matrix.py` | +5/-5 | ✅ 无重叠 | **高** |
| `hermes_cli/setup.py` | +48/-10 | ✅ 无重叠 | **高** |

### 关键发现

1. **上游 gateway/run.py 已有 236 个 `t()` 调用**——我们只新增了 4 个，说明大部分 i18n 工作已完成
2. **en.yaml/zh.yaml 中我们的 4 个 key 不与 #27395 重复**（key 名不同），但修改了相同的代码段
3. **平台适配器翻译是我们独有且无重叠的最大价值**
4. **setup.py 配置向导翻译也是独有贡献**

## 4. 策略决策

### 方案 A：等 #27395 合并后 rebase（推荐 ⭐）

**理由：**
- #27395 覆盖面更广（run_agent.py 29 个 key 是大头）
- 作者 gaoang0802 先提交，先合并合理
- 我们的独有贡献（平台适配器 + setup.py + 2 个 gateway key）不受影响
- 避免社区贡献者之间的冲突

**步骤：**
1. 在 #27395 下留言，说明我们有平台适配器翻译，看是否可以配合
2. 等 #27395 合并
3. Rebase 到 #27395 基础上，只保留我们的独有改动：
   - `gateway.restart.restarting_hint` + `gateway.restart.shutting_down`（与他的 key 名不同，可并存）
   - `gateway.restart.success` + `gateway.online`（他没做）
   - 5 个平台适配器审批按钮
   - setup.py 配置向导
4. 提交新 PR

### 方案 B：先提交我们的（不推荐）

**风险：**
- 与 #27395 在 gateway/run.py 上有行级冲突
- 合并任一 PR 后另一个需要 rebase
- 可能让其他贡献者觉得我们在抢功

### 方案 C：合并到 #27395（如果作者愿意）

**做法：**
- 联系 gaoang0802，建议把平台适配器和 setup.py 改动加入他的 PR
- 我们的改动 fork 到他的分支
- 一个 PR 搞定所有后端中文化

## 5. 推荐行动（方案 A）

### Phase 1：协调（现在）

1. **在 #27395 留言**，内容要点：
   - 我们在做平台适配器（Telegram/QQ/Feishu/Slack/Matrix）审批按钮的中文化
   - 以及 setup.py 配置向导的翻译
   - 问他是否愿意合并，还是等他合并后我们单独提 PR
   - 表示尊重他的先发贡献

2. **暂不提交 PR**，等回复

### Phase 2：清理 patch（等回复后）

3. **回滚 gateway/run.py 的重复改动**（与 #27395 重叠的部分）：
   - 删除 `gateway.restart.restarting_hint` 和 `gateway.restart.shutting_down`（用他的 `restart_notice`/`shutdown_notice`）
   - 保留 `gateway.restart.success` 和 `gateway.online`（他没做）

4. **更新 en.yaml/zh.yaml**：
   - 去掉与 #27395 重复的 key
   - 只保留 `gateway.restart.success` 和 `gateway.online`

5. **保留平台适配器和 setup.py 改动**（完全独有）

### Phase 3：提交

6. 基于 #27395 合并后的代码 rebase
7. 提交 PR，标题建议：`feat(i18n): localize platform adapters + setup wizard for zh-CN`

## 6. 对英文用户的影响

**结论：零影响。**

- 所有 `t()` 调用在 `display.language = "en"` 时返回 en.yaml 中的英文字符串
- 英文字符串与原始硬编码完全一致
- 平台适配器的 "Approve"/"Deny" → en.yaml 中也是 "Approve"/"Deny"
- setup.py 的英文提示词保持不变

## 7. 风险与待确认

| 风险 | 严重度 | 应对 |
|------|--------|------|
| #27395 长期不合并 | 中 | 设 deadline，超时后可考虑方案 B |
| #27395 作者拒绝配合 | 低 | 走方案 A，等合并后 rebase |
| Key 命名冲突 | 低 | 我们的 key 名不同（`restart.restarting_hint` vs `restart_notice`） |
| en.yaml 重复 key | 低 | 我们的 key 不与他重复，不会产生 YAML 重复 |

## 8. 验证清单

- [ ] 在 #27395 留言协调
- [ ] 等待回复
- [ ] 清理 patch（去重叠部分）
- [ ] 重新生成 patch 文件
- [ ] `git apply --check` 验证
- [ ] 本地重启网关测试中文消息
- [ ] 测试英文模式确认无回归
- [ ] 提交 PR
