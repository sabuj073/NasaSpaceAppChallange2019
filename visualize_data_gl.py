from datetime import datetime
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Define Julian epoch
J2000_EPOCH = datetime(2000, 1, 1, 12) # At the noon of 2000/01/01 UTC

class Planet(object):
    """ Defines a planet in the Solar system. """

    def __init__(self, a, lambda0, e, I, lon_of_peri, node, T, color='blue', size=20):
        """
        Args: 
            a (float): semi-major axis (AU)
            lambda0 (float): mean longitude at epoch (degrees)
            e (float): eccentricity
            I (float): inclination (degrees)
            lon_of_peri (float): longitude of perihelion (degrees)
            node (float): longitude of ascending node (degrees)
            T (float): orbital period (years)
        Keyword args:
            color (str): planet color
            size (float): planet plot size
        """

        self.a = a
        self.lambda0 = lambda0
        self.e = e
        self.I = I
        self.lon_of_peri = lon_of_peri
        self.node = node
        self.T = T
        self.color = color
        self.size = size

        # Mean orbital angular velocity, in radians per year
        self.n = 2*np.pi/self.T

    def getPosition(self, t):
        """ Returns the planet's position in a given time. 
        Args:
            t (datetime): a point in time of the planet's orbit
        """

        E = self.solveForE(t)

        x, y, z = orbitalElements2Cartesian(self.a, self.e, self.I, self.lon_of_peri - self.node, self.node, E)

        return x, y, z


    def solveForE(self, t, E=0, n=15):
        """ Find the eccentric anomaly using the iterative method. 
        Args:
            t (float): a point in time of the planet's orbit (years from epoch)
        Keyword args:
            E (float): initial value of the eccentric anomaly for iteration
            n (int): number of iterations
        """

        # Time of perihelion passage
        tau = np.radians(self.lon_of_peri - self.lambda0)/self.n

        # Mean anomaly
        M = self.n*(t-tau)

        def f(E, e, M):
            return M + e*np.sin(E)

        # Solve for eccentric anomaly using the iterative method
        for i in range(n):
            E = f(E, self.e, M)

        return E

    def plotPlanet(self, ax, time):
        """ Plot the planet and its orbit on a 3D plot. 
        Args:
            ax (matplotlib object): 3D plot object
            time (float): years from J2000.0 epoch
        """

        # Eccentric anomaly (all ranges)
        E = np.linspace(-np.pi, np.pi, 100)

        # Plot the planet
        x, y, z = self.getPosition(time)
        ax.scatter(x, y, z, c=self.color, s=self.size, edgecolors='face')

        # Plot planet's orbit
        x, y, z = orbitalElements2Cartesian(self.a, self.e, self.I, self.lon_of_peri - self.node, 
            self.node, E)

        ax.plot(x, y, z, color=self.color, linestyle='-', linewidth=0.5)



def orbitalElements2Cartesian(a, e, I, peri, node, E):
    """ Convert orbital elements to Cartesian coordinates in the Solar System.
    Args: 
        a (float): semi-major axis (AU)
        e (float): eccentricity
        I (float): inclination (degrees)
        peri (float): longitude of perihelion (degrees)
        node (float): longitude of ascending node (degrees)
        E (float): eccentric anomaly (radians)
    """

    # Check if the orbit is parabolic or hyperbolic
    if e >=1:
        e = 0.99999999


    # Convert degrees to radians
    I, peri, node = map(np.radians, [I, peri, node])

    # True anomaly
    theta = 2*np.arctan(np.sqrt((1.0 + e)/(1.0 - e))*np.tan(E/2.0))

    # Distance from the Sun to the poin on orbit
    r = a*(1.0 - e*np.cos(E))

    # Cartesian coordinates
    x = r*(np.cos(node)*np.cos(peri + theta) - np.sin(node)*np.sin(peri + theta)*np.cos(I))
    y = r*(np.sin(node)*np.cos(peri + theta) + np.cos(node)*np.sin(peri + theta)*np.cos(I))
    z = r*np.sin(peri + theta)*np.sin(I)

    return x, y, z

