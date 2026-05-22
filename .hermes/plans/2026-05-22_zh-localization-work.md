# 中文化本地工作计划

> 审查日期: 2026-05-22
> 状态: 规划中
> 前提: 参考 PR #27395（gaoang0802）覆盖范围，避免重复劳动

## 1. 背景

上游 gateway/run.py **已有 236 个 `t()` 调用**，locales 中有 **271 个 key**。但仍有大量硬编码英文消息未翻译。

PR #27395 覆盖了 gateway/run.py 中 10 个核心运行时消息 + run_agent.py 29 个 key，我们不应重复。

## 2. 覆盖范围划分

### 2.1 我们不做（#27395 已覆盖）

| 消息 | #27395 的 key |
|------|--------------|
| Gateway restarting — ... | `gateway.restart_notice` |
| Gateway shutting down — ... | `gateway.shutdown_notice` |
| Queued for the next turn... | `gateway.queued_next_turn` |
| Interrupting current task... | `gateway.interrupting_current_task` |
| Model returned no response... | `gateway.model_no_response` |
| Dangerous command requires approval... | `gateway.approval_text_prompt` |
| Still working... (N min elapsed) | `gateway.still_working` |
| N min elapsed / iteration N/M / running: tool | `gateway.status_*` |
| run_agent.py 全部运行时消息 | `run_agent.*`（29 个 key） |

### 2.2 我们要做的（分三个层级）

---

#### Tier 1：高价值小改动（优先做）

**A. Gateway 在线/重启成功通知（2 处）**

| 行号 | 原始英文 | 新 key |
|------|---------|--------|
| L14041 | `♻ Gateway restarted successfully. Your session continues.` | `gateway.restart.success` |
| L14082 | `♻️ Gateway online — Hermes is back and ready.` | `gateway.online` |

注：这两个 key 在 en.yaml/zh.yaml 中**尚不存在**，需要新增。

**B. 平台适配器审批按钮（5 个文件）**

| 平台 | 文件 | 硬编码字符串 | 改动量 |
|------|------|-------------|--------|
| Telegram | `gateway/platforms/telegram.py` | "✅ Approve Once" / "✅ Approve for Session" / "✅ Approve Always" / "❌ Deny" | ~6 行 |
| QQ | `gateway/platforms/qqbot/adapter.py` | 审批按钮文本 | ~2 行 |
| Feishu | `gateway/platforms/feishu.py` | "Approved once" / "Approved for session" / "Approved permanently" / "Denied" | ~4 行 |
| Slack | `gateway/platforms/slack.py` | 审批按钮文本 | ~6 行 |
| Matrix | `gateway/platforms/matrix.py` | 审批提示文本（approve/deny reaction 说明） | ~6 行 |

新增 locale key：`platform.approve_once` / `platform.approve_session` / `platform.approve_always` / `platform.deny` / `platform.approve` 等。

---

#### Tier 1C：Agent 运行时消息代码补全（#27395 盲区）

#27395 加了 locale key 但没改 agent/ 下的原始代码。这些文件仍然硬编码英文：

| 文件 | 行号 | 消息 | locale key（已存在） |
|------|------|------|---------------------|
| `agent/background_review.py` | L504,510 | 💾 Self-improvement review: {summary} | `run_agent.self_improvement_review` |
| `agent/conversation_compression.py` | L305 | 🗜️ Compacting context — summarizing... | `run_agent.compending_context` |
| `agent/conversation_loop.py` | L3399 | ⟳ compacting context… | `run_agent.compending_context` |
| `agent/conversation_loop.py` | L451 | 📦 Preflight compression: ~N tokens... | `run_agent.preflight_compression` |

改动方式：`from agent.i18n import t` + 替换硬编码字符串为 `t()` 调用。

注：#27395 把部分逻辑搬到了 run_agent.py，但 agent/ 下的原始代码仍存在。
等 #27395 合并后可能需要 rebase，但这些改动本身不会冲突。

---

#### Tier 2：中等改动（Tier 1 完成后）

**C. Gateway 其他硬编码消息（14 处，不含 #27395 覆盖的）**

| 行号 | 消息 | 建议 key |
|------|------|---------|
| L153 | Provider authentication failed. Check... | `gateway.auth_failed_hint` |
| L2868 | Gateway is {action} and is not accepting another turn | `gateway.busy_another_turn` |
| L6818-6819 | Queued for the next turn (depth) | `gateway.queued_depth` |
| L6849 | Steer failed: {exc} | `gateway.steer_failed` |
| L6869 | Agent is running — wait or /stop first (model switch) | `gateway.agent_running_model` |
| L6874 | Agent is running — wait or /stop first (provider switch) | `gateway.agent_running_provider` |
| L6914 | Agent is running — use /goal... | `gateway.agent_running_goal` |
| L6961 | Agent is running — /command can't run | `gateway.agent_running_cmd` |
| L7023 | Gateway is {action} — not accepting turn (slash cmd) | `gateway.busy_slash` |
| L7316 | Gateway is {action} — not accepting new work | `gateway.busy_new_work` |
| L10243 | Could not load config | `gateway.config_load_failed` |
| L13981-13987 | Hermes update finished/failed/timed out | `gateway.update_finished` / `gateway.update_failed` |
| L13816 | Hermes update finished (simple) | `gateway.update_finished_simple` |
| L13908 | Hermes update timed out | `gateway.update_timeout` |
| L17186 | No activity for N min | `gateway.no_activity_warn` |
| L17248 | Agent inactive for N min — no tool calls | `gateway.agent_inactive` |

