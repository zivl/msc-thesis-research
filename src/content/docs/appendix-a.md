---
title: "Appendix A – Permissions Histograms"
---

Table 13 describes permissions and their occurrences histogram within the group types in the training dataset, such that, the histogram values are normalized to the training dataset group size. In the last column, “model scores”, we point the outcome of the model’s training process which is the scores of each permission. Negative score pulls the weight towards *malicious* group and positive score pulls towards *safe* group.

Note: for convenience purposes, all permissions are sorted alphabetically and permissions where their value is zero (0) occurrences in both malicious and safe apps datasets were omitted.

Table 13 - Permissions Histogram of Training Dataset

| Permission                     | In Safe Apps | In Malicious Apps | Model Scores |
|--------------------------------|--------------|-------------------|--------------|
| ACCESS_CHECKIN_PROPERTIES      | 0.002857143  | 0.002857143       | 0.189868     |
| ACCESS_COARSE_LOCATION         | 0.208571429  | 0.214285714       | -1.36292     |
| ACCESS_FINE_LOCATION           | 0.165714286  | 0.185714286       | -0.60079     |
| ACCESS_GPS                     | 0.002857143  | 0.005714286       | 0.227602     |
| ACCESS_LOCATION_EXTRA_COMMANDS | 0.005714286  | 0.02              | -0.62238     |
| ACCESS_MOCK_LOCATION           | 0            | 0.008571429       | -0.20587     |
| ACCESS_NETWORK_STATE           | 0.782857143  | 0.382857143       | 2.513823     |
| ACCESS_SURFACE_FLINGER         | 0.002857143  | 0.008571429       | 0.309038     |
| ACCESS_WIFI_STATE              | 0.491428571  | 0.214285714       | 1.227483     |
| ACCOUNT_MANAGER                | 0.008571429  | 0.002857143       | 0.349041     |
| AUTHENTICATE_ACCOUNTS          | 0.051428571  | 0.002857143       | 1.501681     |
| BATTERY_STATS                  | 0.022857143  | 0.017142857       | 0.960596     |
| BIND_APPWIDGET                 | 0            | 0.002857143       | -0.0674      |
| BIND_DEVICE_ADMIN              | 0.005714286  | 0.005714286       | 0.168901     |
| BIND_INPUT_METHOD              | 0.002857143  | 0.002857143       | 0.001247     |
| BIND_REMOTEVIEWS               | 0.02         | 0                 | 0.687412     |
| BIND_WALLPAPER                 | 0.017142857  | 0.014285714       | -0.29839     |
| BLUETOOTH                      | 0.034285714  | 0.034285714       | -0.55814     |
| BLUETOOTH_ADMIN                | 0.02         | 0.02              | -0.82445     |
| BRICK                          | 0            | 0.014285714       | -1.52586     |
| BROADCAST_PACKAGE_REMOVED      | 0.002857143  | 0.008571429       | -0.08194     |
| BROADCAST_SMS                  | 0.002857143  | 0.017142857       | -0.05983     |
| BROADCAST_STICKY               | 0.042857143  | 0.017142857       | 1.310563     |
| BROADCAST_WAP_PUSH             | 0            | 0.014285714       | -0.43871     |
| CALL_PHONE                     | 0.051428571  | 0.165714286       | -0.17216     |
| CALL_PRIVILEGED                | 0            | 0.017142857       | -0.22957     |
| CAMERA                         | 0.117142857  | 0.037142857       | 1.862345     |
| CHANGE_COMPONENT_ENABLED_STATE | 0.005714286  | 0.008571429       | 0.30333      |
| CHANGE_CONFIGURATION           | 0.011428571  | 0.08              | -1.33199     |
| CHANGE_NETWORK_STATE           | 0.045714286  | 0.057142857       | 0.30624      |
| CHANGE_WIFI_MULTICAST_STATE    | 0.011428571  | 0.002857143       | 0.865725     |
| CHANGE_WIFI_STATE              | 0.051428571  | 0.125714286       | -2.29926     |
| CLEAR_APP_CACHE                | 0.008571429  | 0.002857143       | 0.790354     |
| CLEAR_APP_USER_DATA            | 0            | 0.002857143       | -0.0674      |
| CONTROL_LOCATION_UPDATES       | 0.008571429  | 0.014285714       | 1.183239     |
| DELETE_CACHE_FILES             | 0.002857143  | 0.005714286       | 0.02002      |
| DELETE_PACKAGES                | 0.002857143  | 0.04              | -0.62077     |
| DEVICE_POWER                   | 0.014285714  | 0.028571429       | 0.153917     |
| DIAGNOSTIC                     | 0            | 0.002857143       | -0.0674      |
| DISABLE_KEYGUARD               | 0.057142857  | 0.042857143       | 0.5725       |
| DUMP                           | 0.002857143  | 0.005714286       | -0.68934     |
| EXPAND_STATUS_BAR              | 0.02         | 0.011428571       | -0.30114     |
| FACTORY_TEST                   | 0            | 0.02              | -1.87047     |
| FLASHLIGHT                     | 0.025714286  | 0.005714286       | 0.351303     |
| FORCE_BACK                     | 0            | 0.002857143       | -0.0674      |
| GET_ACCOUNTS                   | 0.268571429  | 0.054285714       | 1.05004      |
| GET_PACKAGE_SIZE               | 0.008571429  | 0.005714286       | 0.922192     |
| GET_TASKS                      | 0.125714286  | 0.085714286       | -0.17061     |
| GLOBAL_SEARCH                  | 0.005714286  | 0.002857143       | 5.25E-04     |
| HARDWARE_CONTROLS              | 0.002857143  | 0                 | 0.341672     |
| HARDWARE_TEST                  | 0            | 0.008571429       | -1.31213     |
| INJECT_EVENTS                  | 0.002857143  | 0.005714286       | -0.57518     |
| INSTALL_LOCATION_PROVIDER      | 0            | 0.002857143       | -0.0674      |
| INSTALL_PACKAGES               | 0.002857143  | 0.114285714       | -2.43274     |
| INSTALL_SHORTCUT               | 0.062857143  | 0.12              | -0.60821     |
| INTERNAL_SYSTEM_WINDOW         | 0.005714286  | 0.014285714       | 0.39569      |
| INTERNET                       | 0.854285714  | 0.957142857       | -0.19113     |
| KILL_BACKGROUND_PROCESSES      | 0.02         | 0.011428571       | 0.89539      |
| LOCATION_HARDWARE              | 0.002857143  | 0                 | 6.52E-05     |
| MANAGE_ACCOUNTS                | 0.08         | 0.017142857       | 0.606548     |
| MANAGE_APP_TOKENS              | 0            | 0.005714286       | -0.07925     |
| MASTER_CLEAR                   | 0            | 0.008571429       | -0.97376     |
| MESSAGES                       | 0.002857143  | 0                 | -8.08E-04    |
| MODIFY_AUDIO_SETTINGS          | 0.048571429  | 0.048571429       | -0.04334     |
| MODIFY_PHONE_STATE             | 0.014285714  | 0.057142857       | 1.114185     |
| MOUNT_FORMAT_FILESYSTEMS       | 0.002857143  | 0.002857143       | 0.360765     |
| MOUNT_UNMOUNT_FILESYSTEMS      | 0.08         | 0.048571429       | 1.924997     |
| NETWORK                        | 0.002857143  | 0                 | 0.30046      |
| NFC                            | 0.034285714  | 0                 | 1.096687     |
| PERSISTENT_ACTIVITY            | 0            | 0.005714286       | -0.07925     |
| PERSONAL_INFO                  | 0.014285714  | 0                 | 0.253556     |
| PROCESS_OUTGOING_CALLS         | 0.005714286  | 0.071428571       | -0.77475     |
| READ_CALENDAR                  | 0.02         | 0.025714286       | -0.42627     |
| READ_CALL_LOG                  | 0.005714286  | 0                 | 0.061955     |
| READ_CONTACTS                  | 0.108571429  | 0.185714286       | 0.476569     |
| READ_EXTERNAL_STORAGE          | 0.091428571  | 0.071428571       | -0.44166     |
| READ_FRAME_BUFFER              | 0.002857143  | 0.017142857       | -1.17336     |
| READ_HISTORY_BOOKMARKS         | 0.02         | 0.094285714       | -0.90449     |
| READ_INPUT_STATE               | 0            | 0.002857143       | -0.0674      |
| READ_LOGS                      | 0.022857143  | 0.08              | -2.36808     |
| READ_PHONE_STATE               | 0.525714286  | 0.882857143       | -1.90804     |
| READ_PROFILE                   | 0.025714286  | 0.014285714       | -0.8239      |
| READ_SETTINGS                  | 0.02         | 0.048571429       | -0.23301     |
| READ_SMS                       | 0.028571429  | 0.425714286       | -0.85599     |
| READ_SOCIAL_STREAM             | 0.008571429  | 0                 | 0.003482     |
| READ_SYNC_SETTINGS             | 0.054285714  | 0.002857143       | 1.914926     |
| READ_SYNC_STATS                | 0.02         | 0.002857143       | 0.389589     |
| READ_USER_DICTIONARY           | 0.002857143  | 0                 | 0.060111     |
| REBOOT                         | 0            | 0.002857143       | -0.0674      |
| RECEIVE_BOOT_COMPLETED         | 0.194285714  | 0.277142857       | 0.192032     |
| RECEIVE_MMS                    | 0.008571429  | 0.031428571       | -0.08828     |
| RECEIVE_SMS                    | 0.022857143  | 0.594285714       | -2.80615     |
| RECEIVE_WAP_PUSH               | 0            | 0.034285714       | -0.88655     |
| RECORD_AUDIO                   | 0.068571429  | 0.04              | 0.236615     |
| REORDER_TASKS                  | 0.011428571  | 0.014285714       | -0.05414     |
| RESTART_PACKAGES               | 0.014285714  | 0.068571429       | -0.06581     |
| SEND_SMS                       | 0.034285714  | 0.631428571       | -0.84061     |
| SET_ACTIVITY_WATCHER           | 0            | 0.002857143       | -0.0674      |
| SET_ALARM                      | 0.008571429  | 0.031428571       | 0.120418     |
| SET_ALWAYS_FINISH              | 0            | 0.002857143       | -0.0674      |
| SET_ANIMATION_SCALE            | 0.002857143  | 0.002857143       | 0.738363     |
| SET_DEBUG_APP                  | 0            | 0.002857143       | -0.0674      |
| SET_ORIENTATION                | 0.022857143  | 0.002857143       | 1.966844     |
| SET_PREFERRED_APPLICATIONS     | 0            | 0.002857143       | -0.0674      |
| SET_PROCESS_LIMIT              | 0            | 0.002857143       | -0.0674      |
| SET_TIME                       | 0.002857143  | 0                 | 0.217625     |
| SET_TIME_ZONE                  | 0.002857143  | 0.002857143       | 0.625903     |
| SET_WALLPAPER                  | 0.028571429  | 0.017142857       | 0.563883     |
| SET_WALLPAPER_HINTS            | 0            | 0.002857143       | -0.0674      |
| SIGNAL_PERSISTENT_PROCESSES    | 0            | 0.002857143       | -0.0674      |
| STATUS_BAR                     | 0.02         | 0.022857143       | 0.02093      |
| STORAGE                        | 0.002857143  | 0                 | 0.099131     |
| SUBSCRIBED_FEEDS_READ          | 0.017142857  | 0.002857143       | 0.100298     |
| SUBSCRIBED_FEEDS_WRITE         | 0.017142857  | 0.002857143       | 0.462476     |
| SYSTEM_ALERT_WINDOW            | 0.068571429  | 0.08              | 0.239469     |
| SYSTEM_TOOLS                   | 0            | 0.008571429       | -1.50883     |
| UNINSTALL_SHORTCUT             | 0.022857143  | 0.014285714       | -0.12604     |
| UPDATE_DEVICE_STATS            | 0.005714286  | 0.031428571       | -0.28921     |
| USE_CREDENTIALS                | 0.074285714  | 0.005714286       | 0.547921     |
| WAKE_LOCK                      | 0.425714286  | 0.371428571       | 1.052219     |
| WRITE_APN_SETTINGS             | 0.005714286  | 0.054285714       | -0.36813     |
| WRITE_CALENDAR                 | 0.011428571  | 0.022857143       | -1.1841      |
| WRITE_CALL_LOG                 | 0.002857143  | 0                 | 0.003508     |
| WRITE_CONTACTS                 | 0.051428571  | 0.062857143       | 0.56024      |
| WRITE_EXTERNAL_STORAGE         | 0.677142857  | 0.717142857       | 0.321755     |
| WRITE_GSERVICES                | 0.002857143  | 0.002857143       | 0.233063     |
| WRITE_HISTORY_BOOKMARKS        | 0.005714286  | 0.057142857       | -1.73415     |
| WRITE_PROFILE                  | 0.005714286  | 0                 | 0.012152     |
| WRITE_SECURE_SETTINGS          | 0.014285714  | 0.057142857       | -0.30297     |
| WRITE_SETTINGS                 | 0.08         | 0.137142857       | -0.27728     |
| WRITE_SMS                      | 0.02         | 0.082857143       | 0.414486     |
| WRITE_SOCIAL_STREAM            | 0.008571429  | 0                 | 0.003482     |
| WRITE_SYNC_SETTINGS            | 0.054285714  | 0.002857143       | 1.466328     |
| WRITE_USER_DICTIONARY          | 0.005714286  | 0                 | 0.488274     |

