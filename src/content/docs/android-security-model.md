---
title: "2. Android Security Model and Permissions"
---

Android’s existing security model is implemented at two layers: an application-level permissions model (known as Android permissions) and a kernel-level sandboxing and isolation mechanism \[48\]. We first review the kernel layer: the foundational mechanism of Linux for application isolation and sandboxing, normally operates invisibly to the app developers and users, so long as an app does not attempt to violate the restrictions imposed by the kernel. Android also relies on Linux kernel which provides a secure inter-process communication (IPC) facility to enable secure communication between applications running in different processes. These security features at the operating system level ensure that even native code is constrained by the application *sandbox*, e.g. whether that code is the result of included application behavior or an exploitation of application vulnerability – the system would prevent the rogue application from harming other applications, the Android system, or the device itself.

As part of the Android security, Android uses Security-Enhanced Linux (SE-Linux) \[47\] to enforce Mandatory Access Control (MAC) over all processes, even processes running with root/superuser privileges. SE-Linux can operate in one of two global modes: permissive mode, in which permission denials are logged but not enforced, and enforcing mode, in which permission denials are both logged and enforced. Android includes SE-Linux in enforcing mode in which illegitimate actions are prevented and all potential violations are logged by the kernel \[27\].

In MAC mechanism, the operating system constrains the ability of a *subject* or *initiator* to access or perform some operation on an *object* or *target*. In practice, a subject is usually a process or thread, objects can be files, directories, network sockets, shared memory segments, I/O devices etc. Both subjects and objects have a set of security attributes. Whenever a subject attempts to access an object, an authorization rule enforced by the operating system kernel examines these security attributes and decides whether the access can take place. Any operation by any subject on any object is tested against the set of authorization rules to determine if the operation is allowed. The enhancement of MAC over Linux’s default discretionary access control (DAC) is that unlike with DAC, users cannot override or modify this policy, either accidentally or intentionally.

The application-level permissions model, which is enforced by the Android middleware, controls access to application components, such as the ability to invoke a service provided by another application, and it controls access to system resources, such as the ability to access the camera or the network. By default, it denies access to features or functionality that could negatively impact the user experience, the system, or other applications installed on the device. Examples of these features are sending messages or making phone calls, which incur monetary cost to the user. Keeping the device screen on or accessing the vibrator, which could result in battery drain. Reading the user’s address book and calendar which could result in privacy violations.

The Android permissions model is directly exposed to Android application developers, who must specify the set of required permissions. Failure to declare a particular permission will result in the related system call or inter-process communication being denied by Android. Android permissions are categorized into the following:

*Signature-or-System* and *Signature* permissions which are used to protect the most sensitive operations on the Android devices. These permissions can only be granted to apps pre-installed into the device’s /system/root folder and/or apps signed with the device manufacturer’s private key. Requests to use these permissions by other apps without the manufacturer’s private key will be ignored \[14\].

*Normal* permissions which are used to govern the functionalities which can be annoying, from user-experience point-of-view (e.g., vibrating the phone).

At last there are the *Dangerous* permissions which are used to protect the user from operations that can be potentially harmful including those that cost money or potentially intrude the users’ privacy (e.g. contact, accounts, camera etc.).

In this paper we focus in the latter group of *dangerous* permissions. These permissions are the ones to put the user in risk of monetary fraud or privacy violation.

In order to better understand these permissions capabilities, we divide the permissions into groups, overview them and show documentation of Android documentation \[27\]:

Cost Sensitive – any function that might generate a cost for the user or the network.

| Permission | Description |
|:---|:---|
| CALL_PHONE | Initiate a phone call without going through the Dialer user interface for the user to confirm the call being placed. |
| CALL_PRIVILEGED | Call any phone number, including emergency numbers, without going through the Dialer user interface for the user to confirm the call being placed. |
| SEND_SMS | Send SMS messages. |
| INTERNET | Open network sockets. |
| ACCESS_NETWORK_STATE | Access information about networks |
| ACCESS_WIFI_STATE | Access information about Wi-Fi networks |
| CHANGE_NETWORK_STATE | Change network connectivity state |
| CHANGE_WIFI_STATE | Change Wi-Fi connectivity state |

Table 1 - Core Sensitive Permission List

Personal Information – provide access to user’s personal and private information data.

| Permission             | Description                                     |
|:-----------------------|:------------------------------------------------|
| READ_PROFILE           | Read the user's personal profile data.          |
| READ_SMS               | Read SMS messages.                              |
| READ_HISTORY_BOOKMARKS | Read the user's browsing history and bookmarks. |
| READ_CONTACTS          | Read the user's contacts data.                  |
| READ_CALENDAR          | Read the user's calendar data.                  |
| READ_CALL_LOG          | Read the user's call log.                       |

