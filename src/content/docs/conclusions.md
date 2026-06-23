---
title: "8. Conclusions and Future Work"
---

In this paper we showed that by using machine-learning based classifier, we can learn a lot about a certain app and classify ahead of installation whether an app is dangerous or not. While we are aiming to spot malicious apps, we successfully classified malicious apps with over 90% success rate in all tests. We created a robust and accurate classifier to identify malicious apps. Our classifier works fast and capable of classifying an app in less than 2ms! On the other hand, for all our test runs we consistently see the same problematic issue with safe apps classifications. We believe that future work should focus on several areas: safe apps training dataset, other set of permissions to be modeled, another mobile app features to be modeled and using more classification tools.

As discussed in previous sections, we assume we picked up wrong apps to be in the safe apps training dataset. Hence, part of the future work is to replace that training dataset for the safe apps with suitable one. To remind, most of our apps in the safe apps training set is constructed by top and most popular apps on Google Play (at the time it was collected, during October 2013). Perhaps many of them included permissions which are also associated with malicious apps? Perhaps a few even contain the exact permission combination set of a malicious app? Those kind of assumptions should be considered when putting safe apps in the training set. Retrospectively, we are now aware of it.

Another future work action item should focus on the set of permissions to be modeled. This action is tightly coupled with the pervious suggestion of rebuilding the training set. Again, eliminating permissions has to be done very cautiously and should be considered along with the permissions’ security value. We suggest to concentrate on removing permissions which their distribution among safe apps and malicious apps is almost the same and therefore these permissions do not contribute any data to the classifier. For example, the *VIBRATION* permission. An android app that willing to engage the device vibration feature has to declare this permission. One can decide not to model this permission for the following reasons:

- It is certainly not a security-manner permission that may cause to abuse of the device or the user of any kind.

- The *VIBRATION* permission is very commonly and equally used in both safe and malicious apps. Hence, it is not a feature to characterize a safe/malicious app.

- Unlike other permissions, the user may turn off the vibration.

Furthermore, in future work, the app features to be modeled might include other features as well and not count only on the permissions required by the app. For example, Android app’s manifest file contains other data than permissions. Data such as event-listeners, background services and activities is also located in the Android manifest file and it is worth to try to explore if and how malicious apps are using it compared to safe apps. If a difference can be found then it can be used as another app feature.

In parallel, additional machine-learning tools can be used to try and find another, better, classifier or algorithm to be used to identify malicious apps using the permissions as features. For instance, WEKA is an open-source collection of algorithms for machine learning, big-data and data mining tasks. The WEKA library contains tools for data pre-processing, classification, regression, clustering, association rules, and visualization. It is also well-suited for developing new machine learning schemes. We believe that migrating our data into tools such as WEKA may be useful and contribute to better understanding the patterns of malicious apps in comparison to safe apps.

Despite this work’s results, modeling the Android’s permissions into a machine-learning algorithm has never been done before (at the time of writing).Our approach proves that most of Android malicious exploitations can be prevented and mitigated only by taking a look at the permissions required by a certain app.

For comparison, X.Jiang et al. \[29\] examined the performance of malware detection by big 4 anti-virus companies. Their results show that the best case detects 79.6% of infected apps while the worst case detects only 20.2%. To relate other works, Shabtai et al. \[38\] also used Logistic Regression techniques to detect malware apps. Their results ranged 31.1% - 81.6%. So far, the only work we have found that has the closest results to ours is X.Jiang et al. \[37\]. In their work, they have also used the Contagio Mobile Malware apps repository \[34\], though, their amount of apps under test was pretty low, their system reports 122 of 133 infected apps that were tested (~90%). They had a performance overhead problem as well.

Figure 12 summarizes the comparison of our results to the results of previous suggested solutions, as well as anti-virus companies, in detecting malicious apps.


<figure>
<img src="/msc-thesis-research/images/figure12-comparing-solutions.png" alt="Figure 12 - Comparing Results of Different Solutions" />
<figcaption>Figure 12 - Comparing Results of Different Solutions</figcaption>
</figure>


Our implementation is easy to deploy and platform independent. The entire code is written in Java, hence, can be deployed on any platform. Since it is very lightweight, less than 300K, it can be installed on the device itself, whether it’s a mobile device or any other wearable technology that runs Android. Another option could be to deploy this mechanism on a remote machine or even in the cloud and provide this solution via software as a service (SAAS). In this way, the device just sends a request with the desired app to install and immediately gets response with the classification.