**D. Setup.py 关键页面（约 30 个核心字符串）**

只翻译用户最常看到的几个页面，不翻全部 302 个：

| 页面 | 字符串数 | 内容 |
|------|---------|------|
| 欢迎/概览 | ~5 | Welcome header, navigation hints |
| Provider 选择 | ~8 | "Choose how to connect", provider list |
| API Key 输入 | ~5 | "Get your key at:", "Saved", "Skipped" |
| 完成/摘要 | ~10 | Summary, tool availability, tips |

新增 `setup.*` locale 模块。

---

#### Tier 3：后续可做

- Setup.py 全部 302 个字符串
- Gateway 剩余低频消息（background task、compression 等）
- `hermes_cli/` 其他 CLI 消息

## 3. Locale 文件变更

### en.yaml 新增

```yaml
# Tier 1
gateway:
  restart:
    success: "♻ Gateway restarted successfully. Your session continues."
  online: "♻️ Gateway online — Hermes is back and ready."

platform:
  approve_once: "✅ Approve Once"
  approve_session: "✅ Approve for Session"
  approve_always: "✅ Approve Always"
  deny: "❌ Deny"
  approved_once: "Approved once"
  approved_session: "Approved for session"
  approved_always: "Approved permanently"
  denied: "Denied"

# Tier 2 (gateway.* 按上面表格添加)
# Tier 2 (setup.* 按上面表格添加)
```

### zh.yaml 新增

```yaml
gateway:
  restart:
    success: "♻ 网关重启成功，会话继续。"
  online: "♻️ 网关已上线 — Hermes 准备就绪。"

platform:
  approve_once: "✅ 批准一次"
  approve_session: "✅ 本次会话批准"
  approve_always: "✅ 永久批准"
  deny: "❌ 拒绝"
  approved_once: "已批准一次"
  approved_session: "本次会话已批准"
  approved_always: "已永久批准"
  denied: "已拒绝"

# Tier 2 中文翻译...
```

### 其他 14 个语言文件

同步 key 结构，值用英文占位。

## 4. 实施步骤

### Step 1: Tier 1A — Gateway 通知（2 处）
1. 在 en.yaml/zh.yaml 新增 `gateway.restart.success` 和 `gateway.online`
2. 在 gateway/run.py L14041 和 L14082 改为 `t()` 调用
3. 验证：`git diff` 确认改动正确

### Step 2: Tier 1B — 平台适配器（5 个文件）
1. 在 en.yaml/zh.yaml 新增 `platform.*` 模块
2. telegram.py：改 4 个按钮文本
3. qqbot/adapter.py：改审批按钮
4. feishu.py：改 4 个状态文本
5. slack.py：改按钮文本
6. matrix.py：改审批提示文本
7. 同步其他 14 个语言文件

### Step 3: Tier 2C — Gateway 其他消息（14 处）
1. 逐个替换硬编码字符串为 `t()` 调用
2. 添加对应的 en.yaml/zh.yaml key

### Step 4: Tier 2D — Setup.py 核心页面（~30 处）
1. 在 en.yaml/zh.yaml 新增 `setup.*` 模块
2. 翻译核心页面的 print_* 调用

### Step 5: 验证
1. `git apply --check` 或 `git diff` 检查
2. 本地重启网关测试中文消息
3. 切回英文模式确认无回归

## 5. 对英文用户的影响

**零影响。** 所有 `t()` 调用在 `display.language = "en"` 时返回 en.yaml 中的英文字符串，与原始硬编码完全一致。

## 6. 文件清单

| 文件 | 改动 |
|------|------|
| `locales/en.yaml` | 新增 key（Tier 1 约 10 个，Tier 2 约 30 个） |
| `locales/zh.yaml` | 对应中文翻译 |
| `locales/*.yaml`（14 个） | key 同步，英文占位 |
| `gateway/run.py` | ~16 处 `t()` 替换（不含 #27395 覆盖的） |
| `gateway/platforms/telegram.py` | ~6 行按钮文本 |
| `gateway/platforms/qqbot/adapter.py` | ~2 行 |
| `gateway/platforms/feishu.py` | ~4 行 |
| `gateway/platforms/slack.py` | ~6 行 |
| `gateway/platforms/matrix.py` | ~6 行 |
| `agent/background_review.py` | ~4 行（Self-improvement review） |
| `agent/conversation_compression.py` | ~2 行（Compacting context） |
| `agent/conversation_loop.py` | ~4 行（Compacting context + Preflight compression） |
| `hermes_cli/setup.py` | ~30 行（Tier 2D） |

**总计：~20 个文件，~110 处改动**

## 7. 验证清单

- [ ] Tier 1A 完成：gateway.restart.success + gateway.online
- [ ] Tier 1B 完成：5 个平台适配器审批按钮
- [ ] en.yaml / zh.yaml key 无重复
- [ ] 其他 14 个语言文件 key 同步
- [ ] `git diff` 审查所有改动
- [ ] 本地重启网关测试中文
- [ ] 英文模式回归测试
- [ ] Tier 2 开始...
