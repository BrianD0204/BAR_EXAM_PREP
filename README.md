# Bar Study Studio

A static, editable study website for the **New York Bar Exam** in a gray light/dark theme. This is a **recreated version** of the study site, not a direct export of the original published project's source files.

## Open locally

1. Download and extract the ZIP.
2. Open `index.html` in Chrome, Edge, or Firefox.
3. Practice! No installation, server, account, API key, or subscription is needed.

For reliable saved progress across visits and computers, publish the files to GitHub Pages or another static host. Browser storage is tied to the specific site/browser; using a different address or clearing site data can reset progress. Back up any writing with the writing lab's **Save answer as .txt** button.

## Publish using GitHub Pages

1. Create a new GitHub repository, e.g. `bar-study-studio`.
2. Upload `index.html`, `style.css`, `script.js`, `questions.js`, `favicon.svg` to the repository's root (the `.tsv` and `.py` files are optional, intended for editing).
3. In **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, and save.
4. The site will be hosted at a URL resembling `https://YOUR_USERNAME.github.io/bar-study-studio/`.

## What the site includes

- 280 original, supplemental MBE practice prompts, spanning 7 subjects: Civil Procedure, Constitutional Law, Contracts, Criminal Law and Procedure, Evidence, Real Property, Torts.
- A set of **140 legal concepts** with two complementary questions each: an application scenario and a rule-recognition question.
- 10, 25, 50, 100, and 200-question practice sessions, configurable study/exam answer feedback, and editable countdown timers.
- Missed/unanswered/flagged filters, answer review, progress dashboard and per-subject coverage.
- 140 topic flashcards, eight essay prompts, two abbreviated MPT-style skills drills, a writing editor with saved drafts, timer, word counter, and text export.
- Editable study plan, exam-date countdown and daily practice goal.
- Persisted gray light/dark mode; saved answer history and flags using browser localStorage.

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | Website structure |
| `style.css` | Responsive gray themes and layouts |
| `script.js` | App interactions, timers, sessions, saved progress |
| `questions.js` | Loadable practice question bank |
| `questions.json` | Readable editable bank of 280 questions |
| `concepts.tsv` | 140 concepts and scenarios used to generate the bank |
| `generate_questions.py` | Rebuild `questions.js` and `questions.json` from `concepts.tsv` (run `python generate_questions.py`) |
| `favicon.svg` | Minimal site icon |

## Important content and exam note

**This question bank is independently drafted, introductory educational material—not official NCBE questions, not licensed or vetted by NCBE, and not a replacement for authoritative bar-preparation materials.** The fact patterns and rule-recognition items are intentionally concise. Professional bar preparation requires more complex, realistic fact patterns and official practice sets.

As of November 2026, New York plans to administer the legacy Uniform Bar Examination through **February 2028**, then transition to the **NextGen Bar Exam beginning July 2028**. The traditional MBE comprises **200 multiple-choice questions, 175 scored and 25 unscored**, in two three-hour sessions, while the UBE also includes essay and performance tests. Confirm the exam rules for your administration with:

- [National Conference of Bar Examiners](https://www.ncbex.org/exams/mbe/preparing-mbe)
- [New York State Board of Law Examiners](https://www.nybarexam.org/)
- [NCBE — New York jurisdiction](https://www.ncbex.org/jurisdictions/NY)

## How to customize

- **Colors:** change CSS variables at the beginning of `style.css` (`:root` and `:root[data-theme="dark"]`).
- **Site name:** change text in `index.html`.
- **Questions:** edit `concepts.tsv` and run `python generate_questions.py` or edit `questions.json` and regenerate `questions.js` manually. For new subjects or a different concept count, update validation in the generator.
- **Essay writing prompts:** edit the `PROMPTS` list near the beginning of `script.js`.
- **Data and privacy:** data does not leave the browser. No analytics, registration, paid API, or backend included.

Happy studying!

### Custom heart icon
The sidebar logo uses `♥` in `index.html`, and the browser-tab icon is defined in `favicon.svg`. Change either file to customize the heart.
