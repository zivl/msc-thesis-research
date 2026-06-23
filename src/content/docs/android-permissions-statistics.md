---
title: "3. Android Permissions Statistics"
---

We have built a crawler to get apps data from Google Play. We reached more than 15,000 apps, randomly, of all kinds and categories. Figure 4 describes the app category distribution in the collected data from Google Play.


<figure>
<img src="/msc-thesis-research/images/figure4-apps-distribution-categories.png" alt="Figure 4 - Distribution over Google Play Categories" />
<figcaption>Figure 4 - Distribution over Google Play Categories</figcaption>
</figure>


For each app we collect the following information: name, app identifier, creator, category, download count, price, type and the list of permissions required by the app. We use the data to analyze a lot of statistical information about the apps and the permissions used. After analyzing the data, we have better understanding of the permissions deviation and usage trends:

In Figure 5, you may see the histogram of the number of permissions requested by app. The majority of the apps require up to 5 permissions. It seem as a legitimate amount of permissions to require. We assume that apps from Google Play are considered as safe apps. By inspecting deeper we can see that the vast majority of apps use 0-3 permissions, thus we conclude that most of the vendors use least privileges needed to function.


<figure>
<img src="/msc-thesis-research/images/figure5-apps-permissions-histogram.png" alt="Figure 5 - Histogram ratio of how many apps require a certain amount of permissions" />
<figcaption>Figure 5 - Histogram ratio of how many apps require a certain amount of permissions</figcaption>
</figure>


Figure 6 shows histogram of the top 15 most required permissions. Pay attention that most of the permissions in Figure 6 are already appointed as dangerous permissions in previous section. Clearly, these 15 permission reveals the device’s data and the user’s private data \[27\]. Sensitive permissions, such as reading the phone state, reading a user’s address book, calendar, and location and send this data to remoted server. Exposing the user’s internet accounts, e.g. Google or Facebook accounts, to learn more about the user even browsing data and the ability to install other apps. All of the above are crucial to the user’s privacy and information integrity.


<figure>
<img src="/msc-thesis-research/images/figure6-top15-permissions.png" alt="Figure 6 - Top 15 Most Required Permissions" />
<figcaption>Figure 6 - Top 15 Most Required Permissions</figcaption>
</figure>


The Mobile Security Review 2012 report \[21\] states the top 30 most dangerous permissions. From their list, we randomly picked 10 permissions and watched the usage of those permissions. The usage results are shown in Figure 7.


<figure>
<img src="/msc-thesis-research/images/figure7-dangerous-permissions.png" alt="Figure 7 - Dangerous Permissions Usage" />
<figcaption>Figure 7 - Dangerous Permissions Usage</figcaption>
</figure>


There is a large intersection between the “most-used” permissions and the “most-dangerous” permissions. We can simply conclude that Android users are exposed to privacy violation and data leakage, even if caused by the developer innocence or negligence.

A cause of concern is the fact that many of the common requested permissions are invasive permissions and grant the app access to private data and maybe sensitive business data – in the case of corporate users. A rapidly growing number of employees are using personal mobile devices to connect to their employers’ networks. While this *bring your own device* (BYOD) trend is popular with employees and businesses, it has a major downside: The personal devices accessing business-critical data enable a huge number of malicious and unauthorized apps to access enterprise networks. These apps pose an enormous security risk. For example, a spyware app that has access to address book can easily steel information about business contacts and clients’ information. Another example: a malicious app that has access to the device file system, where the employee saves marketing or engineering data. In both examples, sensitive data may be stolen without the user even notice that malicious activity. According to Bit9 Report 2012 \[22\], more than 71% of employers allow employee-owned devices to connect to their network.

A dominant permission in Figures 6 and 7 is the *INTERNET* permission which grants internet access. Currently, according to our database, 79% of the apps are using the *INTERNET* permission. According to Federal Trade Commission Report \[49\], in 2012 more than 80% of the apps use the *INTERNET* permission compared to 62% in previous year and this number is on the rise. Digging a little bit more in this specific permission statistics, Figure 6 shows the *INTERNET* permission distribution among app categories. The *INTERNET* access permission is very common and not precisely related to a certain category or functionality.

Note: not all of Google Play categories are seen in Figure 7 due to space formatting of the document. To overcome the spacing issue, some of the closely related categories were joined, e.g. Games & Puzzles; News, Books & Magazines.


<figure>
<img src="/msc-thesis-research/images/figure7-internet-permission.png" alt="Figure 7 - INTERNET Permission Usage" />
<figcaption>Figure 7 - INTERNET Permission Usage</figcaption>
</figure>


We would like to clarify that the internet permission by itself is not so dangerous. It is a legitimate permission in which many apps need an internet connection to perform and function as designed. On the other hand, internet access is dangerous when combined with other permissions such as mentioned above, cause to leakage of information whether accidentally or intentionally. In many apps, the communication transmitted over the internet is not encrypted, e.g. WhatsApp Messenger. In such cases, a Man in the Middle (MITM) might intercept such transitions and benefit from the revealed data, also known as a MITM attack. In other cases personal data is transmitted to 3<sup>rd</sup> party advertisers.

The real concern becomes a threat when a combination of a certain group of permissions together with internet access may violate the user’s privacy, expose sensitive data and cause irreversible damage. Not only personal information data can be exposed to the world, but with the right combination we can see spying and malicious apps that can easily abuse the user without him being aware of the threat. Let’s take a spyware app which pretended to be an official Swiss banking app \[34\]. This spyware app requires the following permissions:

- RECEIVE_BOOT_COMPLETED – automatically start at boot

- INTERNET – full Internet access

- ACCESS_NETWORK_STATE – view network status

- ACCESS_COARSE_LOCATION – coarse (network-based) location

- RECEIVE_SMS – receive SMS

- READ_PHONE_STATE – read phone state and identity

- READ_SMS – read SMS or MMS

The spyware activity is activated immediately after installation. It sends text and multimedia messages to remote machine without the user intervention. In case the user reboots the device, it immediately starts again to keep track after any text and multimedia message of the spied user. The entire personal information comes with the location of the user such that the spying party probably gets this supplementary information with every SMS/MMS.

By observing these findings and in light of Android Security, it is well clear that a user-consent permission-model fails in this case to protect the average Android user. Furthermore, it exposes the careless user to malicious and harmful apps by granting access to sensitive data. It’s an easy world to mobile attackers and fraud makers in Android. Attackers don’t have to break anything or hack their way in – they just step in the opened door which the user opens and welcomes them into his device.
