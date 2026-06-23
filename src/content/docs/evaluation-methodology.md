---
title: "7. Evaluation Methodology"
---

Evaluating Binary Logistic Regression models are simple and easy to understand. Our classification result is a value from {*safe, malicious*}. In order to evaluate the classifier, each classification result sorted into one of the following groups, denoted as follows:

- tp = True Positives – Safe apps that were classified as safe apps.

- fp = False Positives – Safe apps that were classified as malicious apps.

- tn = True Negatives – Malicious apps that were classified as malicious apps.

- fn = False Negatives – Malicious apps that were classified as safe apps.

## 7.1. Evaluation Criteria

In our evaluations, we use the following, standard, measurements criteria to evaluate our results. You may also refer to Table 5 which visualizes the measurements criteria in a convenient way.

- Accuracy – In general measurement systems, accuracy defined as the degree of closeness of measurements of a quantity to that quantity's actual (true) value. In our binary model, it represents how well the model classifies the apps. The accuracy function in binary model is defined as follows:\
  \
  ``` math
  Ac(tp,\ fp,\ tn,\ fn) = \ \frac{tp + tn}{tp + fp + tn + fn}
  ```

- Precision – Also known as the “Positive Predictive Value”, defined as the proportion of the true positives against all the positive results (both true positives and false positives). In our case, it measures how many safe apps were classified as safe apps.\
  The Precision function in a binary model is defined as follows:

>
> ``` math
> \Pr(tp,\ fp) = \frac{tp}{tp + fp}
> ```

- Negative Predictive Value – just like the above criterion, we want to have a measurement of how many malicious apps were classified as malicious apps. The Negative Predictive Value is defined as the proportion of the true negatives against all the negative results (both true negatives and false negatives). The Negative Predictive Value function in a binary model is defined as follows:

>
> ``` math
> Np(tn,\ fn) = \frac{tn}{tn + fn}
> ```

<table style="width:98%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="2" rowspan="2" style="text-align: center;"></th>
<th colspan="2" style="text-align: center;">Classification of Apps in Gold Testing Set</th>
<th rowspan="2" style="text-align: center;"></th>
</tr>
<tr>
<th style="text-align: center;">Safe</th>
<th style="text-align: center;">Malicious</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: center;">Test Outcome</td>
<td style="text-align: center;">Safe</td>
<td style="text-align: center;">True Positive</td>
<td style="text-align: center;">False Negative</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">Malicious</td>
<td style="text-align: center;">False Positive</td>
<td style="text-align: center;">True Negative</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
<td style="text-align: center;">Positive Predicted Value</td>
<td style="text-align: center;">Negative Predictive Value</td>
<td style="text-align: center;">Accuracy</td>
</tr>
</tbody>
</table>

Table 5 – The measurements criteria used in the evaluation process

Each time we show some evaluation results of the prediction model (the classifier), we will use the terms explained above.
