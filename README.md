# MLxTBD
A machine learning-guided web app is for supporting the clinician in the telomeropathy diagnosis.

In the backend, a random forest classifier algorithm is trained on a hidden dataset of about 50 patients.

Plase note that it is just a prototype.

The first page is designed for any user who wants to have an AI diagnosis support.
The second page is specific for the analysis we did.

To make it work, you need to install the following Python libraries:
- streamlit
- pandas
- numpy
- pickle
- plotly

And you need to create the file:
.streamlit/config.toml
```
[server]
port = "PORT"

[browser]
serverAddress = "DOMAIN SERVER"
```

And if you want to make the second page work, you need to create the file:
df_clusters3D.csv
This file is the result of a specific clustering analysis where "Cluster" represents the assigned cluster label to each subject and dim1, dim2, dim3 are the dimensions to visualize it. 


To launch the web app:
```
streamlit run telomeropathySupport/TBD.py
```

Enjoy!