Table 14 describes permissions histogram of the safe apps <u>testing</u> dataset results, such that, histogram values are normalized to the group size, i.e. success group or failure group.

Note: For convenience and relevance purposes, we only present here permissions which had more than 20 occurrences in a certain group.

Table 14 - Permissions Histogram of Safe Apps Testing Results

| Permission | Successfully Predicted as Safe | Failed in Prediction |
|----|:--:|:--:|
| ACCESS_COARSE_LOCATION | 0.24 | 0.37 |
| ACCESS_FINE_LOCATION | 0.26 | 0.35 |
| ACCESS_MOCK_LOCATION | 0.03 | 0 |
| ACCESS_NETWORK_STATE | 0.72 | 0.23 |
| ACCESS_WIFI_STATE | 0.24 | 0.09 |
| BATTERY_STATS | 0.03 | 0 |
| BLUETOOTH | 0.03 | 0 |
| CALL_PHONE | 0.11 | 0.15 |
| CAMERA | 0.21 | 0 |
| CHANGE_NETWORK_STATE | 0.03 | 0 |
| CHANGE_WIFI_STATE | 0.05 | 0.05 |
| DEVICE_POWER | 0.03 | 0 |
| DISABLE_KEYGUARD | 0.07 | 0 |
| FLASHLIGHT | 0.05 | 0 |
| GET_ACCOUNTS | 0.11 | 0 |
| GET_TASKS | 0.08 | 0.07 |
| INSTALL_SHORTCUT | 0.05 | 0.05 |
| INTERNET | 0.87 | 0.77 |
| KILL_BACKGROUND_PROCESSES | 0.03 | 0 |
| MODIFY_AUDIO_SETTINGS | 0.07 | 0 |
| MOUNT_UNMOUNT_FILESYSTEMS | 0.03 | 0 |
| READ_CONTACTS | 0.2 | 0.18 |
| READ_EXTERNAL_STORAGE | 0.06 | 0 |
| READ_LOGS | 0.02 | 0.06 |
| READ_PHONE_STATE | 0.4 | 0.51 |
| READ_SMS | 0.02 | 0.07 |
| RECEIVE_BOOT_COMPLETED | 0.22 | 0.17 |
| RECEIVE_SMS | 0 | 0.12 |
| RECORD_AUDIO | 0.11 | 0 |
| RESTART_PACKAGES | 0.06 | 0 |
| SEND_SMS | 0.03 | 0.13 |
| SET_ORIENTATION | 0.04 | 0 |
| SET_WALLPAPER | 0.06 | 0 |
| WAKE_LOCK | 0.46 | 0.2 |
| WRITE_CONTACTS | 0.08 | 0 |
| WRITE_EXTERNAL_STORAGE | 0.54 | 0.28 |
| WRITE_SETTINGS | 0.1 | 0.08 |

