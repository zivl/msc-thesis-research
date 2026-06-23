---
title: "Appendix B - Selective Group of Android Permissions"
---

Table X represents Android permissions which have been selected carefully to be modeled to provide reduced list of features for the classifier.

| Permission Name | Android Official Documentation | Is Modeled | Reason |
|----|----|:--:|----|
| ACCESS_CHECKIN_PROPERTIES | Allows read/write access to the "properties" table in the checkin database, to change values that get uploaded. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ACCESS_COARSE_LOCATION | Allows an app to access approximate location derived from network location sources such as cell towers and Wi-Fi. | V | used by malwares that steals private data |
| ACCESS_FINE_LOCATION | Allows an app to access precise location from location sources such as GPS, cell towers, and Wi-Fi. | V | used by malwares that steals private data |
| ACCESS_LOCATION_EXTRA_COMMANDS | Allows an application to access extra location provider commands | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ACCESS_MOCK_LOCATION | Allows an application to create mock location providers for testing | X | used while the device is in “developing” or “debugger” mode |
| ACCESS_NETWORK_STATE | Allows applications to access information about networks | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ACCESS_SURFACE_FLINGER | Allows an application to use SurfaceFlinger's low level features. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ACCESS_WIFI_STATE | Allows applications to access information about Wi-Fi networks | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ACCOUNT_MANAGER | Allows applications to call into AccountAuthenticators. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| ADD_VOICEMAIL | Allows an application to add voicemails into the system. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| AUTHENTICATE_ACCOUNTS | Allows an application to act as an AccountAuthenticator for the AccountManager | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| BATTERY_STATS | Allows an application to collect battery statistics | X | hardware information retrieving |
| BIND_ACCESSIBILITY_SERVICE | Must be required by an AccessibilityService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_APPWIDGET | Allows an application to tell the AppWidget service which application can access AppWidget's data. | X | used to allow an app to subscribe and/or publish events |
| BIND_DEVICE_ADMIN | Must be required by device administration receiver, to ensure that only the system can interact with it. | X | used to allow an app to subscribe and/or publish events |
| BIND_INPUT_METHOD | Must be required by an InputMethodService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_NFC_SERVICE | Must be required by a HostApduService or OffHostApduService to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_NOTIFICATION_LISTENER_SERVICE | Must be required by an NotificationListenerService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_PRINT_SERVICE | Must be required by a PrintService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_REMOTEVIEWS | Must be required by a RemoteViewsService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_TEXT_SERVICE | Must be required by a TextService (e.g. | X | used to allow an app to subscribe and/or publish events |
| BIND_VPN_SERVICE | Must be required by a VpnService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BIND_WALLPAPER | Must be required by a WallpaperService, to ensure that only the system can bind to it. | X | used to allow an app to subscribe and/or publish events |
| BLUETOOTH | Allows applications to connect to paired bluetooth devices | V | used by malwares to change different kind of configurations without the user consent |
| BLUETOOTH_ADMIN | Allows applications to discover and pair bluetooth devices | V | used by malwares to change different kind of configurations without the user consent |
| BLUETOOTH_PRIVILEGED | Allows applications to pair bluetooth devices without user interaction. | V | used by malwares to change different kind of configurations without the user consent |
| BRICK | Required to be able to disable the device (very dangerous!). | X | not used by any app |
| BROADCAST_PACKAGE_REMOVED | Allows an application to broadcast a notification that an application package has been removed. | X | used to allow an app to subscribe and/or publish events |
| BROADCAST_SMS | Allows an application to broadcast an SMS receipt notification. | X | used to allow an app to subscribe and/or publish events |
| BROADCAST_STICKY | Allows an application to broadcast sticky intents. | X | used to allow an app to subscribe and/or publish events |
| BROADCAST_WAP_PUSH | Allows an application to broadcast a WAP PUSH receipt notification. | X | used to allow an app to subscribe and/or publish events |
| CALL_PHONE | Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call being placed. | V | used by malwares for money frauds |
| CALL_PRIVILEGED | Allows an application to call any phone number, including emergency numbers, without going through the Dialer user interface for the user to confirm the call being placed. | V | used by malwares for money frauds |
| CAMERA | Required to be able to access the camera device. | V | used by spywares |
| CAPTURE_AUDIO_OUTPUT | Allows an application to capture audio output. | V | used by spywares |
| CAPTURE_SECURE_VIDEO_OUTPUT | Allows an application to capture secure video output. | V | used by spywares |
| CAPTURE_VIDEO_OUTPUT | Allows an application to capture video output. | V | used by spywares |
| CHANGE_COMPONENT_ENABLED_STATE | Allows an application to change whether an application component (other than its own) is enabled or not. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| CHANGE_CONFIGURATION | Allows an application to modify the current configuration, such as locale. | V | used by malwares to change different kind of configurations without the user consent |
| CHANGE_NETWORK_STATE | Allows applications to change network connectivity state | V | used by malwares to change different kind of configurations without the user consent |
| CHANGE_WIFI_MULTICAST_STATE | Allows applications to enter Wi-Fi Multicast mode | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| CHANGE_WIFI_STATE | Allows applications to change Wi-Fi connectivity state | V | used by malwares to change different kind of configurations without the user consent |
| CLEAR_APP_CACHE | Allows an application to clear the caches of all installed applications on the device. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| CLEAR_APP_USER_DATA | Allows an application to clear user data. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| CONTROL_LOCATION_UPDATES | Allows enabling/disabling location update notifications from the radio. | X | used to allow an app to subscribe and/or publish events |
| DELETE_CACHE_FILES | Allows an application to delete cache files. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| DELETE_PACKAGES | Allows an application to delete packages. | V | used by malwares that harms the data and/or delete it |
| DEVICE_POWER | Allows low-level access to power management. | X | hardware information retrieving |
| DIAGNOSTIC | Allows applications to RW to diagnostic resources. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| DISABLE_KEYGUARD | Allows applications to disable the keyguard | X | used for special user-interface effects, accessories and enhancements |
| DUMP | Allows an application to retrieve state dump information from system services. | X | hardware information retrieving |
| EXPAND_STATUS_BAR | Allows an application to expand or collapse the status bar. | X | used for special user-interface effects, accessories and enhancements |
| FACTORY_TEST | Run as a manufacturer test application, running as the root user. | X | used while the device is in “developing” or “debugger” mode |
| FLASHLIGHT | Allows access to the flashlight | X | hardware information retrieving |
| FORCE_BACK | Allows an application to force a BACK operation on whatever is the top activity. | X | used for special user-interface effects, accessories and enhancements |
| GET_ACCOUNTS | Allows access to the list of accounts in the Accounts Service | V | used by malwares that steals private data |
| GET_PACKAGE_SIZE | Allows an application to find out the space used by any package. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| GET_TASKS | Allows an application to get information about the currently or recently running tasks. | V | used by spywares |
| GET_TOP_ACTIVITY_INFO | Allows an application to retrieve private information about the current top activity, such as any assist context it can provide. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| GLOBAL_SEARCH | This permission can be used on content providers to allow the global search system to access their data. | X | used for special user-interface effects, accessories and enhancements |
| HARDWARE_TEST | Allows access to hardware peripherals. | X | hardware information retrieving |
| INJECT_EVENTS | Allows an application to inject user events (keys, touch, trackball) into the event stream and deliver them to ANY window. | X | used to allow an app to subscribe and/or publish events |
| INSTALL_LOCATION_PROVIDER | Allows an application to install a location provider into the Location Manager. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| INSTALL_PACKAGES | Allows an application to install packages. | V | used by malwares that harms the data and/or delete it |
| INSTALL_SHORTCUT | Allows an application to install a shortcut in Launcher | V | used by malwares that harms the data and/or delete it |
| INTERNAL_SYSTEM_WINDOW | Allows an application to open windows that are for use by parts of the system user interface. | X | used for special user-interface effects, accessories and enhancements |
| INTERNET | Allows applications to open network sockets. | V | used by many malwares as vector attack |
| KILL_BACKGROUND_PROCESSES | Allows an application to call killBackgroundProcesses(String). | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| LOCATION_HARDWARE | Allows an application to use location features in hardware, such as the geofencing api. | X | hardware information retrieving |
| MANAGE_ACCOUNTS | Allows an application to manage the list of accounts in the AccountManager | V | used by malwares that steals private data |
| MANAGE_APP_TOKENS | Allows an application to manage (create, destroy, Z-order) application tokens in the window manager. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| MANAGE_DOCUMENTS | Allows an application to manage access to documents, usually as part of a document picker. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| MASTER_CLEAR | Not for use by third-party applications. | V | used by malwares that harms the data and/or delete it |
| MEDIA_CONTENT_CONTROL | Allows an application to know what content is playing and control its playback. | V | used by spywares |
| MODIFY_AUDIO_SETTINGS | Allows an application to modify global audio settings | V | used by malwares to change different kind of configurations without the user consent |
| MODIFY_PHONE_STATE | Allows modification of the telephony state - power on, mmi, etc. | V | used by malwares to change different kind of configurations without the user consent |
| MOUNT_FORMAT_FILESYSTEMS | Allows formatting file systems for removable storage. | V | used by malwares that harms the data and/or delete it |
| MOUNT_UNMOUNT_FILESYSTEMS | Allows mounting and unmounting file systems for removable storage. | V | used by malwares that harms the data and/or delete it |
| NFC | Allows applications to perform I/O operations over NFC | X | hardware information retrieving |
| PERSISTENT_ACTIVITY | This constant was deprecated in API level 9. This functionality will be removed in the future; please do not use. Allow an application to make its activities persistent. | X | used for special user-interface effects, accessories and enhancements |
| PROCESS_OUTGOING_CALLS | Allows an application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether. | V | used by spywares |
| READ_CALENDAR | Allows an application to read the user's calendar data. | V | used by malwares that steals private data |
| READ_CALL_LOG | Allows an application to read the user's call log. | V | used by spywares |
| READ_CONTACTS | Allows an application to read the user's contacts data. | V | used by malwares that steals private data |
| READ_EXTERNAL_STORAGE | Allows an application to read from external storage. | V | used by spywares |
| READ_FRAME_BUFFER | Allows an application to take screen shots and more generally get access to the frame buffer data. | V | used by spywares |
| READ_HISTORY_BOOKMARKS | Allows an application to read (but not write) the user's browsing history and bookmarks. | V | used by spywares |
| READ_INPUT_STATE | This constant was deprecated in API level 16. The API that used this permission has been removed. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| READ_LOGS | Allows an application to read the low-level system log files. | V | used by spywares |
| READ_PHONE_STATE | Allows read only access to phone state. | V | used by malwares that steals private data |
| READ_PROFILE | Allows an application to read the user's personal profile data. | V | used by malwares that steals private data |
| READ_SMS | Allows an application to read SMS messages. | V | used by spywares |
| READ_SOCIAL_STREAM | Allows an application to read from the user's social stream. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| READ_SYNC_SETTINGS | Allows applications to read the sync settings | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| READ_SYNC_STATS | Allows applications to read the sync stats | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| READ_USER_DICTIONARY | Allows an application to read the user dictionary. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| REBOOT | Required to be able to reboot the device. | X | used for special user-interface effects, accessories and enhancements |
| RECEIVE_BOOT_COMPLETED | Allows an application to receive the ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. | X | used to allow an app to subscribe and/or publish events |
| RECEIVE_MMS | Allows an application to monitor incoming MMS messages, to record or perform processing on them. | V | used by malwares that steals private data |
| RECEIVE_SMS | Allows an application to monitor incoming SMS messages, to record or perform processing on them. | V | used by malwares that steals private data |
| RECEIVE_WAP_PUSH | Allows an application to monitor incoming WAP push messages. | V | used by malwares that steals private data |
| RECORD_AUDIO | Allows an application to record audio | V | used by spywares |
| REORDER_TASKS | Allows an application to change the Z-order of tasks | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| RESTART_PACKAGES | This constant was deprecated in API level 8. The restartPackage(String) API is no longer supported. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SEND_RESPOND_VIA_MESSAGE | Allows an application (Phone) to send a request to other applications to handle the respond-via-message action during incoming calls. | X | used to allow an app to subscribe and/or publish events |
| SEND_SMS | Allows an application to send SMS messages. | V | used by malwares for money frauds |
| SET_ACTIVITY_WATCHER | Allows an application to watch and control how activities are started globally in the system. | X | used while the device is in “developing” or “debugger” mode |
| SET_ALARM | Allows an application to broadcast an Intent to set an alarm for the user. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SET_ALWAYS_FINISH | Allows an application to control whether activities are immediately finished when put in the background. | X | used for special user-interface effects, accessories and enhancements |
| SET_ANIMATION_SCALE | Modify the global animation scaling factor. | X | used for special user-interface effects, accessories and enhancements |
| SET_DEBUG_APP | Configure an application for debugging. | X | used while the device is in “developing” or “debugger” mode |
| SET_ORIENTATION | Allows low-level access to setting the orientation (actually rotation) of the screen. | X | used for special user-interface effects, accessories and enhancements |
| SET_POINTER_SPEED | Allows low-level access to setting the pointer speed. | X | used for special user-interface effects, accessories and enhancements |
| SET_PREFERRED_APPLICATIONS | This constant was deprecated in API level 7. No longer useful, see addPackageToPreferred(String) for details. | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| SET_PROCESS_LIMIT | Allows an application to set the maximum number of (not needed) application processes that can be running. | X | used for special user-interface effects, accessories and enhancements |
| SET_TIME | Allows applications to set the system time. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SET_TIME_ZONE | Allows applications to set the system time zone | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SET_WALLPAPER | Allows applications to set the wallpaper | X | used for special user-interface effects, accessories and enhancements |
| SET_WALLPAPER_HINTS | Allows applications to set the wallpaper hints | X | used for special user-interface effects, accessories and enhancements |
| SIGNAL_PERSISTENT_PROCESSES | Allow an application to request that a signal be sent to all persistent processes. | X | used to allow an app to subscribe and/or publish events |
| STATUS_BAR | Allows an application to open, close, or disable the status bar and its icons. | X | used for special user-interface effects, accessories and enhancements |
| SUBSCRIBED_FEEDS_READ | Allows an application to allow access the subscribed feeds ContentProvider. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SUBSCRIBED_FEEDS_WRITE |  | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| SYSTEM_ALERT_WINDOW | Allows an application to open windows using the type TYPE_SYSTEM_ALERT, shown on top of all other applications. | X | used for special user-interface effects, accessories and enhancements |
| TRANSMIT_IR | Allows using the device's IR transmitter, if available | X | used to get some data’s state or status. It cannot harm the user or the device in any way |
| UNINSTALL_SHORTCUT | Allows an application to uninstall a shortcut in Launcher | X | used for special user-interface effects, accessories and enhancements |
| UPDATE_DEVICE_STATS | Allows an application to update device statistics. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| USE_CREDENTIALS | Allows an application to request authtokens from the AccountManager | V | used by malwares that steals private data |
| USE_SIP | Allows an application to use SIP service | X | used for special user-interface effects, accessories and enhancements |
| VIBRATE | Allows access to the vibrator | X | hardware information retrieving |
| WAKE_LOCK | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming | X | used for special user-interface effects, accessories and enhancements |
| WRITE_APN_SETTINGS | Allows applications to write the apn settings. | V | used by malwares that harms the data and/or delete it |
| WRITE_CALENDAR | Allows an application to write (but not read) the user's calendar data. | V | used by malwares that harms the data and/or delete it |
| WRITE_CALL_LOG | Allows an application to write (but not read) the user's contacts data. | V | used by malwares that harms the data and/or delete it |
| WRITE_CONTACTS | Allows an application to write (but not read) the user's contacts data. | V | used by malwares that harms the data and/or delete it |
| WRITE_EXTERNAL_STORAGE | Allows an application to write to external storage. | V | used by malwares that harms the data and/or delete it |
| WRITE_GSERVICES | Allows an application to modify the Google service map. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| WRITE_HISTORY_BOOKMARKS | Allows an application to write (but not read) the user's browsing history and bookmarks. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| WRITE_PROFILE | Allows an application to write (but not read) the user's personal profile data. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| WRITE_SECURE_SETTINGS | Allows an application to read or write the secure system settings. | V | used by malwares that harms the data and/or delete it |
| WRITE_SETTINGS | Allows an application to read or write the system settings. | V | used by malwares that harms the data and/or delete it |
| WRITE_SMS | Allows an application to write SMS messages. | V | used by malwares for money frauds |
| WRITE_SOCIAL_STREAM | Allows an application to write (but not read) the user's social stream data. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| WRITE_SYNC_SETTINGS | Allows applications to write the sync settings | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |
| WRITE_USER_DICTIONARY | Allows an application to write to the user dictionary. | X | Disclosure of such data will not affect or harm the user, will not cause to money consumption or compromise the device |

\
