---
title: "4. Related Work"
---

With the growing popularity of Android, there have been a number of publications on Android security and its permission system. Most of them are informative or theoretic and only few suggest a practical ideas or a solution. Prior research efforts have been made to improve the privacy leakage problem. These works can be divided into the following categories:

1.  Detecting malicious characteristics proactively or at pre-installation time.

2.  Tracking malicious behavior at runtime.

3.  Obscuring personal data at runtime.

## 4.1. Proactive Detection

In the first category, there are works such as Enck et al. \[8\], who proposed a certification system to help identifying Android apps that request a suspicious permission combination using a set of predefined rules. The proposed solution, Kirin, is a security service for Android, which performs lightweight certification of applications to mitigate malware at install time. Kirin certification uses security rules, which are templates designed to conservatively match undesirable properties in security configuration bundled with applications. They use a variant of security requirements engineering techniques to perform an in-depth security analysis of Android to produce a set of rules that match malware characteristics.

Enck et al. \[8\], define the Kirin Security Language (KSL) to construct a set of rules to be tested while installing an app on the device. A rule indicates combinations of permission labels and action strings that should not be used by third-party applications. Each rule begins with the keyword “restrict”. The remainder of the rule is a conjunction sets of permissions and action strings received. Each set is denoted as either “permission” or “receive”, respectively.

Figure 8 describes the KSL in a BNF notation:


<figure>
<img src="/msc-thesis-research/images/figure8-ksl-syntax.png" alt="Figure 8 - KSL Syntax and Semantics" style="width:480px" />
<figcaption>Figure 8 - KSL Syntax and Semantics</figcaption>
</figure>


Let’s see a few usage examples:

1.  A rule to restrict the “SEND_SMS” permission would be:

*“restrict permission \[‘SEND_SMS’\]”*

2.  In Android the user may define default app to handle an incoming call event.\
    A rule to restrict the “SET_PREFFERED_APPLICATIONS” permission that receive “CALL” action string would be:

> “*restrict permission \[‘SET_PREFFERED_APPLICATION’\] and receive \[‘CALL’\]*”

Their algorithm takes the app’s manifest file as input and simply tests the rules against an app’s permissions and the list of action string used by *Activities*, *Services* and *Broadcast* *Receivers*. Recall, each rule define a forbidden pattern, an undesired functionality or behavior. If a certain app has passed all the defined list of rules then the algorithm returns void (success). That means that the tested app is not breaking any of the defined rules and compliance with a desired functionality. Otherwise, in case where the tested app failed in one rule (or more), the algorithm returns the set of rules that failed the algorithm, i.e. the rules that were violated.

To run their proof-of-concept, they define a following 9 rules-set:

1.  *An application must not have the* SET*\_*DEBUG*\_*APP *permission label.  *

2.  *An application must not have* PHONE*\_*STATE*,* RECORD*\_*AUDIO*, and* INTERNET *permission labels.*

3.  *An application must not have* PROCESS*\_*OUTGOING*\_*CALL*,* RECORD*\_*AUDIO*, and* INTERNET *permission labels.*

4.  *An application must not have* ACCESS*\_*FINE*\_*LOCATION*,* INTERNET*, and* RECEIVE*\_*BOOT*\_*COMPLETE *permission labels.*

5.  *An application must not have* ACCESS*\_*COARSE*\_*LOCATION*,* INTERNET*, and* RECEIVE*\_*BOOT*\_*COMPLETE *permission labels. *

6.  *An application must not have* RECEIVE*\_*SMS *and* WRITE*\_*SMS *permission labels. *

7.  *An application must not have* SEND*\_*SMS *and* WRITE*\_*SMS *permission labels. *

8.  *An application must not have* INSTALL*\_*SHORTCUT *and* UNINSTALL*\_*SHORTCUT *permission labels.*

9.  *An application must not have the* SET*\_*PREFERRED*\_*APPLICATION *permission label and receive Intents for the* CALL *action string.*

Explanation of the above rules:

- Rule 1 ensures third party applications do not have the SET_DEBUG_APP permission. The SET\_ DEBUG_APP permission allows an application to turn on debugging for another application.

