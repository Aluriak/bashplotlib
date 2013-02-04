#bashplotlib
*plotting in the terminal*

<p>bashplotlib is a python package and command line tool for making basic plots in the terminal. I use it to help keep tabs on logfiles and processes running on EC2 servers.</p>

##installation
<h5>install with pip</h5>
<pre>
	$ pip install bashplotlib
</pre>
<h5>install from source</h5>
<pre>
	$ git clone git@github.com:glamp/bashplotlib.git
	$ cd bashplotlib
	$ python setup.py install
</pre>

<p>This will install the bashplotlib python package and will also add <code>hist</code> and <code>scatter</code> 
to your python scripts folder. This folder should be on your path (add it if it's not).</p>

##features
<ul>
    <li>quick plotting from the command line</li>
    <li>pipe data into plots with stdin</li>
</ul>

##usage
<h5>command line</h5>
<p>this is how you use it from the command line</p>
<h5>in python</h5>
<p>this is how you use it in python</p>

##examples
<pre>$ scatter -f data/texas.txt --pch .</pre>
<img src="examples/texas.png">

<pre>$ hist data/exp.txt</pre>
<img src="examples/histogram.png">

<pre>$ scatter -x data/x_test.txt -y data/y_test.txt</pre>
<img src="examples/scatter.png">

<pre>$ scatter -f data/lower48.txt -s 40 --pch .</pre>
<img src="examples/usa.png">

##todo
<ul>
	<li>sideways numbers for x-axis of histograms</li>
	<li>colors for individual points</li>
	<li>line charts</li>
	<li>trendlines</li>
</ul>

