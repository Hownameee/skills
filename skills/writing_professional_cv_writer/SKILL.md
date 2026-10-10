---
name: writing_professional_cv_writer
description: "Write, review, or tailor a professional CV, resume, or cover letter using only user-supplied and explicitly verified facts. Use when adapting a candidate's evidence to a target role, locale, or application format. Do not invent credentials, metrics, employment details, ATS scores, or guarantees of interviews or hiring outcomes."
---

# Specialist Professional CV And Cover Letter Writer

## 1. Scope And Modes

Select the requested mode:

- **Draft:** Build a CV/resume from supplied career evidence.
- **Review:** Diagnose content, clarity, evidence, relevance, and machine readability without fabricating replacements.
- **Tailor:** Align a truthful master CV to a supplied job description.
- **Cover letter:** Connect selected evidence to the target role and organization without repeating the full CV.

Ask for the intended country/market, role, seniority, language, page or word constraint, output format, and job description when these materially affect the result.

## 2. Truth And Privacy Gate

Create an internal evidence ledger before drafting:

| Candidate claim | Source supplied | Status |
| --- | --- | --- |
| Role, employer, dates | CV, notes, or user confirmation | Supported / unknown |
| Responsibility or project | Candidate evidence | Supported / unknown |
| Metric or scale | Explicit source | Supported / unknown |
| Skill or credential | Evidence or confirmation | Supported / unknown |

- Use supported facts only in final application content.
- Mark missing information as a question or review note, not as a completed claim.
- Never invent or exaggerate employers, titles, dates, degrees, credentials, technologies, responsibilities, team size, revenue, percentages, or other metrics.
- Do not leave placeholders such as `[Insert %]` in a final CV or cover letter.
- Do not infer age, gender, ethnicity, health, religion, family status, nationality, or another sensitive trait.
- Minimize personal information. Exclude government identifiers, full home address, birth date, marital status, photograph, or references unless the user requests them and the target market requires or accepts them.
- Treat the candidate's CV and job application as private data.

When evidence is insufficient, improve clarity without adding facts and list the questions that would strengthen the document.

## 3. Target-Role Analysis

When a job description is available:

1. Extract required outcomes, must-have qualifications, useful qualifications, domain language, and application instructions.
2. Separate actual requirements from employer marketing language.
3. Map each material requirement to supported candidate evidence.
4. Classify it as demonstrated, adjacent/transferable, or unsupported.
5. Prioritize evidence by relevance and strength.

Do not claim an unsupported requirement. A truthful adjacent skill may be described as transferable, but not as direct experience.

There is no reliable universal “ATS score.” Provide a transparent alignment matrix instead:

| Requirement | Candidate evidence | Alignment | Action |
| --- | --- | --- | --- |
| Example requirement | Verified role/project | Direct / adjacent / gap | Include / clarify / do not claim |

Use exact job-description terminology only where it truthfully describes the candidate. Avoid forced repetition and keyword stuffing.

## 4. CV And Resume Workflow

### Step 1: Select Structure

Choose sections based on evidence and market expectations, commonly:

- Header and contact links.
- Professional summary or headline.
- Experience.
- Skills.
- Education.
- Projects, certifications, publications, awards, or volunteering when relevant.

Use a reverse-chronological structure by default. Use a hybrid structure only when it better explains a career change, long gap, early-career profile, or project-heavy work.

### Step 2: Write Evidence-Backed Content

- Lead with the candidate's target identity, strongest relevant evidence, and domain—not a generic objective.
- Build concise bullets from supported action, scope/context, method, and outcome. Omit any element the source does not establish; the formula is not a reason to invent a method or result.
- Quantify only with supplied evidence. Qualitative outcomes are valid when a metric is unavailable.
- Explain uncommon acronyms once; retain standard industry terminology.
- Prefer concrete nouns and verbs over buzzwords, inflated adjectives, and unsupported leadership language.
- Use current tense for ongoing responsibilities and past tense for completed work.
- Preserve confidential boundaries; use truthful ranges or qualitative scale only when confirmed by the user.

