---
title: "1. Introduction"
---

As our digital world is rapidly changing and mobile devices become a main platform in our daily private and business tasks, people are still not taking into account many threats they are exposed to. Many mobile users do not perceive that their device is no longer “just a smart-phone” – but it is a small and powerful computer which has the same capabilities of any other desktop computer. Moreover, mobile devices are equipped with GPS receiver, gyro-meter, always online and many more sensors to enhance the interaction with the user. All the above are feature that has changed our world, yet include threats and risks that should be taken into consideration.

In the second half of 2013, Google Play – Google’s official app store for the Android platform reached over 1M apps. Such huge amount of apps with millions of users around the world is a greenhouse for many malicious intentions and attacks. Malicious apps have been spotted on Google Play already, as well as in other 3<sup>rd</sup> party app stores for the Android platform. A user who runs on a malicious app on his device is in risk of financial fraud, privacy violations and being taken advantage of by a botnet controllers, sometimes, all at the same time.

According to Lookout Mobile Security report in August 2011 \[20\], Android users are two and a half times more likely to encounter malware today than 6 months earlier that year. An estimated 0.5M – 1M people were affected by Android malware in the first half of 2011. Android apps infected with malware went from 80 apps in January to over 400 apps cumulative in June 2011, as seen in Figure 1. Attackers are deploying a variety of increasingly sophisticated techniques to take control of the phone, personal data, and money. Additionally, malware writers are using new distribution techniques, such as malvertising (malwares by clicking on ads) and upgrade attacks.


<figure>
<img src="/msc-thesis-research/images/figure1-android-infected-apps.png" alt="Figure 1 - Growth of Android Infected Apps." />
<figcaption>Figure 1 - Growth of Android Infected Apps.</figcaption>
</figure>


With those numbers on the rise, the reality today is even more disturbing. Sophos report \[23\] points that in 2012 attackers extend their reach to more platforms, respond to new security research findings more rapidly, and leverage zero-day exploits more effectively. The prolific nature of threats, especially on the Android platform, continues to increase. Sophos et al. \[30\] observed 81 times more Android malware than in 2010 – an 8,000% leap. In 2012 \[30\] have already seen 41 times more malware than in all of 2011 – a growth rate of nearly 4,100%. Furthermore, in a few countries the Android *threat-exposure -rate* reaches higher scores of other platforms such as PCs, as seen in Figure 2.

Why is this happening? Mobile malware is a profitable business. The mobile malware industry has matured and become a viable business model for attackers. One type of malware designed for profit — Toll Fraud — is the most prevalent type of malware. Primarily impacting Eastern Europe and Russia, Toll Fraud has successfully stolen millions from consumers \[31\].


<figure>
<img src="/msc-thesis-research/images/figure2-malware-ter.png" alt="Figure 2 – Malware TER Scores of Android vs. PC." />
<figcaption>Figure 2 – Malware TER Scores of Android vs. PC.</figcaption>
</figure>


Applications written for Android can be distributed to end users directly through a developer’s web site, or through the Google Play. Google Play is Google’s official app market and offers a central location where developers can submit their applications and, with minimal interaction from Google, reach end user devices. This differs from the Apple’s App Store where all applications must pass through a vetting process (performed by Apple in a closed manner) before reaching consumers. Until recently, Google Play apps were not always inspected upon submission, allowing malicious application developers to quickly get their applications onto end user devices. It is important to mention that in terms of user behavior, people who download apps outside of trusted sources like Google Play have a higher likelihood of encountering malware since there is no supervision at all.

According to Sophos et al. \[30\], in 2011 alone, Google removed more than 100 malicious applications from its app store. Google discovered 50 applications infected by a single piece of malware known as Droid Dream, which had the capability to compromise personal data. However, Google hasn’t always acted in a timely manner to prevent infections. Users downloaded one harmful app more than 260,000 times before the company removed it.\
In the first half of 2013, Google removed 32 apps from Google Play over malware concerns. In total, according to Google Play statistics, the combined affected (with malware) applications have been downloaded between 2,000,000 – 9,000,000 times \[46\]. Those removals, by the way, were removed after user complains and requests by mobile application security companies and the open community. There were not spotted by Google in the first place.

As Google sees this growing threat as well, Google has decided to take action and recently initiated with a number of processes and solutions to mitigate the phenomenon. Google has released a number of new features recently that improve the security of Android as a whole. The latest versions of the Android operating system have implemented progressively stricter forms of:

- Address Space Layout Randomization (ASLR) – helps protect against some security attacks by making it more difficult for an attacker to predict target memory addresses of key data areas in a process’s address space that can be the target of an attack.

- Data Execution Prevention (DEP) – helps protect against exploits such as buffer overflows by limiting the surface of executable memory regions to those expected to contain code rather than allowing execution in regions used only for data.

Which together make the exploitation of memory corruption vulnerabilities probabilistically difficult.

Previous versions of Android have featured a number of security mitigations, including DEP in Android 2.3+ (Gingerbread). Android 4.0 (Ice Cream Sandwich) was the first to make use of ASLR, however the implementation was shown to be relatively limited, leaving substantial segments of process address space predictable. Android 4.1 (Jelly Bean), released in July 2012, includes a more comprehensive and secure implementation.

Furthermore, a new keychain API and underlying encrypted storage let applications store and retrieve private keys and their corresponding certificate chains. Any application can use the keychain API to install and store user certificates and CAs securely. Ice Cream Sandwich also includes Full Disk Encryption, a feature initially released for tablets in Android 3.0, which allows devices to perform boot-time, on-the-fly encryption / decryption of the app storage area.

In early February 2012, Google announced Bouncer, a system to automatically analyze submissions to Google Play for potentially malicious behavior. Bouncer provides developers and the greater security community an alternative to the manual curation process. Developers can still innovate quickly while Bouncer increases the baseline level of security for Android users. Recent research has uncovered methods to profile Bouncer’s execution environment, which could be used to sneak malicious apps past Google Play’s “velvet rope.” Similar to system-level vulnerabilities, we expect that there will always be a way for determined malware developers to sneak malicious applications past safeguards such as Bouncer, but it is a great step in raising the bar to attacking Android devices \[31\].
