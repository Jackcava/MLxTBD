# MLxTBD
A machine learning-guided web app is for supporting the clinician in the telomeropathy diagnosis.

In the backend, a random forest classifier algorithm is trained on a hidden dataset of about 50 patients.

Plase note that it is just a prototype.

To make it work, you need to install the following Python libraries:
- streamlit
- pandas
- numpy
- pickle
- plotly

And you may need to create the file:
.streamlit/config.toml
```
[server]
port = "PORT"

[browser]
serverAddress = "DOMAIN SERVER"
```

To launch the web app:
```
streamlit run TBD.py
```

Enjoy!

