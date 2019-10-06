# RTEA-Real Time Evaluation of Asteroid

We have used machine learning technique(Deep Neural Network) to classify near earth objects whether they are hazardous to earth or not and predict impact if any asteroid hit the earth.
NEO that can hit earth are visualised in 3d in our web app.
Project includes the following features - 
 - Hazardous asteroid nformation from NASA directory(using API) in real time.
 - Close approach date and time.
 - Asteroid orbit visualisation in 3d
 - Asteroid impact information

Api used here are 
- https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=3vgYWNjKFyD7st8laqSmoZBka5uHuluQcYXusMtr
- https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=3vgYWNjKFyD7st8laqSmoZBka5uHuluQcYXusMtr

# Prediction of Threat
Machine Learning is a technique which can be used to predict whether a Near Earth
Object poses a threat to planet Earth or not by analysing its mundane features such as
reflectivity ,rotation and composition and then comparing these features to those of the
NEOs which entered the Earth’s atmosphere.
The training set or the previous data set of asteroid detection can be the following: 






| Composition(x1)  | Reflectivity (x2)  | Rotation (x3)     | Minimum distance of the asteroids trajectory from Earth (y)|
| ---------------- | ------------------ |-------------------|------------------------------------------------------------|
| Data from NEOWISE| Data from NEOWISE  | Data from NEOWISE |    Data from NEOWISE                                       |


Using a mean normalisation method, we scale the values of x1, x2 and x3 so that they lie
between -1<=xi<=1 and it is easy for the other machine learning algorithms to work
their way around the data : 
