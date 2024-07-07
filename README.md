# Explain the dataset

The dataset contains the following attributes:

1. Id: Unique identifier for each record.
2. Age: Age of the person (in days).
3. Gender: Gender (1 for female, 2 for male).
4. Height: Height in cm.
5. Weight: Weight in kg.
6. Ap_hi: Systolic blood pressure.
7. Ap_lo: Diastolic blood pressure.
8. Cholesterol: Cholesterol level (1: normal, 2: above normal, 3: well above normal).
9. Gluc: Glucose level (1: normal, 2: above normal, 3: well above normal).
10. Smoke: Whether the person smokes (1: yes, 0: no).
11. Alco: Whether the person consumes alcohol (1: yes, 0: no).
12. Active: Whether the person is physically active (1: yes, 0: no).
13. Cardio: Presence or absence of cardiovascular disease (1: presence, 0: absence).

# Analyse the dataset

### 1. Dataset size: 
	1. 70,000 rows
	2. 13 columns 

### 2. Missing values:
	1. id             0
	2. age            0
	3. gender         0
	4. height         0
	5. weight         0
	6. ap_hi          0
	7. ap_lo          0
	8. cholesterol    0
	9. gluc           0
	10. smoke          0
	11. alco           0
	12. active         0
	13. cardio         0

**There were no missing values**

### 3. Cardio dataset HeatMap

![Cardio Dataset heatmap](https://drive.google.com/uc?export=view&id=1dhXhIi0W-sqSZrV2K4-VN7UumuZXRGxF)

#### Heatmap Analysis
Analyzing a heatmap involves looking at the correlation coefficients between different features in a dataset. Here’s an interpretation based on the provided heatmap:

### Overview

- The heatmap shows correlation coefficients ranging from -1 to 1.
- Positive correlations are shown in shades of red, while negative correlations are in shades of blue.
- The color bar on the right indicates the strength of the correlation: red means a strong positive correlation, blue means a strong negative correlation, and white means no correlation.

### Correlations between input features and target feature
- id             0
- **age**            **0.24**
- gender         0.01
- height         -0.01
- **weight**         **0.18**
- ap_hi          0.05
- ap_lo          0.07
- **cholesterol**    **0.22**
- gluc           0.09
- smoke        -0.02
- alco           -0.01
- active         -0.04
- cardio        1

### Insights and Deductions

1. **Self-Correlation:**
   - The diagonal elements all have a correlation of 1 (dark red), which is expected as each feature is perfectly correlated with itself.

2. **Age and Cardio:**
   - There is a moderate positive correlation between `age` and `cardio` (0.24).
   - This suggests that older individuals are more likely to have cardiovascular conditions, which aligns with general medical understanding.

3. **Weight and Height:**
   - `weight` and `height` have a positive correlation of 0.29.
   - Taller individuals tend to weigh more, which is a common anthropometric observation.

4. **Height and Gender:**
   - There is a moderate positive correlation between `height` and `gender` (0.50).
   - This suggests that gender could be encoded such that one gender (likely male) is taller than the other (likely female), which is consistent with typical human height differences.

5. **Cholesterol and Gluc (Glucose):**
   - There is a moderate positive correlation between `cholesterol` and `gluc` (0.45).
   - Higher cholesterol levels are associated with higher glucose levels, indicating a potential link between lipid metabolism and glucose metabolism.

6. **Cardio and Cholesterol:**
   - `cardio` and `cholesterol` have a positive correlation (0.22).
   - This implies that higher cholesterol levels are associated with an increased likelihood of cardiovascular conditions, consistent with medical knowledge.

7. **Alcohol and Smoke:**
   - `alco` and `smoke` have a strong positive correlation (0.34).
   - Individuals who smoke are more likely to consume alcohol, which aligns with observed behavioral patterns.

8. **Ap_hi (Systolic Blood Pressure) and Ap_lo (Diastolic Blood Pressure):**
   - `ap_hi` and `ap_lo` have a positive correlation (0.45).
   - Systolic and diastolic blood pressure values are positively correlated, as they are both measures of blood pressure.

9. **Active and Cardio:**
   - `active` has a slight negative correlation with `cardio` (-0.04).
   - This weak negative correlation suggests that individuals who are more active might have a slightly lower risk of cardiovascular conditions.

### Explanations for Deductions

- **Age and Cardio:** Aging is associated with various risk factors such as hypertension, cholesterol buildup, and reduced physical activity, which contribute to cardiovascular diseases.
- **Weight and Height:** Height and weight are often correlated because larger body frames typically weigh more.
- **Height and Gender:** Men generally have taller average heights compared to women, which could explain the moderate correlation.
- **Cholesterol and Glucose:** Dyslipidemia (abnormal amount of lipids) and high blood sugar levels are both common in metabolic syndromes and diabetes.
- **Cardio and Cholesterol:** High cholesterol levels are a known risk factor for the development of cardiovascular diseases.
- **Alcohol and Smoke:** There is a well-documented correlation between smoking and alcohol consumption, often linked to lifestyle choices.
- **Systolic and Diastolic Blood Pressure:** Both are measures of blood pressure and naturally correlate as they are parts of the same cardiovascular assessment.
- **Active and Cardio:** Physical activity is known to reduce the risk of cardiovascular diseases, hence the negative correlation.

### Conclusion

The heatmap reveals several meaningful correlations within the dataset, confirming known medical and behavioral associations. These insights can be valuable for predictive modeling and understanding the underlying relationships between various health metrics.

We also understood that the important features that showed strong positive correlation with cardio were **'age'**, **'weight'**, **'cholesterol'** and **'ap_hi'**, **'ap_lo'** showed a medium positive correlation. SO we use those particular features that matter to train our model.

## Results

### 1st Iteration using important features
	Test size: 0.7
	Accuracy: 63%
 	Used important features only
### 2nd Iteration using all features
	Test size: 0.7
	Accuracy: 