Table 2 - Personal Information Permission List

Sensitive Data Input Devices – Android devices frequently provide sensitive data input devices that allow applications to interact with the surrounding environment, such as camera, microphone or GPS.

| Permission | Description |
|:---|:---|
| ACCESS_COARSE_LOCATION | Access approximate location derived from network location sources such as cell towers and Wi-Fi. |
| ACCESS_FINE_LOCATION | Access precise location from location sources such as GPS, cell towers, and Wi-Fi. |
| CAMERA | Access the camera device. |
| RECORD_AUDIO | record audio |
| BLUETOOTH | connect to paired bluetooth devices |
| BLUETOOTH_ADMIN | discover and pair bluetooth devices |
| BLUETOOTH_PRIVILEGED | pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access |

Table 3 - Sensitive Data Input Devices Permission List

Device Metadata – access to data that is not intrinsically sensitive, but may indirectly reveal characteristics about the user, user preferences, and the manner in which they use a device.

| Permission       | Description                                            |
|:-----------------|:-------------------------------------------------------|
| GET_ACCOUNTS     | Access to the list of accounts in the Accounts Service |
| READ_PHONE_STATE | Read only access to phone state.                       |
| READ_LOGS        | Read the low-level system log files.                   |

Table 4 - Device Metadata Permission List

In practice, Android security model could use several improvements, e.g., informing users, more clearly of the security implications of running an app – not only what data is revealed but also what can be done with it, e.g. “this app sends your contacts to 3<sup>rd</sup> party advertisers”. At this point, revoking/granting app permissions without reinstalling the app is not possible. Unlike in Apple’s iOS, where the user can go the privacy settings and revoke a certain permission to a specific app, in Android this is not an option.

As a result, users can have sensitive data leaked or subscription fees charged without their consent. For example, by sending SMS messages to premium numbers via the SMS related Android permissions, as the well-known Android malwares *Zsone* and *Geinimi* do \[28\]. While most of these attacks are first initiated when a user downloads a third-party app to the device, to make matters worse, even stock Android devices with pre-installed apps are prone to exposing personal privacy information due to their higher privilege levels.

While Android permissions model enabling developers to provide a broad range of functionality in their apps, it relies on the end users’ ability to evaluate the requested permissions at the time of installation. In Android, the user must accept all the permissions or forego the installation of the app. This method is called User-Consent Permission System and is also common in Facebook apps, Chrome Extensions and others platforms \[2\]. The operating system vendor relies on the user making the authorization decisions. The problem in user-consent permission systems is that users may become habituated to permission queries and may carelessly click through them. Another concern is the permission name that appears on screen is may not be intuitive for the user and does not always explicitly describe the permission’s capabilities. This is one of the most exploitable vulnerability of many such platform and it is being abused by many malicious mobile apps \[7\].

In a user-consent permission system the user is given the ability to choose, at installation time or in a later phase, whether a certain application will receive a group of permissions or not. In Android, when installing an app, users are presented with the list of permissions requested by the app, as seen in Figure 2. At this phase, the user can determine whether the permissions are appropriate for the app functionality. If the permissions seem overreaching, a user may choose not to install the app.

Apparently, most users do not check the app's permissions at the installation phase as they are very excited to use it already \[13, 14\]. Researchers have examined the best way to visually display installation permissions to users \[16\] but did not examine the frequency of prompts at install-time permission systems. Science literature regarding warning messages, indicates that frequent exposure to specific warnings, especially if the warnings do not lead to negative consequences, drastically reduce the warnings’ effectiveness \[15, 16\]. Even through an option exists to check the app's permission later from the settings menu of Android, most users won't go this menu unless they want to uninstall the app.

For example, in Figure 3 listed below is a permissions approval screen of a simple wallpaper app. By checking thoroughly the permissions it is clearly evident that this app is suspicious: it could be simply a developer overlook, but why does a wallpaper application need to send SMS?


<figure>
<img src="/msc-thesis-research/images/figure3-permissions-approval-screen.png" alt="Figure 3 - Permissions Approval Screen." style="width:340px" />
<figcaption>Figure 3 - Permissions Approval Screen.</figcaption>
</figure>


In case of a more advanced Android (hostile) developer, tracks can be easily covered by clearing all the actions performed by the spyware from the phone log and another update with normal permission can also be performed to provide no clue of malicious activity. If the user does spot a malicious or suspicious activity, it may be too late since the harm has been done already.
