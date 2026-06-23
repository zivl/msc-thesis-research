---
title: "Results"
---

Table 6 describes the results we get by running the prediction model over the entire testing set. It shows the testing set actual classifications against our classifier’s prediction. To remind, apps which were classified as *unknown* are such that did not pass the minimum number of permissions threshold. In the last row of Table 6 we calculate the evaluation measurement criteria for the results, i.e. Positive Predictive Value, Negative Predictive Value and the Accuracy.

We will refer the results in Table 6 as our baseline results. Baseline results are plain results without any intervention by us to bias the algorithm or make any other “special tuning”.

<table style="width:95%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Test<br />
Outcome</strong></th>
<th colspan="2" style="text-align: center;"><strong>Gold Set</strong></th>
<th style="text-align: center;"><strong>Successful<br />
Predictions</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">Safe</td>
<td style="text-align: center;">Malicious</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">Safe</td>
<td style="text-align: center;">1359</td>
<td style="text-align: center;">162</td>
<td rowspan="2" style="text-align: center;">3182</td>
</tr>
<tr>
<td style="text-align: center;">Malicious</td>
<td style="text-align: center;">598</td>
<td style="text-align: center;">1823</td>
</tr>
<tr>
<td style="text-align: center;">Unknown</td>
<td style="text-align: center;">43 (2.2%)</td>
<td style="text-align: center;">15 (0.8%)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">Ratio (%)</td>
<td style="text-align: center;">Precision</td>
<td style="text-align: center;">True Negatives (Np)</td>
<td style="text-align: center;">Accuracy</td>
</tr>
<tr>
<td style="text-align: center;"><strong>69.4%</strong></td>
<td style="text-align: center;"><strong>91.8%</strong></td>
<td style="text-align: center;"><strong>80.7%</strong></td>
</tr>
</tbody>
</table>

Table 6 - Baseline Results

## Set Confidence Threshold

In addition to the number of permissions threshold, we introduce the possibility to set a threshold over the prediction’s probability level – the confidence. Why?

For instance, if the stockbroker had told you to put your money on a certain share at the stock exchange with probability of 51% that this share rises tomorrow you wouldn’t really take him/her seriously.

We encounter exactly the same issue in some classifications. An app which was classified with probability of 51% doesn’t really count. While analyzing the results, we spotted among misclassified apps many with very low probability level, i.e. a malicious app was classified as malicious app, but with probability of 50%-60%. Thus, we want to ignore those kind of results, where the confidence level is too low. Similar to the previous threshold, apps which did not pass the threshold were classified as *unknown*. Consider that the decision regarding classification with less than the desired confidence could be in the hand of a third factor. Perhaps this factor maybe another security system, perhaps it will be the individual user or the enterprise organization IT department.

In Figure 10, we show the results of a few different tests. In each test, we set the confidence level threshold to different value.

Note: during this process there are apps that dropped out of the test set and are not counted in any of the evaluation criteria.


<figure>
<img src="/msc-thesis-research/images/figure10-threshold-confidence.png" alt="Figure 10 - Evaluation results over different levels of confidence threshold" />
<figcaption>Figure 10 - Evaluation results over different levels of confidence threshold</figcaption>
</figure>


The results shown in Figure 10 reflects the trade-off between conservativeness and permissiveness in classification algorithms. As expected, as we set the confidence threshold higher – the *true positive* and *true negative* metrics goes higher as well as the *accuracy*. Additionally, the amount of dropped out apps increases. Intuitively, this simply caused due to the fact that the algorithm takes only what it classified with confidence above the set threshold and the more we want the algorithm to be sure in its classification – it will drop apps away when they don’t pass that confidence level. For the same reason, the *false negative* and *false positive* metrics going low respectively. On the other hand, as the threshold goes higher the amount of dropped out apps increases. Significantly, we see the increasing of the *unknown* good apps. From our baseline test, we are aware that our classifier does not excels in good apps classification. This significant increase in the amount of good apps which were classified as *unknown*, yet with only minor increase of the *true positive* metric points out a training dataset issue regarding the good apps. This issue is further discussed in section 7.4

