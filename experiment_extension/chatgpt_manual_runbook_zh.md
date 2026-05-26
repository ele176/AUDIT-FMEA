# ChatGPT 手工生成实验 Runbook

目的：用 ChatGPT 补充 repeated-run stability 和 role-ablation 结果，为 AUDIT-FMEA 顶会/强刊版本提供更强方法证据。

## 总原则

1. 每个 run 开一个新的 ChatGPT 对话。
2. 不要让 ChatGPT 看之前 run 的输出。
3. 每个 run 只粘贴对应 prompt。
4. 输出必须是 CSV，不要解释文字。
5. 生成后把 CSV 保存到指定文件名。
6. 不要手工美化结果。只允许修正 CSV 格式错误，例如多余说明文字、代码块标记、明显断行。

## 你需要记录的信息

每次生成后，在 `data/run_manifest.csv` 里补：

- `model_name`：ChatGPT 页面显示的模型名，比如 GPT-5、GPT-4.1、GPT-4o 等。
- `model_provider`：OpenAI。
- `date_generated`：生成日期，例如 2026-05-24。
- `temperature`：如果网页端看不到，写 `not_available_web_ui`。
- `top_p`：如果网页端看不到，写 `not_available_web_ui`。
- `seed_or_session_id`：网页端通常没有，写 `not_available_web_ui`。
- `notes`：是否手工修正了 CSV 格式。

## 最小需要生成的文件

已有 run01 来自原始实验。你现在只需要补这些：

| Variant | Need files |
|---|---|
| M2 | `M2_run02.csv`, `M2_run03.csv` |
| M3 | `M3_run02.csv`, `M3_run03.csv` |
| M4_full | `M4_full_run02.csv`, `M4_full_run03.csv` |
| M4_no_critic | `M4_no_critic_run01.csv`, `M4_no_critic_run02.csv`, `M4_no_critic_run03.csv` |
| M4_no_integrity | `M4_no_integrity_run01.csv`, `M4_no_integrity_run02.csv`, `M4_no_integrity_run03.csv` |

保存位置：

`paper_project/08_top_conference_rework/experiment_extension/data/runs/`

## 生成顺序

推荐顺序：

1. M2_run02
2. M2_run03
3. M3_run02
4. M3_run03
5. M4_full_run02
6. M4_full_run03
7. M4_no_critic_run01
8. M4_no_critic_run02
9. M4_no_critic_run03
10. M4_no_integrity_run01
11. M4_no_integrity_run02
12. M4_no_integrity_run03

## 生成后怎么交给我

最简单：

1. 每个输出复制为 `.csv` 文件放到 `data/runs/`。
2. 回来告诉我“我放好了”。
3. 我会运行统计脚本、检查 CSV、修论文结果段。

如果你不会保存 CSV，就把 ChatGPT 输出直接贴给我，我帮你整理。

