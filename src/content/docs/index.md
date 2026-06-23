---
title: "Is This Safe or Not?"
---

<figure class="logo">
<img src="/msc-thesis-research/images/logo-idc.png" alt="IDC Herzliya — Efi Arazi School of Computer Science" style="width:260px" />
</figure>


The Interdisciplinary Center, Herzlia

Efi Arazi School of Computer Science

**Is This Safe or Not?**

**Mobile Apps Classification on Android**

M.Sc. Final Project

Submitted in Partial Fulfillment of the Requirements for the

Degree of Master of Science (M.Sc.) in Computer Science

Submitted by Ziv Levy

Under the supervision of Dr. David Movshovitz

October, 2014

## Acknowledgements

I would like take this opportunity and to thank my high-school sweetheart, my wife, for being there and supporting me during this long time of research.

I’d like to express my sincere gratitude to Dr. David Movshovitz, for his professional knowledge and expertise, to guide me in writing this work.

I would also like to thank Itamar Keller and Orgad Keller for hours of consulting and brainstorming.

## Abstract

With the increasing number of apps in the market, identifying malicious apps is a common concerns for all players in the market. Many enterprises invest much of their resources in protecting valuable data assets such as business and marketing data, design and engineering data and other data which is important to their business. Mobile users use apps on daily basis for productivity, social interaction, financial benefits, gaming and many other tasks. However, these apps may run malicious processes during their installation or operation. These malicious processes compromise the device and put the device’s owner at risk.

The term “app classification” in a security manner means to define whether an app is/maybe dangerous or not. A dangerous app could be an app specifically designed to be malicious (e.g., malware and spyware), or an app that can be exploited for malicious purposes due to vulnerabilities. It could be as well as privacy threats that might be caused by apps that are not necessarily malicious but gather or use sensitive information (e.g., location, address book, personally identifiable information) more than is necessary, or more than the user is comfortable with, to perform their function.

Mobile app classification has become an interesting problem in the mobile industry and is not a trivial task which is still under development. The major challenge is that there are not many effective and explicit features available for classification models due to the limited contextual information of apps available for the analysis \[45\]. Recent works regarding mobile security and mobile app classifications in particular, showed several techniques of classifications according to different app parameters and properties. In some works they used static code analysis to track the code behavior and functionality. In other cases, a set of static rules were defined to conditionally test against certain permissions or block/manipulate data transmission. These works will be reviewed broadly in section 4.

Nevertheless, at the time those lines were written, no one had tried to classify an app by the permissions required by the app. In Android, a permission is a restriction limiting access to a part of the code or to data on the device. The limitation is imposed to protect critical data and code that could be misused to distort or damage the user experience \[27\]. By definition, we assume that every required permission exposes some data. Consequently, the combination of permissions together in the same app is the cause of risk to the user. Therefore, this is what we are using to classify apps whether safe or not.

There are many classifiers algorithms, such as decision trees, k-nearest neighbor and support-vector-machine. We use Logistic Regression algorithms to predict an app classification given the app’s permissions. Logistic regression is type of statistical machine-learning technique and is especially used for binary classifications, e.g. {*yes*, *no*}, {*good*, bad}, etc. Further explanation is covered in section 5.

In this research we demonstrate that good classification of malicious apps can be achieved for Android OS by only inspecting the app’s permissions. We present an algorithm to classify apps with minimal overhead, reaching a classification time of less than 2ms while reaching more than 90% success rate in spotting dangerous apps. Being able to provide a simple answer whether a certain app is safe or malicious or what is the app’s potential risk, can help many users to keep their data safe, or at least they would be more conscious about the apps they install and run. Such solution will educate even the novice users to use his device and app wisely.

In this work we focus on Google’s Android Operating System. In section 1 we introduce the problem, following it in section 2 by a discussion of how Android’s security model operates: Why is it vulnerable? What are the attack vectors and what Google does about it? In this section we also analyze threats and risks involved, and show examples of exploitations of Android’s security model. In section 3 we show some statistics over a collection of more than 15,000 apps from Google Play and present the permissions usage trends and popularity

Section 4 explores previous research in the field. We discuss and criticize previous works and show advantages and disadvantages of each approach. We then present our approach in sections 5. We introduce the linear regression technique for statistical prediction for the classification problem. We show where technique is being used.

We further discuss in section 6, how we model our task as a classification problem following by discussion of our approach and it contributes to Android’s security mechanisms.\
Finally, we run tests and evaluate the algorithm’s prediction in section 7 and conclude in section 8.