An average user, who has such classification mechanism, could easily use it to assist while installing an app on his mobile device. Our proposed solution is easy to maintain. It has optional configurations that can be changed according to the consumer needs and it works as fast as 2ms per app instance. We believe this work highly contribute to the mobile security field by implementing our idea as a proof of concept to find a great and generic solution to Android’s permission mechanism vulnerability.

**References**

1.  Berger, B. J., Bunke, M., & Sohr, K. (2011, October). An Android Security Case Study with Bauhaus. In Reverse Engineering (WCRE), 2011 18th Working Conference on (pp. 179-183). IEEE.

2.  Chia, P. H., Yamamoto, Y., & Asokan, N. (2012, April). Is this app safe?: a large scale study on application permissions and risk signals. In Proceedings of the 21st international conference on World Wide Web (pp. 311-320). ACM.

3.  Nunez, G. (2011). Party pooper: Third-party libraries in android. Electrical Engineering and Computer Sciences University of California at Berkeley. <span class="mark"></span>

4.  Fan, R. E., Chang, K. W., Hsieh, C. J., Wang, X. R., & Lin, C. J. (2008). LIBLINEAR: A library for large linear classification. The Journal of Machine Learning Research, 9, 1871-1874.

5.  Le Thanh, H. (2013). Analysis of Malware Families on Android Mobiles: Detection Characteristics Recognizable by Ordinary Phone Users and How to Fix It. Journal of Information Security, 4, 213.

6.  Boutet, J., & Homsher, L. (2010). Malicious Android Applications: Risks and Exploitation. SANS Institute, 22.

7.  Felt, A. P., & Wagner, D. (2011). Phishing on mobile devices.

8.  Enck, W., Ongtang, M., & McDaniel, P. (2009, November). On lightweight mobile phone application certification. In Proceedings of the 16th ACM conference on Computer and communications security (pp. 235-245). ACM.

9.  Wei, X., Gomez, L., Neamtiu, I., & Faloutsos, M. (2012, December). Permission evolution in the android ecosystem. In Proceedings of the 28th Annual Computer Security Applications Conference (pp. 31-40). ACM.

10. Felt, A. P., Wang, H. J., Moshchuk, A., Hanna, S., & Chin, E. (2011, August). Permission Re-Delegation: Attacks and Defenses. In USENIX Security Symposium.

11. Enck, W., Gilbert, P., Chun, B. G., Cox, L. P., Jung, J., McDaniel, P., & Sheth, A. N. (2014). TaintDroid: an information flow tracking system for real-time privacy monitoring on smartphones. Communications of the ACM, 57(3), 99-106.

12. Barrera, D., Kayacik, H. G., van Oorschot, P. C., & Somayaji, A. (2010, October). A methodology for empirical analysis of permission-based security models and its application to android. In Proceedings of the 17th ACM conference on Computer and communications security (pp. 73-84). ACM.

13. Felt, A. P., Greenwood, K., & Wagner, D. (2011, June). The effectiveness of application permissions. In Proceedings of the 2nd USENIX conference on Web application development (pp. 7-7). USENIX Association.

14. Magat, W. A., Viscusi, W. K., & Huber, J. (1988). Consumer processing of hazard warning information. Journal of Risk and Uncertainty, 1(2), 201-232.

15. Stewart, D. W., & Martin, I. M. (1994). Intended and unintended consequences of warning messages: A review and synthesis of empirical research. Journal of Public Policy & Marketing, 1-19.

16. Tam, J., Reeder, R. W., & Schechter, S. (2010). I’m Allowing What? Disclosing the authority applications demand of users as a condition of installation.

17. Zhang, M., & Yin, H. Transforming and Taming Privacy-Breaching Android Applications.

18. Hornyack, P., Han, S., Jung, J., Schechter, S., & Wetherall, D. (2011, October). These aren't the droids you're looking for: retrofitting android to protect data from imperious applications. In Proceedings of the 18th ACM conference on Computer and communications security (pp. 639-652). ACM.

19. Ongtang, M., McLaughlin, S., Enck, W., & McDaniel, P. (2012). Semantically rich application‐centric security in Android. Security and Communication Networks, 5(6), 658-673.

20. Lookout Mobile Threat Report, August 2011. Lookout Mobile Security. http://mylookout.com

21. Mobile Security Review, August 2012. AV Comparatives Organization. http://av-comparatives.com