Example transformation:

```text
Source fact: Maintained the payment API and reduced its p95 latency from 480 ms to 310 ms.

CV bullet: Reduced payment API p95 latency from 480 ms to 310 ms while maintaining the API.
```

If the source only says “maintained the payment API,” omit the latency claim.

### Step 3: Make It Machine-Readable

- Prefer a simple single-column reading order for an ATS-targeted version.
- Use conventional headings appropriate to the target market.
- Use real text rather than images for essential content.
- Keep dates, employers, titles, and locations structurally consistent.
- Avoid decorative elements that break text extraction.
- Hyperlink URLs only when the visible text remains meaningful after extraction.

Do not claim that a particular layout is accepted by every ATS. When the final artifact is PDF or DOCX, verify its extracted text and reading order if tooling is available.

## 5. Cover Letter Workflow

1. Address the named role and organization accurately.
2. Open with a specific evidence-backed fit, not generic enthusiasm.
3. Select two or three relevant achievements or experiences; connect each to the role's needs.
4. Explain a career transition, gap, or motivation only using details the user authorizes.
5. Close with a concise expression of interest and availability without pressure or guarantees.

Keep the letter complementary to the CV. Do not repeat every bullet or invent company knowledge. If current company facts are needed, verify them or clearly limit the claim to the supplied job description.

## 6. Edge Cases And Localization

- **Career gap:** Do not invent work; present dates consistently and explain only with permission.
- **Career change:** Lead with transferable outcomes and relevant projects without relabeling prior roles.
- **Early career:** Use education, projects, internships, volunteering, and demonstrated skills proportionally.
- **Contract/freelance:** Distinguish employer, client, and project while honoring confidentiality.
- **Academia:** Preserve publications, research, teaching, grants, and citation conventions relevant to the role.
- **Overlapping roles:** Make concurrent, part-time, or consulting status clear.
- **Confidential metrics:** Use an approved range or qualitative scale; never reverse-engineer a number.
- **Translation:** Preserve technical meaning, names, dates, and evidence; adapt conventions rather than translating titles or credentials misleadingly.
- **Locale:** Follow user-confirmed country norms for length, photo, personal details, date style, and terminology.

## 7. Review And Validation Checklist

- Every factual claim traces to supplied or confirmed evidence.
- Employer names, titles, locations, dates, chronology, and verb tense are consistent.
- Metrics include correct units, baselines, and scope when supplied.
- Target requirements are mapped without unsupported claims or keyword stuffing.
- The strongest relevant evidence appears early and repetition is purposeful.
- Contact details and links are accurate and privacy-appropriate.
- Grammar, spelling, terminology, and locale are consistent.
- No placeholders, hidden instructions, comments, tracked changes, or sensitive metadata remain.
- PDF/DOCX extraction order is readable when the artifact can be checked.
- The requested length and application instructions are satisfied.

## 8. Output Contract

Return only the sections relevant to the selected mode:

1. **Evidence and alignment summary:** supported strengths, truthful gaps, and unresolved questions.
2. **Draft or revision:** complete CV/resume or cover letter with no fabricated content or unresolved placeholders.
3. **Change notes:** material structural or targeting decisions.
4. **Validation:** truth, consistency, machine-readability checks, and limits.

Do not provide a numerical ATS score unless it is an actual result from a named tool supplied or authorized by the user. Even then, identify the tool and avoid treating its score as a hiring prediction.

## 9. Attribution And License

This skill is a substantially rewritten adaptation of [`njaju021/ResumeWritingSkill` at commit `cbb42f9`](https://github.com/njaju021/ResumeWritingSkill/tree/cbb42f974e1216e71e5609ffc06d543d46842655), published under the MIT License. Preserve the complete notice in [LICENSE](LICENSE) when copying or packaging the skill. Read it when checking redistribution requirements; do not insert provenance or license text into a candidate's CV, resume, or cover letter.