Threshold over the confidence is another configurable parameter for the algorithm consumer. In this way, where an app that is classified as *unknown*, the decision regarding that app could be provided or handled by another factor.

## Classifier Stability

A classifier is considered stable enough when minor modification in the training set will not have significant effect on classification results. In order to determine stability we run a several trials such that, for each trial a new classifier was constructed with randomly picked safe and malicious apps for training (from the same repositories as described in section 6.1). Though, the testing set stays the same. The baseline results (Table 6) are used as a reference for comparison.

In Table 7, you may find the testing results of 10 trials. For each trial result, we specify the following measurements criteria: accuracy, precision and negative predictive value.

| Trial No. | Accuracy | Positive Predictive Value | Negative Predictive Value |
|:---------:|:--------:|:-------------------------:|:-------------------------:|
|     1     |  81.1%   |           70.3%           |           90.9%           |
|     2     |  82.5%   |           73.0%           |           91.0%           |
|     3     |  81.4%   |           73.2%           |           88.8%           |
|     4     |  81.5%   |           72.4%           |           89.8%           |
|     5     |  81.7%   |           71.5%           |           90.9%           |
|     6     |  79.7%   |           69.2%           |           90.6%           |
|     7     |  81.6%   |           72.5%           |           89.8%           |
|     8     |  81.7%   |           71.9%           |           90.6%           |
|     9     |  81.4%   |           72.3%           |           89.7%           |
|    10     |  81.6%   |           71.5%           |           90.8%           |

Table 7 - Results of random training set models

By the results shown in Table 7, we see that the minimal precision value was 69.2% and the maximal value was 73.2%, a difference of about 5% and our original results are within this range. In the negative predictive value criterion, the minimum value was 88.8% and the maximum value was 91%, difference of about 2.2% and our original results are within this range as well.

Concluding from these facts, our classifier is stable and is not overly sensitive for minor changes in the training set.

## Algorithm Performance

Our testing and experiments were done on a Windows 7 PC, with 8GB RAM and quad-core processor. Though, the entire code is written in Java, so it can be deployed everywhere. As seen in the diagram in Figure 7, the system has 2 phases. One phase responsible for the algorithm training and the second phase is actual classification of test set apps. The training process is considered as the “heavy” phase of creating a classifier and is usually done “offline”. In our implementation, the training process takes ~200ms over the whole trainings set of 700 samples. The classification/prediction phase is usually done online and with some interaction with another system or with the user that waits for the classification response. In our implementation this process takes ~2ms per one app instance, which means that our implementation could be hosted on any system without any overhead to affect the hosted system responsiveness or overuse its resources.

## Results Analysis

We would like to point out why there are some apps that are failing from being predicted correctly. Although the *malicious* apps testing results are relatively much better than the *safe* app results, we try to find the general reason why our classifier fails.

As part of the inspection, we extracted out the classifier’s data and scoring regarding each permission which had been modeled. We mapped the permissions histogram over the following data:

- Training dataset.

- Failing apps in the safe apps testing set

- Failing apps in the malicious apps testing set

In addition, we joined the scores for each permission, given by the <u>trained</u> classifier. All of those histograms data and information can be found in *Appendix A - Permissions Histograms.*

After deep inspection and analysis of the failed apps we have come to the conclusion that many failed classifications were apps which required *highly scored permissions*. Recall, in the training process each permission *p* gets its score/weight *β<sub>p</sub>*. In each of the training sets, there are a few permissions which are more dominant in their specific set, hence scored relatively higher or lower, respectively to training set type. Many misclassified apps are using these highly scored permissions. In fact, more than 50% of the failing apps are using them.

For example, while inspecting the safe apps, we see that permissions such as *READ_PHONE_STATE*, *RECEIVE_SMS* and *READ_LOGS* appears relatively more in the failed apps than in the successfully classified apps. Combining this data with the training dataset histogram and scoring data we understand that those permissions are mostly used by malicious apps. The permissions specified above are highly dangerous permissions where an app that has one or a combination of them can learn a lot about the user’s device, information, private stuff and the user or device behavior. Perhaps, those safe apps which claim to have these dangerous permissions are not harmful as they were classified. However, these permissions are tightly related to malicious apps characteristics, hence, scored accordingly. A safe app that claims to have those permissions, not always though, has a better chance to be classified as malicious app.

