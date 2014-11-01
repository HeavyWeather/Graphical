def hillshade(data,scale=10.0,azdeg=165.0,altdeg=45.0):
  ''' 
    This code thanks to Ran Novitsky Nof
  http://rnovitsky.blogspot.co.uk/2010/04/using-hillshade-image-as-intensity.html
  Repeated here to make my cyclopean uk_map code prettier.

  convert data to hillshade based on matplotlib.colors.LightSource class.
    input:
         data - a 2-d array of data
         scale - scaling value of the data. higher number = lower gradient
         azdeg - where the light comes from: 0 south ; 90 east ; 180 north ;
                      270 west
         altdeg - where the light comes from: 0 horison ; 90 zenith
    output: a 2-d array of normalized hilshade
  '''
  
  from pylab import pi, gradient, arctan, hypot, arctan2, sin, cos
  # convert alt, az to radians
  az = azdeg*pi/180.0
  alt = altdeg*pi/180.0
  # gradient in x and y directions
  dx, dy = gradient(data/float(scale))
  slope = 0.5*pi - arctan(hypot(dx, dy))
  aspect = arctan2(dx, dy)
  intensity = sin(alt)*sin(slope) + cos(alt)*cos(slope)*cos(-az - aspect - 0.5*pi)
  intensity = (intensity - intensity.min())/(intensity.max() - intensity.min())
  return intensity
