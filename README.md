# VoiceCription
It is very simple Web Application for doctors, which takes voice input that doctor ask their patient and and produces a Prescription.

![Main page](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/Main.png?raw=true)

This Application first ask doctor to login or sign up.

![Login Page](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/login.png?raw=true)

![authorize](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/authorize.png?raw=true)

After Login it redirects to Doctor's Dashboard where doctor can see his/her Details. 
Doctor then can upload her/his digital signature we will be used in prescription.

![Dashboard](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/dashboard.png?raw=true)

![Dashboard2](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/dashboard2.png?raw=true)

Doctor can also search for patient record by entering her/his name and their prescription can be accessed by Doctor.

![past_record](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/past_record.png?raw=true)

On clicking + button Doctor will redirect to form page where doctor gives voice input for different fields.

![Form](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/form.png?raw=true)

On submiiting, a prescription is created and uploaded on doctor's Google Drive and Creates QRCode show it on next screen for patient.

![qrscreen](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/qrcode.png?raw=true)

Patient can now Scan the Qr Code for downloading his/her Prescription. 

![qr_code](https://github.com/aakashdinkar/VoiceCription/blob/master/datafiles/qr.png?raw=true)


**How to run it ?**
</br>
Clone the repo:
```bash
$ cd VoiceCription
$ python install -r requirements.txt
$ python manage.py runserver 3000
```
Additionally for installing PyAudio, you have to install a package i.e.
```bash
$ pip install pipwin
$ pipwin install pyaudio
```

To upload and extract prescription, I have used Google Drive API. To continue with this API, secret-credentials which you can download from login into [Developer Console](https://developers.google.com/drive). 
After downloading your own credentials place in this directory with name **client_secrets.json**.
```bash
├───assets
├───datafiles
├───media
│   └───images
├───Voice
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───Voice
│   └───__pycache__
└───VoiceCription
    └───__pycache__
```

---

**Feel free for requesting PRs to contribute or any modification.**