- Rules 2 and 3 protect against the voice call eavesdropper.

- Rules 4 and 5 protect against a location tracker.

- Rules 6 and 7 consider malware’s interaction with SMS. Rule 6 protects against malware hiding or otherwise tampering with incoming SMS messages. Rule 7 mitigates mobile bots sending SMS spam. Similar to Rule 6, this rule ensures the malware cannot remove traces of its activity.

- Rule 8 makes use of the duality of some permission labels. Android defines separate permissions for installing and uninstalling shortcuts on the phone’s home screen. This rule ensures that a third-party application cannot have both. If an application has both, it can redirect the shortcuts for frequently used applications to a malicious one. For instance, the shortcut for the web browser could be redirected to an identically appearing application that harvests passwords.

- Rule 9 provides an example of a rule considering both a permission and an action string. This specific rule prevents malware from replacing the default voice call dialer application without the user’s knowledge.

Of course the rules above may be changed and can be configured according to the stakeholder’s will.

However, we find the following limitations critical and should be considered: A rule-based system requires resources of security experts, such personals who understand the threats and risks and will know how to model it into Kirin. The definition of assets/rules may vary and maybe undertaken by layman or unprofessional personnel. It also requires understanding of the Kirin Security Language (KSL) which could be prohibitive. Defining rules of forbidden pattern could be very restricted and not flexible for changing variables in the real world and also vulnerable to zero-day threats.

A work regarding proactively assessing the potential risk of apps is the RiskRanker by X. Jiang et al. \[37\]. They claim to have the ability to spot Android malware apps, while not relying on any other malware samples and signatures. The results of apps testing are divided into three categories of potential risk:

- High-risk – apps that exploit platform-level software vulnerabilities to compromise the phone integrity without proper authorization from users.

- Medium-risk – apps that do not exploit software vulnerabilities, but can cause users financial loss or disclose their sensitive information.

- Low-risk – apps that are similar, but milder. Such apps may collect device-specific or generic, generally readily available personal information.

Note: we focus on medium/low risks as our work does not focus on platform-level vulnerabilities.

The RiskRanker assessment process performs a two-order risk analysis. In the first-order risk analysis, it aims to directly identify apps in high/medium-risk categories. The modules in the first order handle non-obfuscated apps by evaluating the risks in a straightforward manner, i.e. static code analysis. A behavior that is found to be suspicious for malware activity are apps that could result in the user being charged money surreptitiously or that upload private information to a remote server. Android has a group of permissions named android.permission-group.COST_MONEY, which is defined as “permissions that can be used to make the user spend money without their direct involvement.” \[27\]. Recall, these features can be used to construct malware such as SMS Trojans, which send text messages to premium phone numbers that result in charges being placed on the user’s phone bill.

Nevertheless, these same features do have legitimate uses, typically in the form of instant-messaging, reminder, or social-networking apps. Hence, to overcome and distinguish between such legitimate and malicious uses of potentially costly functions, they leverage the associated semantics defined in Android. Specifically, mobile apps make extensive use of callbacks triggered by user interaction. For example, when a user presses a “send” button on the screen, it ultimately will lead to execute some onClick(...) callback function. Unlike malware functionality, the user triggered the desired function by himself to send a message. Malware that intends to charge the user without their knowledge is unlikely to do so via such a callback handler. Similarly, malware that transmits sensitive data is unlikely to prompt the user before doing so. Assuming this kind of behavior, the RiskRanker static code analysis looks for code snippets that cost the user money without being called by callback handler functions.

In the second-order risk analysis, the modules performs further investigation to uncover suspicious app behavior. There modules capture certain behaviors, e.g. encryption and dynamic code loading. Such behaviors, in themselves, are not of concern, but in conjunction with others may form malicious patterns and be instrumental to detect stealthy malware. To recognize such behaviors, the modules collect information concerning existence and location of child processes such as background dynamic code loading as well as related execution path(s), usage of Java encryption and decryption tools, and native code execution.