22. Pausing Google Play: More Than 100,000 Android Apps May Pose Security Risks. Bit9 Report. (2012). http://bit9.com

23. New Platforms and Changing Threats. Sophos Security Threat Report 2013. Sophos LTD. http://sophos.com

24. Boyd, C. R., Tolson, M. A., & Copes, W. S. (1987). Evaluating trauma care: the TRISS method. Journal of Trauma-Injury, Infection, and Critical Care, 27(4), 370-378.

25. Logistic regression analysis for experimental determination of forming limit diagrams. M. Stranoa, B.M. Colosimob a Università di Cassino, Dip. Ingegneria Industriale, Italy, Politecnico di Milano, Dip. Meccanica, via Bonardi 9, Milano, Italy

26. Palei, S. K., & Das, S. K. (2009). Logistic regression model for prediction of roof fall risks in bord and pillar workings in coal mines: an approach. Safety science, 47(1), 88-96.

27. Google’s Official Android Developers Web Page. Google Inc. http://developers.android.com

28. Bugiel, S., Davi, L., Dmitrienko, A., Fischer, T., Sadeghi, A. R., & Shastry, B. (2012, February). Towards Taming Privilege-Escalation Attacks on Android. In NDSS.

29. Zhou, Y., & Jiang, X. (2012, May). Dissecting android malware: Characterization and evolution. In Security and Privacy (SP), 2012 IEEE Symposium on (pp. 95-109). IEEE.

30. When Malware Goes Mobile: Causes, Outcomes and Cures. Vanja Svajcer, Principal Researcher. SophosLabs. (2012). Sophos Ltd. http://sophos.com

31. State of Mobile Security. (2012). Lookout Mobile Security. https://www.lookout.com/resources/reports/state-of-mobile-security-2012

32. AVG Threat Labs. AVG. (Online Service). http://www.avgthreatlabs.com

33. Android Malware - Past, Present, and Future. (2011). McAfee.

34. Contagio Mobile. (Online Service). http://contagiominidump.blogspot.com

35. Virus Share. (Online Service). http://virusshare.com/

36. Google Play. Google Inc. Official App Market. (Online Service). <http://play.google>.com.

37. Grace, M., Zhou, Y., Zhang, Q., Zou, S., & Jiang, X. (2012, June). Riskranker: scalable and accurate zero-day android malware detection. In Proceedings of the 10th international conference on Mobile systems, applications, and services (pp. 281-294). ACM.

38. Shabtai, A., Kanonov, U., Elovici, Y., Glezer, C., & Weiss, Y. (2012). “Andromaly”: a behavioral malware detection framework for android devices. Journal of Intelligent Information Systems, 38(1), 161-190.

39. Android trickery. http://c-skills.blogspot.com/2010/07/android-trickery.html.

40. First SMS Trojan detected for smartphones running Android. Kaspersky Lab. (2010). http://www.kaspersky.com/about/news/virus/2010/First_SMS_Trojan_detected_for_smartphones_running_Android

41. Duggan, M. (2012). Cell phone activities 2012. Cell.

42. Alan Agresti. Barbara Finlay (1998). Statistical Methods for the Social Sciences, 4<sup>th</sup> Edition (Chapter 15). *Journal of the American Statistical Association, 93*, p. 844.

43. Kim, E., Kim, W., & Lee, Y. (2003). Combination of multiple classifiers for the customer's purchase behavior prediction. Decision Support Systems, 34(2), 167-175.

44. Katz, J. N., & King, G. (1999). A statistical model for multiparty electoral data. American Political Science Review, 15-32.

45. Zhu, H., Cao, H., Chen, E., Xiong, H., & Tian, J. (2012, October). Exploiting enriched contextual information for mobile app classification. In *Proceedings of the 21st ACM international conference on Information and knowledge management* (pp. 1617-1621). ACM.

46. Lookout Mobile Security. Bad News. https://www.lookout.com/resources/top-threats/bad-news

47. National Security Agency (NSA), Research Department. Security-Enhanced Linux. https://www.nsa.gov/research/selinux/

48. Smalley, S., & Craig, R. (2013, February). Security Enhanced (SE) Android: Bringing Flexible MAC to Android. In *NDSS*.

49. Federal Trade Commission (FTC). (2012). Mobile Apps for Kids – FTC Staff Report. http://www.ftc.gov

50. WEKA. (1997). Machine Learning Group at the University of Waikato http://www.cs.waikato.ac.nz/ml/weka/