Table 15 describes permissions histogram of the malicious apps <u>testing</u> dataset results, such that, histogram values are normalized to the group size, i.e. success group or failure group.

Note: For convenience and relevance purposes, we only present here permissions which had more than 20 occurrences in a certain group.

Table 15 - Permissions Histogram of Malicious Apps Testing Results

| Permission | Successfully Predicted as Malicious | Failed in Prediction |
|----|:--:|:--:|
| ACCESS_COARSE_LOCATION | 0.22 | 0.38 |
| ACCESS_FINE_LOCATION | 0.2 | 0.27 |
| ACCESS_LOCATION_EXTRA_COMMANDS | 0.04 | 0 |
| ACCESS_NETWORK_STATE | 0.32 | 0.87 |
| ACCESS_WIFI_STATE | 0.21 | 0.59 |
| BIND_WALLPAPER | 0.02 | 0 |
| CALL_PHONE | 0.13 | 0 |
| CAMERA | 0.03 | 0 |
| CHANGE_CONFIGURATION | 0.08 | 0 |
| CHANGE_NETWORK_STATE | 0.04 | 0 |
| CHANGE_WIFI_STATE | 0.13 | 0 |
| DELETE_PACKAGES | 0.04 | 0 |
| DISABLE_KEYGUARD | 0.02 | 0 |
| GET_ACCOUNTS | 0.03 | 0 |
| GET_TASKS | 0.07 | 0.32 |
| INSTALL_PACKAGES | 0.12 | 0 |
| INTERNET | 0.99 | 0.97 |
| MODIFY_AUDIO_SETTINGS | 0.02 | 0 |
| MOUNT_UNMOUNT_FILESYSTEMS | 0.02 | 0 |
| PROCESS_OUTGOING_CALLS | 0.02 | 0 |
| READ_CONTACTS | 0.1 | 0 |
| READ_EXTERNAL_STORAGE | 0.05 | 0 |
| READ_HISTORY_BOOKMARKS | 0.05 | 0 |
| READ_LOGS | 0.06 | 0 |
| READ_PHONE_STATE | 0.95 | 0.77 |
| READ_SMS | 0.42 | 0 |
| RECEIVE_BOOT_COMPLETED | 0.26 | 0.29 |
| RECEIVE_SMS | 0.63 | 0 |
| RECEIVE_WAP_PUSH | 0.03 | 0 |
| RECORD_AUDIO | 0.03 | 0 |
| RESTART_PACKAGES | 0.06 | 0 |
| SEND_SMS | 0.68 | 0 |
| SET_ALARM | 0.05 | 0 |
| SET_WALLPAPER | 0.03 | 0 |
| SYSTEM_ALERT_WINDOW | 0.07 | 0 |
| UPDATE_DEVICE_STATS | 0.02 | 0 |
| WAKE_LOCK | 0.4 | 0.51 |
| WRITE_APN_SETTINGS | 0.02 | 0 |
| WRITE_CONTACTS | 0.03 | 0 |
| WRITE_EXTERNAL_STORAGE | 0.74 | 0.78 |
| WRITE_HISTORY_BOOKMARKS | 0.05 | 0 |
| WRITE_SECURE_SETTINGS | 0.05 | 0 |
| WRITE_SETTINGS | 0.1 | 0.18 |
| WRITE_SMS | 0.05 | 0 |
| INSTALL_SHORTCUT | 0.17 | 0.21 |
| UNINSTALL_SHORTCUT | 0.03 | 0 |
| READ_SETTINGS | 0.05 | 0 |