In X. Jiang et al. \[37\], along their testing of apps from multiple Android markets, they have also tested the RiskRanker with malware samples that have been taken from the public Contagio Mobile Dump repository \[34\]. Unfortunately, they have tested only 133 malicious apps. They present a high success ratio of ~90%, which are 121 apps that were detected as malicious or dangerous apps. However, they didn’t test RiskRanker on safe apps, hence, there is no false-positive ratio to understand whether the RiskRanker is realistic solution. Nevertheless, they clearly state that the apps that have failed in the detection were out of the RiskRanker analysis scope, e.g. social engineering attacks – apps that pretend to be something else like the FakeNetflix app which steals Netflix user credentials \[37\]. That means, more rules that has to be covered, coded and tested. This leads us to discuss the RiskRanker limitations and disadvantages.

To begin with, root-exploit detection scheme depends on signatures, which obviously implies that it can detect only known exploits and may also miss encrypted or obfuscated exploits. Moreover, X. Jiang et al. \[37\] claims to have a tool which is not based on malware samples or signatures but is actually relying on known OS exploitations.\
The RiskRanker also considers the javax.crypto libraries for convenient encryption detection. Nothing prevents an attacker from implementing their own in-app encryption or decryption scheme. Similarly, instead of packaging their native code or child apps in the assets or resource directories, such code can be downloaded from the Internet or stored as raw data contained in a constant array.

## 4.2. Runtime Tracking

In this category, Shabtai et al. \[38\] introduce a system that continuously monitors various features and events obtained from the mobile device. The system then applies machine-learning-based detectors to classify the collected data as benign or malicious. When a threat is spotted, a proper notification is displayed to the user. The user is presented with a set of automatic or manual actions that can be undertaken to mitigate the threat. Predefined automatic actions include among others: uninstalling an application, killing a process, disconnecting all radios, encrypting data, changing firewall policies and more. A manual action can be uninstalling an application subject to user consent.

In order to test and evaluate their system, they have used multiple classifiers. One of the classifiers being used is a logistic regression classifier. Their training set vectors are based on operating the device and monitoring its activity. While training their benign behavior data they operate the device normally to reflect benign behavior. While training their malicious behavior they execute some malicious and abnormal operations. Such operations could be transmitting a certain amount of data, exceptional CPU consumption, a certain amount of running process, etc.

They have performed a few experiments to evaluate the ability to differentiate between benign and malicious apps. Among those experiments we will discuss experiment no. 2. In this experiment the testing set did not include apps from the training set. Their success ratio of spotting malware was 81.6% which was the highest successful results amongst their 4 different experiments.

Although Shabtai et al. \[38\] are, in a way, closer to our work in a sense of using machine-learning techniques to distinguish dangerous and safe apps, there are some points that raise questions. The first issue we would like to discuss is the fact that they have developed the malicious apps by themselves. In addition, they used very small number of apps for training and testing. To be precise, they have used 40 benign apps and 4 malicious apps. They reports on hundreds of features vectors extracted out of those apps. On the other hand, the scope of those apps is limited to the specific apps functionality. Hence, the feature vectors would be limited to a certain scope as well. It might be that many of those vectors will be redundant.

For a real working system on a user’s device, there will be a concern of the system’s overhead to the operating system. Even though they claim to have a lightweight system, it is still running at the background to perform real time monitoring on the device. This kind of background service could affect the CPU by consuming more CPU time for calculations and background operations. It affects the device’s memory since it’s always on, running in the background. Consequently, it affects battery performance. It is likely to assume impact on the user experience as each user action would be performed with an overhead due to registering, logging, auditing and metering that action with their system.

## 4.3. Runtime Obscurity

There are works that focuses on the user’s private data and information. Enck et al. \[11\] presents the TaintDroid – a real-time and dynamic taint tracking and analysis system. Capable of simultaneously tracking multiple sources of sensitive data. The term “taint” stands for a methodology of tracking information and labeling it. The TaintDroid system aims to detect when sensitive data is being transferred out via untrusted app. Also, the TaintDroid aims to facilitate the analysis of apps by mobile device users or external security services. The way TaintDroid act is as follows: it automatically labels (taints) data from privacy-sensitive sources and transitively applies labels as sensitive data propagates through program variables, files and inter-process messages. When tainted data are transmitted over the network, or otherwise leave the system, TaintDroid logs the data’s labels, the app responsible for transmitting the data, and the data’s destination. This way, one could have a greater insight into what mobile apps are doing and potentially identify misbehaving apps. By extending the Android operating system, they had the ability to taint data such as the location, microphone, camera, contacts, SMS messages, SIM and other device identifiers.

