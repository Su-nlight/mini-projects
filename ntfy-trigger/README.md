
# NTFY Triggers presets

This project is made as a reference and ready to burn code of the presets for NTFY service using `ESP32` or `ESP8266`. The ESP development board has inbuilt wifi and bluetooth modules and has higher clock speed than arduino boards making it capable for such an application. This project uses `KY-022` infrared reciever module connected to ESP as per following pin scheme.

| ESP GPIO PIN | KY-022 PIN |
| :-----: | :-----: |
| | |
| | |
| | |



## NTFY API Reference

#### Example HTTP call

```http
POST /phil_alerts HTTP/1.1
Host: ntfy.sh
Title: Unauthorized access detected
Priority: urgent
Tags: warning,skull
Remote access to phils-laptop detected. Act right away.
```

### List of all parameters
The following is a list of all parameters that can be passed when publishing a message. Parameter names are case-insensitive when used in HTTP headers, and must be lowercase when used as query parameters in the URL. They are listed in the table in their canonical form.<br><br>

| Parameter | Aliases     | Description                |
| :-------- | :------- | :------------------------- |
| `X-Message` | `Message`,`m` | Main body of the message as shown in the notification |
| `X-Title` | `Title`,`t` | Message Title |
| `X-Priority` | `Priority`,`prio`,`p`  | Message Priority |
| `X-Tags` | `Tags`,`tag`,`ta` | Tags and emoji |
| `X-Delay` | `Delay`, `X-At`,`At`, `X-In` , `In` | Timestamp or duration for delayed delivery |
| `X-Actions` | `Actions`,`Action` | JSON array or short format of user actions |
| `X-Click` | `Click` | URL to open when notification is clicked |
| `X-Attach` | `Attach` , `a` | URL to send as an attachment, as an alternative to PUT/POST-ing an attachment|
|`X-Markdown` | `Markdown` , `md` | Enable Markdown formatting in the notification body|
| `X-Icon` | `Icon` | URL to use as notification icon |
| `X-Filename` | `Filename` , `file` , `f` | Optional attachment filename, as it appears in the client|
| `X-Email` | `X-E-Mail` , `Email` , `E-Mail` , `mail` , `e` | E-mail address for e-mail notifications |
| `X-Call` | `Call` | Phone number for phone calls|
| `X-Cache` | `Cache` | Allows disabling message caching|
| `X-Firebase` | `Firebase` | Allows disabling sending to Firebase |
| `X-UnifiedPush` | `UnifiedPush` , `up` | UnifiedPush publish option, only to be used by UnifiedPush apps |
| `X-Poll-ID` | `Poll-ID` | Internal parameter, used for iOS push notifications |
| `Authorization` | - | If supported by the server, you can login to access protected topics |