In the previous paragraphs, we pointed out a problematic issue with our classifier. Since its knowledge is based on permissions only, there is a confusion regarding some apps with a certain combination of permissions, as described above. This leads us to try to reduce the permissions which are modeled to a smaller permission group in which only certain relevant and security-manner Android permissions are modeled. The data regarding that group with detailed information for each permission can be found at *Appendix B - Selective Group of Android Permissions*. Omitting features has to be considered carefully since this has a direct effect over the classifier. After carefully selecting the permissions to be modeled according to each permission relevance to malicious activity, we did another run with the same testing dataset as described in section 6.4.

We present in Table 8 the results of running the testing dataset with a classifier which was trained by modeling only the permissions specified in *Appendix B*. For discussion purposes and more convenient view perspective, we compare the results against Table 6 where we had a classifier trained with all permissions. The comparison is shown in Figure 11.

<table style="width:95%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Test<br />
Outcome</strong></th>
<th colspan="2" style="text-align: center;"><strong>Gold Set</strong></th>
<th style="text-align: center;"><strong>Successful<br />
Predictions</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">Safe</td>
<td style="text-align: center;">Malicious</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">Safe</td>
<td style="text-align: center;">1335</td>
<td style="text-align: center;">392</td>
<td rowspan="2" style="text-align: center;">2908</td>
</tr>
<tr>
<td style="text-align: center;">Malicious</td>
<td style="text-align: center;">463</td>
<td style="text-align: center;">1573</td>
</tr>
<tr>
<td style="text-align: center;">Unknown</td>
<td style="text-align: center;">164 (8.4%)</td>
<td style="text-align: center;">29 (1.5%)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">Ratio (%)</td>
<td style="text-align: center;">Precision</td>
<td style="text-align: center;">True Negatives</td>
<td style="text-align: center;">Accuracy</td>
</tr>
<tr>
<td style="text-align: center;"><strong>74.2%</strong></td>
<td style="text-align: center;"><strong>80.1%</strong></td>
<td style="text-align: center;"><strong>77.3%</strong></td>
</tr>
</tbody>
</table>

Table 8 - Classification Result with Reduced Permission Set


<figure>
<img src="/msc-thesis-research/images/figure11-permissions-modeling-comparison.png" alt="Figure 11 - Comparison of different groups of modeled permissions" />
<figcaption>Figure 11 - Comparison of different groups of modeled permissions</figcaption>
</figure>


From the results shown in Table 8 and the comparison in Figure 11, it is well seen that reducing the permission set to narrower one wasn’t successful. As expected, we see increase in *unknown* classifications among the safe apps. This increase caused by the fact that we omitted many permissions which are used by safe apps and now the classifier, which has a threshold over the minimum number of permissions – as described in section 6.5, dropped them away. Furthermore, by summing the total number of safe apps that were tested we won’t get 2000 as we gave as input – which means that there were some apps that were not tested at all due to the fact that they did not contain any permissions to model (they contain only permissions that were omitted). This is what causing the moderate increase in the *true positive* criterion and respectively, moderate decrease in the *false positive* criterion.

In addition, we get poor results in the malicious tested apps as well. Because we omitted many permissions, obviously some of them are included in the malicious apps as well. To begin with, the training dataset should have been changed accordingly when having this kind of change in feature modeling. We hoped to get better results by obtaining only the relevant permissions but instead we got worse results in every evaluation criterion.

Regardless the latter results, as seen in Table 6 results, our classifier can spot malicious apps with very high *true negative* ratio. Nevertheless, we cannot ignore the low *true positive* and *false positive* ratio results. We would not want this kind of behavior in a real system with such high *false positives*. Therefore, we point it out as a general issue of our classifier and the way we modeled apps into features for the classifier. Retrospectively, a classifier which its features are based on one type of parameter is not enough, at least not in our case. Due to lack of resources and scope of this paper we discuss in section 8 about future work that should be considered.