In order to evaluate TaintDroid, they have used 30 popular apps. For each app, they manually exercised the functionality offered by the app. They recorded the system logs including detailed tainted information from TaintDroid. Only 30 apps were tested. While testing, Enck et al. \[11\] claim to have only 14% overhead over the operating system. They mention that “interactive” apps can be monitored with negligible latency.

Though, they did not mention what is considered as “interactive”? Is interactive app is one that shows some kind of a “loading” icon spinning? Is it means that the user keeps waiting a few more milliseconds? If so, how many? They measured a few actions with the device and timed those actions. Among those measured actions was taking a picture. Taking a picture while TaintDroid is running in the background took almost twice as before. The mobile device’s camera has become one the most popular features being used. Hence, it is likely to assume that after a few time using the camera app, users will notice the overhead and might remove the TaintDroid extension from their devices.

Another limitation of TaintDroid is that it cannot differentiate third-party apps activity from the operating system activity. It causes significant false positives when the tracked information contains configuration identifiers. For example, the IMSI numeric string consists of a Mobile Country Code (MCC), Mobile Network Code (MNC), and Mobile Station Identifier Number (MSIN), which are all tainted together. Android uses the MCC and MNC extensively as configuration parameters when communicating other data. This causes all information in a parcel to become tainted, eventually resulting in an explosion of tainted information. By tainting all this data together, it reduces the amount of information to taint, but makes it harder to track which app used what.

Although the target of TaintDroid is not specifically spotting malware or any other malicious behavior, it could be cleverer to test the system on real malicious apps that do abuse the user’s privacy data and information. Sometimes, malware app developers use workarounds to bypass such mechanisms (detailed above) to avoid detection. It would be interesting to see if TaintDroid can also detect usage of those apps as well. In this context, TaintDroid only provides the reordered/logged information. It seems to be lacking learning or logic mechanism to take actions or advise for actions for the device’s user.

To address the later limitation of TaintDroid\[11\], Hornyack et al. \[18\] proposed AppFence to enforce information flow policies at runtime. With support of TaintDroid \[11\], AppFence keeps track of the propagation of private information. Once privacy leakage is detected, AppFence either blocks the leakage at the sink or shuffle the information from the source. Though effective in terms of blocking privacy leakage, AppFence has several limitations:

1)  Due to the taint tracking on every single Dalvik bytecode execution, AppFence incurs significant performance overhead

2)  As firmware modification is required, deploying it on large amount of Android devices can be challenging.

In order to overcome those limitations, M. Zhang et al. \[17\] proposed a bytecode transformation approach to effectively defeating privacy leakage. Given an unknown app, they first perform application-wide static dataflow analysis to identify potential taint propagation segments for information leakage. Then to keep track of taint propagation and prevent the actual information leakage, they insert bytecode instructions along the taint propagation chops. To further improve performance, they apply a series of optimization methods to remove redundant and unnecessary instrumentation bytecode.

This solution maybe better but there are limitations and disadvantages that are still remains. For example, changing the bytecode of an app may result in app crashes and flaw of functionality.

Same as with AppFence \[18\], an app that is aware of \[17, 18\]-like mechanisms can detect the presence of filtration blocking. For example, an app could open two independent sockets, transmit tainted data over only one of those sockets and untainted data over the other socket, and have the server report back what it received. Similarly, shadow data may also not be convincing enough to fool an app. Apps that detect the presence of privacy controls could inform users that they refuse to provide user-desired functionality until these controls have been deactivated.

In our work we overcome those disadvantages by implementing a different approach of machine learning over the apps’ permissions and their potential of harming and exposing the user’s privacy data. No need for extra processing such as code analysis, re-writes of the app bytecode and other such actions.
