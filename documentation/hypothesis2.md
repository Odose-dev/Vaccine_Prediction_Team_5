# Sprint 1 — Hypotheses and Research Questions

## 1. Hypotheses

### H1 — Beliefs Influence Vaccination

People who believe that the flu vaccine is effective and perceive vaccination as beneficial are more likely to get vaccinated.

**Relevant columns:**

- `opinion_h1n1_vacc_effective`
- `opinion_seas_vacc_effective`
- `opinion_h1n1_risk`
- `opinion_seas_risk`
- `h1n1_vaccine`
- `seasonal_vaccine`

---

### H2 — Demographics Influence Vaccination

Vaccination uptake differs across demographic groups such as age, education, income, and gender.

**Relevant columns:**

- `age_group`
- `education`
- `income_poverty`
- `sex`
- `race`
- `h1n1_vaccine`
- `seasonal_vaccine`

---

### H3 — Preventive Behaviour Is Associated with Vaccination

People who engage in preventive health behaviours are more likely to get vaccinated.

**Relevant columns:**

- `behavioral_wash_hands`
- `behavioral_face_mask`
- `behavioral_avoidance`
- `behavioral_large_gatherings`
- `behavioral_touch_face`
- `h1n1_vaccine`
- `seasonal_vaccine`

---

### H4 — Doctor Recommendations Influence Vaccination

People who receive a doctor's recommendation are more likely to get the corresponding vaccine.

**Relevant columns:**

- `doctor_recc_h1n1`
- `doctor_recc_seasonal`
- `h1n1_vaccine`
- `seasonal_vaccine`

> **Why this hypothesis is particularly strong:**  
> The relationship is very easy to communicate in a presentation.

---

### H5 — Vaccination Behaviours Are Correlated

People who receive the seasonal flu vaccine are more likely to have received the H1N1 vaccine.

**Relevant columns:**

- `h1n1_vaccine`
- `seasonal_vaccine`

> This directly addresses one of the Sprint's suggested hypotheses.

---

# 2. Research Questions

Now let's turn those hypotheses into questions we can actually answer with data.

### RQ1 — Age

**Are certain age groups more likely to receive the H1N1 and seasonal flu vaccines?**

We'll compare vaccination rates across:

- `18–34`
- `35–44`
- `45–54`
- `55–64`
- `65+`

---

### RQ2 — Demographics

**Do gender, education, and income level correlate with vaccination uptake?**

We'll investigate:

- `sex`
- `education`
- `income_poverty`

---

### RQ3 — Health Conditions

**Are people with chronic medical conditions more likely to receive flu vaccinations?**

**Relevant variable:**

- `chronic_med_condition`

We can also look at:

- `health_insurance`
- `health_worker`

---

### RQ4 — Doctor Recommendation

**How strongly is a doctor's recommendation associated with vaccination uptake?**

We'll compare:

- Doctor recommendation = **Yes**
- Doctor recommendation = **No**

against vaccination rates.

---

### RQ5 — Beliefs and Risk Perception

**Does people's perception of vaccine effectiveness and flu risk relate to vaccination decisions?**

**Relevant variables:**

- `opinion_h1n1_vacc_effective`
- `opinion_h1n1_risk`
- `opinion_seas_vacc_effective`
- `opinion_seas_risk`

---

### RQ6 — Preventive Behaviour

**Are people who engage in preventive behaviours more likely to get vaccinated?**

We'll investigate behaviours such as:

- Washing hands
- Avoiding large gatherings
- Wearing masks
- Avoiding contact with sick people
- Avoiding touching the face

---

### RQ7 — Relationship Between Vaccines

**Are people who received the seasonal flu vaccine also more likely to have received the H1N1 vaccine?**

This gives us a very clear cross-vaccine comparison.

---

# 3. Sprint 1 Hypothesis Table

| ID | Hypothesis |
|---|---|
| **H1** | Beliefs and risk perception influence vaccination decisions. |
| **H2** | Demographic characteristics are associated with vaccination uptake. |
| **H3** | Preventive health behaviours are associated with higher vaccination uptake. |
| **H4** | Doctor recommendations are strongly associated with vaccination uptake. |
| **H5** | H1N1 and seasonal flu vaccination behaviours are positively associated. |

---

# 4. Sprint 1 Research Question Table

| ID | Research Question |
|---|---|
| **RQ1** | Are certain age groups more likely to get vaccinated? |
| **RQ2** | Do gender, education, and income correlate with vaccination? |
| **RQ3** | Are people with chronic medical conditions more likely to get vaccinated? |
| **RQ4** | How strongly is a doctor's recommendation associated with vaccination? |
| **RQ5** | Does perceived vaccine effectiveness or flu risk relate to vaccination? |
| **RQ6** | Do preventive behaviours correlate with vaccination uptake? |
| **RQ7** | Are people who receive the seasonal vaccine also more likely to receive the H1N1 vaccine? |