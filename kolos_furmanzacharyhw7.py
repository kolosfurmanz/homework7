import numpy as np 
import matplotlib.pyplot as plt
from astropy import units as u 
#importing necessary libraries 

data = open("sed.txt","r")
lines = data.readlines() 
#inputting the data via the text file and having Python read the values themselves

wavelength = [float(x.split(",")[0]) for x in lines]
luminosity = [float(y.split(",")[1]) for y in lines]
#this separates the values into x and y so a graph can be made 

a = np.array(wavelength) 
b = np.array(luminosity) 
#making the lists into arrays so the integral can actually be taken 

c = np.where(a == 10.000784441103388) 
print("The integral must be taken from the first wavelength term to the following term:", c[0]) 
#I found the lower bound of the integral by looking at what value in the list was closest to 10 and taking the index np.where found as the lower bound in the integral 

a *= u.micron 
b *= u.Lsun/u.micron  
#using astropy units to give the arrays their proper units 

fig, graph = plt.subplots()
graph.plot(wavelength, luminosity)
graph.set_xscale("log")
graph.set_yscale("log")
graph.set(xlabel = "Wavelength in microns", ylabel = "Luminosity in Lsun/micron")
plt.title("Luminosity vs Wavelength")
plt.savefig("hw7graph.png", dpi = 300)
#code for the graph itself, making the x and y-scales logarithmic 

integral = (np.trapz(b[0:833], x = -a[0:833])).to(u.erg/u.s)
print("The integral from wavelengths 10 to 1000 microns equals", integral) 
#final code for the integral itself starting from the 1st term, the x-values are negative since the wavelengths decrease making the integral result positive 
