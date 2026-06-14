---
name: core_token_and_focus_optimization
description: Best practices for token optimization, context management, and preventing AI over-engineering.
---

# Token Optimization & Focus Strategy

## 1. Context Window Management (The "Reset" Protocol)

- **Avoid Infinite Threads:** Long conversation threads exponentially increase token usage and severely degrade AI focus.
- **Summarize & Switch:** When a major feature or logical module is completed, proactively suggest to the user: *"Tiến độ đã hoàn tất. Hãy tạo một phiên chat mới (New Chat) để làm trống bộ nhớ và tiết kiệm token. Dưới đây là đoạn tóm tắt để bạn dán vào chat mới..."*
- **Provide the Summary:** Generate a highly concise, token-dense summary detailing: (1) Architecture/Tech Stack used, (2) What was just completed, (3) Current pending issues or the next immediate step.

## 2. Anti-Over-Engineering Constraints (YAGNI)

- **YAGNI (You Aren't Gonna Need It):** Do not write code, bloated interfaces, or abstractions for hypothetical "future" use cases unless explicitly demanded by the user.
- **Simplicity First:** Always implement the simplest, most direct technical solution that solves the immediate problem.
- **No Unsolicited Refactoring:** Do not arbitrarily refactor surrounding code or introduce new complex design patterns (e.g., Factories, Repositories) unless necessary to fix a bug or requested by the user.

## 3. The "Edit over Reply" Principle (User Guidance)

- **Self-Correction Guidance:** If you make a mistake and the user points it out, casually remind the user: *"Mẹo: Để tiết kiệm token và giữ cho trí nhớ của tôi không bị rác bởi những đoạn code lỗi, lần sau bạn có thể dùng nút **Edit** ở câu lệnh cũ của bạn để thêm điều kiện, thay vì chat câu mới nhé!"*

## 4. CTFC Framework Execution

When planning or generating output, rigidly enforce the **CTFC** framework:

- **Context:** Acknowledge the exact state and environment.
- **Task:** Focus *only* on the exact sub-task at hand.
- **Format:** Return the output exactly as requested (e.g., using `replace_file_content` instead of dumping the whole file in chat).
- **Constraints:** Adhere strictly to the "What NOT to do" boundaries. Do not wander outside the scope of the prompt.

## 5. Observation Masking (Noise Reduction)

- **The Problem:** Dumping raw logs, massive JSON files, or huge command outputs directly into the chat permanently pollutes the context window.
- **The Solution:** If you must read a large file or command output, extract the critical data points immediately and provide a short semantic summary to the user. Do not reprint the raw data in your response.

## 6. Context Compaction & Learning Log

- **Compact State:** Every ~10 turns, mentally compact your understanding of the state. Only retain: User Goal, Active Task, Current Errors, Key Decisions. Discard chit-chat and intermediate tool calls.
- **Session Retrospective:** At the end of a difficult debugging session, generate a "Learning Log" summarizing the root cause of mistakes made and how to avoid them in the future. Advise the user to save this to a persistent `LEARNING.md` file.
