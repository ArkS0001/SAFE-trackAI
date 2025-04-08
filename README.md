# SAFE-trackAI
![Screenshot 2025-04-08 at 15-59-48 Hallucination Mitigat](https://github.com/user-attachments/assets/eeecdbd1-05ab-4ca0-993a-3d9ffe40583c)
![Screenshot 2025-04-08 at 16-00-00 Hallucination Mitigat](https://github.com/user-attachments/assets/f8ba4673-ff8e-470f-9371-55fc656645b3)

```
### 1. Input Phase
------------------------------------------------
| **Start:** Receive Input Prompt              |
|    (Text, Image, etc.)                       |
------------------------------------------------
             │
             ▼
------------------------------------------------------
| **Preprocessing:**                                 |
| - Tokenization & Language Detection                |
| - Normalize Input (remove noise, standardize case) |
------------------------------------------------------

### 2. Fuzzy Matching Module
             │
             ▼
-----------------------------------------------------
| **Fuzzy Matching Module:**                        |
| - Apply Levenshtein, Soundex, and n-Gram matching |
-----------------------------------------------------

### 3. LLM Contextual Check
             │
             ▼
------------------------------------------------
| **LLM Contextual Check:**                    |
| - One-Shot Evaluation to understand context  |
------------------------------------------------

### 4. Category Analysis
             │
             ▼
------------------------------------------------
| **Category Analysis:**                       |
| - Check for Bias (Religion/Political)        |
| - Detect Jailbreak Attempts                  |
| - NSFW Content Screening                     |
------------------------------------------------

### 5. Severity Scoring
             │
             ▼
------------------------------------------------
| **Severity Scoring:**                        |
| - Assign a score (0-10) for each category    |
| - Aggregate weighted scores                  |
------------------------------------------------

### 6. Multi-Modal Integration
             │
             ▼
------------------------------------------------
| **Multi-Modal Integration:**                 |
| - For images/audio: extract features & match |
------------------------------------------------

### 7. Output Phase
             │
             ▼
------------------------------------------------
| **Output:**                                  |
| - Final Severity Score (0-10)                |
------------------------------------------------
```
