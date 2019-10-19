# RETEA-Real Time Evaluation of Asteroid

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

                  x_i=(x_i-µ_i)/Range
Our next step is to just define a hypothesis function, h :

                  h_⁡θ(x) = x_0 θ_0+ θ_1x_1+ θ_2x_2
The hypothesis can either be polynomial or linear depending on the kind of data collected.

Our next step is to choose the best values of θ0, θ1 and θ2 such that the hypothesis, h
can pass through the maximum number of points and thus produce a graph that
accurately predicts data.
The way to do this is by defining a cost function J(θ0,θ1,θ2) and trying to obtain the
minimum value for it ,since, cost function is nothing but 1/2m * (The sum of the square
distance of a test point from the linear/polynomial regression line)
The cost function is defined as follows: 

                  J(θ) = 1/2m (Σ (hϴ(x(i) - y(i))2) 

where,<br/>
 θ→ The vector of θi defined above<br/>
 m→ The number of training examples
 
Now, using random values of θi, we obtain values of J(θ) and plot a contour graph
between J(θ) and θ1 and θ2.

To find the minimum value J(θ), we employ a
gradient descent algorithm which looks like this:<br/>
Repeat {<br/>
                 θj := θj - α (ϑ/ϑθj)J(θ)
}<br/>
OR<br/>
Repeat {<br/>
                 θj := θj - α (1/m)(hθ(x(i))-y(i))(xj(i))<br/>
}<br/>

This statement is further equivalent to:

Repeat {<br/>
                 θ0 := θ0 - α (1/m)(hθ(x(i))-y(i))(x0(i))<br/>
                 θ1 := θ1 - α (1/m)(hθ(x(i))-y(i))(x1(i))<br/>
                 θ2 := θ2 - α (1/m)(hθ(x(i))-y(i))(x2(i))<br/>
}<br/>

where,<br/>
α→learning rate<br/>
The gradient descent algorithm will start with random values of θ[] and keep changing
θ[] to reduce J(θ) until we end up at a minimum. <br/>
The values of θ[] corresponding to the minimum value of J(θ) can be put back into the<br/>
hypothesis function which can now be successfully used to predict whether an asteroid<br/>
will come near the earth or not depending on its values of rotation, reflectivity and
composition. <br/>

# Asteroid Deflection Mechanisms 
We propose to build a small space station that will be the storage site for the
Photons aggregated from the sun.

Inside the space station we will have collider that works on the principle of
Second Harmonic generation (SHG)( In the process non-linear material are
effectively "combined" to generate new photons with twice the energy, and
therefore twice the frequency and half the wavelength of the initial photons.)

The collider will basically keep on combining 2 photons to develop the 3rd
photon with a different angular frequency and then combine the newly
generated photons too, continuing this process to store up Photons of huge
energy and also conserving their momentum until an asteroid is detected to be
deflected.

Once the asteroid is detected The space station will use the stored Photons.The
asteroids course will then be changed by a beam of highly dense anisotropic
emission of thermal Photons that will deflect the asteroid by the phenomenon of
the Yarkovsky effect. <br/>

![example](harmonic.png)

# IMPACT ENERGY AND RECURRENCE INTERVAL
The most fundamental quantity in assessing the
environmental consequences of the impact is the energy
released during the impact, which is related to the kinetic
energy of the impactor E before atmospheric entry begins. At
normal solar system impact speeds, E is approximately given
as one half times the impactor mass mi times the square of the
impactor velocity v0, which can be rewritten in terms of the
meteoroid’s density pi and diameter L0, assuming that the
meteoroid is approximately spherical:</br>
![example1](/Equation/1.PNG)</br>
fact, the program uses the relativistic energy equation
to accommodate the requests of several science fiction
writers. The program does not limit the impact velocity to 72 km s􀀐1, the maximum possible for an impactor bound to the Sun; however, we have limited the maximum velocity to the speed of light.</br>
Natural objects that encounter the Earth are either
asteroids or comets. Asteroids are made of rock ( p i ~2000–
3000 kg m3; Hilton 2002) or iron ( p i ~8000 kg m3) and
typically collide with the Earth’s atmosphere at velocities of
12–20 km s􀀐1 (Bottke et al. 1994). Detailed knowledge of the
composition of comets is currently lacking; however, they are
of much lower density ( p i ~500–1500 kg m3) and are composed
mainly of ice (Chapman and Brandt 2004). Typical velocities
at which comets might encounter the Earth’s atmosphere are in
the range of 30–70 km s^-1 (Marsden and Steel 1994). Thus, an
asteroid or comet typically has 4–20 times the energy per unit
mass of TNT at the moment atmospheric entry begins.
Therefore, impact events have much in common with chemical
and nuclear explosions, a fact that we will rely on later in our
estimates of the environmental effects of an impact
Observations of near-Earth objects made by several
telescopic search programs show that the number of near-
Earth asteroids with a diameter greater than Lkm (in km) may
be expressed approximately by the power law (Near-Earth
Object Science Definition Team 2003):</br>

![example2](/Equation/2.PNG)</br>

These data may also be represented in terms of the
recurrence interval TRE in years versus the impact energy EMt
in megatons of TNT by assuming a probability of a singleobject
collision with Earth (~1.6 × 10􀀐9 yr􀀐1; Near-Earth Object Science Definition Team 2003; their Fig. 2.3) and multiplying
by the number of asteroids of a given potential impact energy
that are estimated to be circling the sun with potentially
hazardous, Earth-crossing orbits. We found that a simple
power-law relationship adequately represents these data:</br>

![example2](/Equation/3.PNG)</br>

Thus, for a given set of user-input impact parameters (L0,
v0, pi, pt, and θ), the program computes the kinetic energy
(EMt, in megatons; 1 Mt = 4.18 × 1015 J) possessed by the
impacting body when it hits the upper atmosphere and defines
an average time interval between impacts of that energy,
somewhere on the Earth. Furthermore, we estimate the
recurrence interval TRL for impacts of this same energy within
a certain specified distance r of the impact. This is simply the
product of the recurrence interval for the whole Earth and the
fraction of the Earth’s surface area that is within the distance r:</br>

![example2](/Equation/4.PNG)</br>

where △ is the epicentral angle from the impact point to a
range r.</br>