def plotPlanets(ax, time):
    """ Plots the Solar system planets. 
    Args:
        ax (matplotlib object): 3D plot object
        time (float): years from J2000.0 epoch
    """

    # Generate Planets (J2000.0 epoch)
    mercury = Planet(0.3871, 252.25, 0.20564, 7.006, 77.46, 48.34, 0.241, color='#ecd67e', size=10)
    venus = Planet(0.7233, 181.98, 0.00676, 3.398, 131.77, 76.67, 0.615, color='#e7d520', size=30)
    earth = Planet(1.0000, 100.47, 0.01673, 0.000, 102.93, 0, 1.000, color='#1c7ff2', size=30)
    mars = Planet(1.5237, 355.43, 0.09337, 1.852, 336.08, 49.71, 1.881, color='#cc1e2c', size=20)
    jupiter = Planet(5.2025, 34.33, 0.04854, 1.299, 14.27, 100.29, 11.87, color='#D8CA9D', size=55)
    saturn = Planet(9.5415, 50.08, 0.05551, 2.494, 92.86, 113.64, 29.47, color='#ead6b8', size=45)
    uranus = Planet(19.188, 314.20, 0.04686, 0.773, 172.43, 73.96, 84.05, color='#287290', size=40)
    neptune = Planet(30.070, 304.22, 0.00895, 1.770, 46.68, 131.79, 164.9, color='#70B7BA', size=40)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # Plot the Sun
    ax.scatter(0, 0, 0, c='yellow', s=100)

    # Plot planets
    for planet in planets:
        planet.plotPlanet(ax, time)



def plotOrbits(orb_elements, time, orbit_colors=None, plot_planets=True):
    """ Plot the given orbits in the solar system. 
    Args:
        orb_elements (ndarray of floats): 2D numpy array with orbits to plot, each entry contains:
            a - Semimajor axis (AU)
            e - Eccentricity
            I - Inclination (degrees)
            peri - Argument of perihelion (degrees)
            node - Ascending node (degrees)
        ax (matplotlib object): 3D plot object
        time (datetime): datetime object of the time of the desired planet positions
    """

    # Check the shape of given orbital elements array
    if len(orb_elements.shape) < 2:
        orb_elements = np.array([orb_elements])


    # Calculate the time difference from epoch to the given time (in years)
    julian = (time - J2000_EPOCH)
    years_diff = (julian.days + (julian.seconds + julian.microseconds/1000000.0) /86400.0)/365.2425

    # Setup the plot
    fig = plt.figure()
    ax = fig.gca(projection='3d', axisbg='black')

    # Set a constant aspect ratio
    ax.set_aspect('equal', adjustable='box-forced')

    # Hide the axes
    ax.set_axis_off()
    ax.grid(b=False)

    # Plot the solar system planets
    if plot_planets:
        plotPlanets(ax, years_diff)


    # Eccentric anomaly (full range)
    E = np.linspace(-np.pi, np.pi, 100)

    # Plot the given orbits
    for i, orbit in enumerate(orb_elements):
        a, e, I, peri, node = orbit

        # Take extra steps in E if the orbit is very large
        if a > 50:
            E = np.linspace(-np.pi, np.pi, (a/20.0)*100)

        # Get the orbit in cartesian space
        x, y, z = orbitalElements2Cartesian(a, e, I, peri, node, E)

        # Check if the colors orbit are provided
        if orbit_colors:
            color = orbit_colors[i]
        else:
            # Set to default
            color = '#32CD32'

        # Plot orbits
        ax.plot(x, y, z, c=color)

    ax.legend()

    # Add limits (in AU)
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)

    plt.tight_layout()
    plt.show()



if __name__ == '__main__':

    # Time now
    time = datetime.now()


    # Define orbits to plot
    # a, e, incl, peri, node
    orb_elements = np.array([
        [2.363, 0.515, 4.0, 205.0, 346.1],
        [0.989, 0.089, 3.1, 55.6, 21.2],
        [0.898, 0.460, 1.3, 77.1, 331.2],
        [184.585332285, 0.994914, 89.3950, 130.8767, 282.4633]
        ])

    # Plot orbits
    plotOrbits(orb_elements, time)
