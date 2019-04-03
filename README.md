# PyTuner
A Personal Guitar Tuner created with Speech Recognition and SciPy. Use it to tune your instrument!

Make sure you have python3 installed, as well as SciPy, Speech Recognition, pyaudio, and path modules.

Just run the tune.py file with python3:

```python3 tune.py```

And here might be the result:

```(g4-)=369 [<-] to -> (g4 )=392```

Basically, the scheme is note=freq, and the arrows represent how close the note you 
played is to the outer range. In this case, your note is closer to a G-flat 4 than a G-4.
Possible notes include all the notes from C-0 to B-8 for every half-step. 

