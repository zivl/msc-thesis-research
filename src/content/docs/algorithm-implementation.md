---
title: "6. The Algorithm Implementation"
---

## 6.1. LibLinear

LibLinear is an open source library for linear classification \[4\]. In the following paragraph we describe how to reduce the app’s permissions to LibLinear input and use it to predict whether the app is potentially *safe* or *malicious*.

We will start at the initial step of how we model an app and define our linear predictor function: Given a list of all of Android’s official permissions \[27\], we label each permission with a number between {1…n}, where *n* is the number of permissions in Android. For each app sample in we define a vector X (also of size n) to be:

$$
\forall x_{i} \in X,\ \ x_{i} = \left\{ \begin{array}{r}
1,\ if\ permission\ i\ exists\ in\ a\ given\ app \\
0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
\end{array} \right.\ 
$$

Next, we define our dependent variable: Let *y* be the algorithm result, the prediction, and is defined as following:

$$
y = \left\{ \begin{aligned}
0,\ \ \ \ \ \ \ \ \ \ \ if\ the\ app\ is\ considered\ as\ malicious \\
1,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  & if\ the\ app\ is\ considered\ as\ safe
\end{aligned} \right.\ 
$$

Thus, for each sample app *A* we construct a vector such that $A' = \left\{ y,x_{1},\ldots,x_{n} \right\}$

For example:

Let’s denote *A* as a *safe* app instance with the following permissions: *A = {ZZ}*. Assuming that there exists permissions such that XX is labeled 1, YY is labeled 2 and ZZ is labeled 3 (and these are the only permissions) – the instance *A* will be converted to the vector: *A’ = {1, 0, 0, 1}*

Our training dataset is a set of all corresponding vectors and are divided into safe and dangerous/malicious combinations, thus we define the following sets:

$$
\begin{bmatrix}
0 & x_{11}\cdots & x_{1n} \\
 \vdots & \ddots & \vdots \\
0 & \cdots & x_{pn}
\end{bmatrix}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \begin{bmatrix}
1 & x_{11}\cdots & x_{1n} \\
 \vdots & \ddots & \vdots \\
1 & \cdots & x_{pn}
\end{bmatrix}
$$

Dangerous/malicious permissions combinations Safe permissions combinations

We will denote *p<sub>d</sub> and p<sub>s</sub>* as the number of instances in the dangerous and safe set, respectively.

Since we are using a statistical model, the size of the sets must be the similar. Otherwise, since the learning process uses observed cases, the balance of seen cases may be biased and may cause to faulty prediction. For example, assume some visual classifier that can predict whether a four-leg mammal is a cat or a dog only by scanning an image. If the training dataset for this classifier will contain only dogs’ images (and maybe a few cats), obviously, most of its predictions would be “this is a dog”. It simply happens because there is not enough data in the corpus so that the model can learn the cat’s characteristics. In our case, unbalanced subsets, for example, the corpus will contain malicious apps, then the model is familiar only (or mostly) with malicious cases which will certainly affect its prediction strength.

In the training procedure, we pass LibLinear the two matrices from above of manually classified instances with its appropriate classification. LibLinear outputs a classifier by computing the coefficients $\beta_{i}$’s influence on the given classifications.

Now, we have a classifier capable of predicting the potential security hazard of any given app with the level of confidence in its decision, according to LibLinear classifier generation. This is a valuable feature that may be used for further calculations and statistical measurements.

Figure 9 summaries the classification procedure. The diagram represents a high-level architecture of this security mechanism (assume that training has already done off-line):


<figure>
<img src="/msc-thesis-research/images/figure9-classification-workflow.png" alt="Figure 9 - App Classification Workflow Diagram" />
<figcaption>Figure 9 - App Classification Workflow Diagram</figcaption>
</figure>


## 6.2. The Datasets

In machine-learning based algorithms the training dataset is also referred as the training set as well as the testing dataset which is also referred as the testing set. In the training process the model is familiarized with real world cases of its classification problem. As mentioned, we model all Android permissions. When we tried to narrow the permission set to a more relevant (security-wised) set, we faced worse results as will be further discussed later in this paper, in the analysis section.

We use four repositories of apps, as described in the following sections, to construct our training set and testing set. In each training set, i.e. malicious apps set and safe apps set, the number of samples is 350. Our testing dataset contains 4000 instances of Android apps. 2000 instances used as safe apps and the other 2000 instances used as malicious apps. In order to justify this amount of apps, we calculate the confidence interval of our results. As described above, the LibLinear library outputs the confidence level per classification. Each classification’s confidence level *X<sub>i</sub>* is independent and the classification results are normally distributed with the parameters mean *µ* and variance *σ<sup>2</sup>*, such that $\left( X_{1},\ldots,X_{n} \right)\sim N(\mu,\sigma)$ and the confidence interval is 
$$
(\overline{X} - \mu\ ,\ \overline{X} + \mu)
$$

Since the variance *σ<sup>2</sup>* is unknown, we use the standard variation *S<sup>2</sup>* instead with the sample mean $\overline{X}$ as follows:

$$
\overline{X} = (X_{1} + \ldots + X_{n})/n
$$

$$
S^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}{(X_{i} - \ \overline{X})}^{2}
$$

In the case of normal distribution, we discover the mean *µ* by the pivotal quantity function:

$$
T = \frac{\overline{X} - \mu}{S/\sqrt{n}}
$$

Shorten basic algebra calculations, we eventually build the confidence interval, using the *Student’s t-distribution* with *n - 1* degrees of freedom:

$$
(\overline{X} - t_{n - 1,\alpha/2}\frac{S}{\sqrt{n}}\ ,\ \overline{\ X} + t_{n - 1,\alpha/2}\frac{S}{\sqrt{n}})
$$

We calculate 95% confidence interval (*α = 0.95*), separately for malicious apps and safe apps, and we get:

Safe apps – (0.812912, 0.828297), *µ* = 0.820605

Malicious apps – (0.940685, 0.949048), *µ = 0.944866*

In both results the 95% confidence interval is very low hence we conclude that this amount of apps is satisfied to test and evaluate our results ahead. Later in section 7, we also show we achieve satisfied variations and diversity from this number of samples as we test the classifier stability for changes in the training set.

For review purposes, for each dataset there exists a file contains the apps and the permissions of each app.

## 6.3. Malicious Apps Dataset

We want to make sure this dataset has samples that are classified as malware. Hence we use the following repositories:

- Malware apps repository provided by Contagio Mobile \[34\]. Contagio Mobile is part of the Contagio initiative. Contagio is a collection of the latest malware samples, threats, observations, and analyses. It is an open security-researchers community.

- Malware apps repository provided by Virus Share \[35\]. VirusShare is a repository of malware samples that provides security researchers, incident responders, forensic analysts, and the morbidly curious access to samples of malicious code.

- Our own “dangerous-apps-permissions” generator. We used \[2, 7, 13\] to obtain a list of dangerous permissions and by running a simple script we can generate apps permissions groups with random number of random permissions (refer to sections 2 and 3 for extended explanation of what is considered as dangerous permission)

Regarding the latter, we use this generator in order to populate the dataset with more dangerous combinations. By doing so, we enrich the dataset with permissions that are most dangerous but they are not necessarily in common use, such as BRICK or INSTALL_PACKAGES. It is very common in classifier models to intervene with the dataset in order to spot certain cases which are not common in the real world. In extreme cases, the dataset may be fully synthetic. For example, models to predict nuclear experiments results. In our case, there are some permissions, as in the examples above, which are used rarely but we do want to spot these occurrences since those permissions are extremely dangerous and suspicious. Without adding the permissions manually, the prediction algorithm will treat them as unseen cases which may result in wrong classification.

Therefore, we built the malicious apps training set which consists of 95% apps from Contagio Mobile and VirusShare. The other 5% consists of generated samples from our dangerous app generator.

## 6.4. Safe Apps Dataset

For constructing the safe apps dataset we used apps from Google Play \[36\] only. In order to achieve as realistic as possible conditions, we included 270 top free and most popular apps on Google Play, for example, apps by leading vendors such as Facebook and Google, and very popular (gaming) apps such as Angry Birds or Candy Crush. Other 80 apps were picked randomly from our own database, built by a crawler we developed, which contains apps from Google Play, as described in section 3. In general, we assume that the majority of app vendors in Google Play have no malicious intentions such that apps in Google Play are consider as safe apps.

## 6.5. Testing the Algorithm

As well as in the apps for training, each app for testing purpose will be modeled to this form as follows:

$$
\left\{ y,x_{1},\ldots,x_{n} \right\}
$$

The only difference between training and testing sample modeling is the *y* value, which in testing sample represents unknown classification value.

We used apps from Google Play for app samples in the safe apps testing dataset. We generally assume that apps from Google’s official app market are considered at least safer than any other Android third-party market. As per the malicious apps testing dataset, we wanted to have a set that contains apps that have already spotted as malicious, thus we used apps from Virus Share. We used only Virus Share in this dataset since we used all our Contagio Mobile apps.

All apps we were using were randomly picked and there is no redundancy within or between datasets, i.e. an app instance may appear only once and only in one dataset. This will guarantee that we avoid the following situations:

1.  Where, for instance, a certain app appears as a “safe” app in the dataset for training and then the same app will appear again in the dataset for testing to be under examination. As you might guess, most likely that this app will be classified as a “safe” app.

2.  Where the same app appears twice in the same dataset it may cause one of the following:

    1.  If it is in the dataset for training, then the training won’t be effective, especially where the number of instances in the training dataset is low. As explained in the section 6.1, we want as rich and as plural dataset as we can get.

    2.  If it is in the dataset for testing, then this is intuitive. We will get the exact same result.

## 6.6. Set Permissions Threshold

There is a known issue regarding classification problems which simply caused by too few data. What “too few data” means? When there are very few permissions the sample does not carry enough information. In our case, the features are the permissions and when an app is lack of permissions then each presence of even a single permission is significant and directly affects the classifier’s outcome. For instance, let’s take one of the apps in the *safe* testing dataset. We denote this safe app as G<sub>1</sub>. The app G<sub>1</sub> has only one permission – *GET_TASKS*, which by itself probably can’t harm. Nevertheless, this permission is most likely to be used by malicious apps in a manner of spying after the device’s activities or even prevent from anti-malware scanners to run. As a result, the *GET_TASKS* permission has a negative score in the classifier. In case this is the only permission, the classifier predict this app as a malicious app. Therefore, the classifier fails in this case. The classifier just doesn’t have any other factor to test it against. The same phenomenon occurred in the malicious apps testing-set as well. We could easily have pointed out examples with exhibit a similar characteristics as in the *safe* examples.

In order to prevent misclassification, we set a threshold over the minimum number of permissions for an app under examination, otherwise the classifier returns *unknown*. By definition, as our classifier uses the permissions as its features hence bases its classification upon the permissions, it cannot perform as it should when there is not enough permissions. We assume that the minimum of 4 permissions are required for reliable classification. From technical point of view, the threshold can be easily configured. The algorithm can take the permissions threshold as an input parameter so the consumer can scale the classifier according to specific needs, confidence and trust.
