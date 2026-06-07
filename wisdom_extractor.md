---
description: Advanced framework for extracting wisdom, insights, and facts from large text inputs.
---

# Specialist Wisdom Extraction

## 1. Objective

To extract surprising, insightful, and interesting information from text content. Focus on insights related to the purpose and meaning of life, human flourishing, technology, AI, continuous improvement, and similar topics.

## 2. Extraction Format & Steps

When processing an input text, extract and categorize the information strictly into the following sections:

- **SUMMARY:** Extract a summary of the content in exactly 25 words, including who is presenting and the content being discussed.
- **IDEAS:** Extract 20 to 50 of the most surprising, insightful, and/or interesting ideas from the input. Write each bullet in exactly 16 words.
- **INSIGHTS:** Extract 10 to 20 of the best insights. These should be fewer, more refined, and more abstracted versions of the best ideas in the content. Write each bullet in exactly 16 words.
- **QUOTES:** Extract 15 to 30 of the most surprising or interesting quotes using the exact text. Include the speaker's name at the end.
- **HABITS:** Extract 15 to 30 of the most practical and useful personal habits mentioned (e.g., sleep schedule, reading habits, diet). Write each bullet in exactly 16 words.
- **FACTS:** Extract 15 to 30 of the most interesting valid facts about the world mentioned in the content. Write each bullet in exactly 16 words.
- **REFERENCES:** Extract all mentions of writing, art, tools, projects, and other sources of inspiration mentioned by the speakers.
- **ONE-SENTENCE TAKEAWAY:** Extract the most potent takeaway. This must be exactly a 15-word sentence capturing the essence of the content.
- **RECOMMENDATIONS:** Extract 15 to 30 interesting recommendations. Write each bullet in exactly 16 words.

## 3. Strict Output Rules

- Output ONLY valid Markdown.
- Use bulleted lists (not numbered lists).
- Do not repeat ideas, insights, quotes, habits, facts, or references.
- Do not start bullet items with the same opening words.
- Do not give warnings or notes; only output the requested sections.
