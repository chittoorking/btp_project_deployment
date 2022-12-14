# About the Project
## The Project is Digital Twin Manufacturing using data analytics
The code from data collection to the model building is present in the ipynb notebook in the Python code folder

### Walk through of the notebook
- We imported the necessary libraries
- Mount to the google drive 
- Change the path to the folder where the dataset is downlaoded in the drive
- Load the dataset in the mat format and convert it into csv format and load the dataframe
- In the dataframe the column names are actually the indexes and the indexes are the columns. We will transpose the DataFrame to make them proper.
- Rename the columns in the dataframe
- Synthetic data generation
- Exploratory data analytics(Histograms,Correlation analysis,Heatmaps)
- Outlier Detection and removal
- Model building for predicting final positions and velocities
- Model building for detecting anomaly along with addressing class imbalance problem
- Select the best model in terms of accuracy and F1 score( Decision Tree Classifier)
- Link to previous deployment on streamlit

### Files in the current folder
- Dockerfile is the final Docker image 
- app.py is the Flask application built
- templates folder and static/css folders contains the html and css files related to the Flask application
- clf_model is the DecisiontTree classification model
- model.h5 and model.json are the model weights of ANN model built for predicting final positions and velocities in h5 and json format respectively
- requirements.txt file is the libraries that will be installed during docker deployment

# Deployment using Docker
- First, using the Flask a simple Web Application was made.
- Download a ubuntu virtual machine and install docker using official documentation
- Setup Docker Daemon
- Go to project folder where Dockerfile is present. Dockerfile is used for building of the docker image.
- In my case it it btp_project_deployment
- Use the below command for build the docker image

docker build -t <name> .

- Use the following command for viewing all the docker images

docker images

- Run the docker container using the below command

docker run -d -p 5000:5000 <name>

- Open the flask app running on port 5000 in any web browser available

localhost:5000

- Give the inputs and click on predict and the app will run the model and predict if there is any anomaly or not 
- 1 indicate anomaly and 0 indicate no anomaly
- We can know which docker containers are running using

docker ps

- Stop the docker container from running by using
 
docker stop <id>

- Delete the image by using the following command

docker image rm -f <image name>


###Future work:
The docker image can be deployed in cloud services such as AWS,Azure or GCP and testing for scaling and availability in poduction.
