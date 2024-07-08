# NTFY Trigger Project Documentation

## NTFY Setup

This setup is valid for any machiene connected to same network as the ESP module with a static or dynamic IP address. There is a minute difference for setting up NTFY for static and dynamic addresses. For now, I will focus on setting it up with static IP address.

### Install requirements
Run the following commands in terminal to install wget, sed, Docker on the machiene.
```
sudo apt install wget
sudo apt install sed
sudo apt install docker.io
```
You can also simply procced to next by uncommenting some lines of `docker_setup.sh` as mentioned in the same.

### Download Setup file
Run the following command in terminal of NTFY host machiene.
```
wget -O docker_setup.yml https://raw.githubusercontent.com/Su-nlight/mini-projects/main/ntfy-trigger/docker_setup.sh
```
**Note** : If you skipped previous step uncomment lines 9 to 11. This can be done using you choice of text editor \[i.e., vim, nano and cat (if you are feelinf adventerous)\] .

you can also use actual `server.yml` file as made by NTFY's creator by uncommenting line 16 & line 21 and commenting out line 17. \[This solution is for those who dont trust me even a little bit, as I do not have a very good reputation among my colleages.\]

As mentioned in the `docker_setup.sh` file itself you can change the external port binding (host machiene's) as per your wish by changing the value `2500` (line 30 of same file) to any value (according to your machiene condition) you desire.


## NTFY Triggers presets

This project is made as a reference and ready to burn code of the presets for NTFY service using `ESP32` or `ESP8266`. The ESP development board has inbuilt wifi and bluetooth modules and has higher clock speed than arduino boards making it capable for such an application. This project uses `KY-022` infrared reciever module connected to ESP as per following pin scheme.

| ESP GPIO PIN | KY-022 PIN |
| :-----: | :-----: |
| GPIO 15 | data / `S` |
| 3.3v | +vcc |
| GND | -vsat |



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
| `X-Markdown` | `Markdown` , `md` | Enable Markdown formatting in the notification body|
| `X-Icon` | `Icon` | URL to use as notification icon |
| `X-Filename` | `Filename` , `file` , `f` | Optional attachment filename, as it appears in the client|
| `X-Email` | `X-E-Mail` , `Email` , `E-Mail` , `mail` , `e` | E-mail address for e-mail notifications |
| `X-Call` | `Call` | Phone number for phone calls|
| `X-Cache` | `Cache` | Allows disabling message caching|
| `X-Firebase` | `Firebase` | Allows disabling sending to Firebase |
| `X-UnifiedPush` | `UnifiedPush` , `up` | UnifiedPush publish option, only to be used by UnifiedPush apps |
| `X-Poll-ID` | `Poll-ID` | Internal parameter, used for iOS push notifications |
| `Authorization` | - | If supported by the server, you can login to access protected topics |
| `Content-Type`| `-` | If set to `text/markdown` , Markdown formatting is enabled |



