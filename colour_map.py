 #######################################
 
  #COLOUR MAP DEFINITION AND CHANGE

  # A small collection of tools to really eff up your colour map for fun and profit.

  #######################################

  
def discrete_cmap(N=10):
  """create a c colormap with N (N<12) discrete colors and register it"""
   import matplotlib
   import matplotlib.colors as col
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt
   import numpy as np

   # define individual colours as hex values
   #clog=['#0000FF','#0099FF','#00FFFF','#66FF00','#CCFF00',
   #	 '#FFFF00','#FFCC00','#FF9900','#FF3300','#CC0000',
   #	 '#CC00CC','#FFCCFF']
   
   clog=['#CC00CC','#CC00CC','#CC00CC','#CC00CC','#CC00CC',
   	'#CC00CC','#CC00CC','#CC00CC','#CC00CC','#CC00CC',
	'#CC00CC','#CC00CC','#CC00CC','#CC00CC','#CC00CC']
   cmap3=col.ListedColormap(clog[0:N],'indexed')
   cm.register_cmap(cmap=cmap3)
   
 #######################################   
  
def cmap_map(function,cmap):
  """ Applies function (which should operate on vectors of shape 3:
  [r, g, b], on colormap cmap. This routine will break any discontinuous     points in a colormap.
  """
  import matplotlib
  from numpy import array
  cdict = cmap._segmentdata
  step_dict = {}
  # First get the list of points where the segments start or end
  for key in ('red','green','blue'): step_dict[key] = map(lambda x: x[0], cdict[key])
  step_list = sum(step_dict.values(), [])
  step_list = array(list(set(step_list)))
  # Then compute the LUT, and apply the function to the LUT
  reduced_cmap = lambda step : array(cmap(step)[0:3])
  old_LUT = array(map( reduced_cmap, step_list))
  new_LUT = array(map( function, old_LUT))
  # Now try to make a minimal segment definition of the new LUT
  cdict = {}
  for i,key in enumerate(('red','green','blue')):
      this_cdict = {}
      for j,step in enumerate(step_list):
          if step in step_dict[key]:
              this_cdict[step] = new_LUT[j,i]
          elif new_LUT[j,i]!=old_LUT[j,i]:
              this_cdict[step] = new_LUT[j,i]
      colorvector=  map(lambda x: x + (x[1], ), this_cdict.items())
      colorvector.sort()
      cdict[key] = colorvector

  return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)

  #######################################

def cmap_xmap(function,cmap):
  """ Applies function, on the indices of colormap cmap. Beware, function
  should map the [0, 1] segment to itself, or you are in for surprises.

  See also cmap_xmap.
  """
  import matplotlib
  from numpy import array
  cdict = cmap._segmentdata
  function_to_map = lambda x : (function(x[0]), x[1], x[2])
  for key in ('red','green','blue'): cdict[key] = map(function_to_map, cdict[key])
  cdict[key].sort()
  assert (cdict[key][0]<0 or cdict[key][-1]>1), "Resulting indices extend out of the [0, 1] segment."

  return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)

  #######################################

def show_cmaps(names=None):
    """display all colormaps included in the names list. If names is None, all
    defined colormaps will be shown."""
    import matplotlib
    import matplotlib.colors as col
    import matplotlib.cm as cm
    import matplotlib.pyplot as plt
    import numpy as np

    # base code from http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
    matplotlib.rc('text', usetex=False)
    a=np.outer(np.arange(0,1,0.01),np.ones(10))   # pseudo image data
    f=plt.figure(figsize=(10,5))
    f.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
    # get list of all colormap names
    # this only obtains names of built-in colormaps:
    maps=[m for m in cm.datad if not m.endswith("_r")]
    # use undocumented cmap_d dictionary instead
    maps = [m for m in cm.cmap_d if not m.endswith("_r")]
    maps.sort()
    # determine number of subplots to make
    l=len(maps)+1
    if names is not None: l=len(names)  # assume all names are correct!
    # loop over maps and plot the selected ones
    i=0
    for m in maps:
        if names is None or m in names:
            i+=1
            ax = plt.subplot(1,l,i)
            ax.axis("off")
            plt.imshow(a,aspect='auto',cmap=cm.get_cmap(m),origin="lower")
            plt.title(m,rotation=90,fontsize=10,verticalalignment='bottom')
    plt.savefig("colormaps.png",dpi=100,facecolor='gray')
